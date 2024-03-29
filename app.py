import os
import json
import requests
import math
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

RAWG_API_KEY = os.environ.get("RAWG_API_KEY")
RAWG_API_URL = "https://api.rawg.io/api/games"

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    recent_reviews = mongo.db.game_reviews.find().sort([('_id', -1)]).limit(3)
    return render_template("base.html", recent_reviews=recent_reviews)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("Sign up Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    current_username = session.get("user")
    user_reviews = mongo.db.game_reviews.find({"username": username})
    return render_template("profile.html", username=username, current_username=current_username, user_reviews=user_reviews)


@app.route("/log_out")
def log_out():
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/get_game_reviews")
def get_game_reviews():
    page = request.args.get("page", 1, type=int)
    per_page = 5  
    start_index = (page - 1) * per_page
    total_reviews = mongo.db.game_reviews.count_documents({})
    total_pages = math.ceil(total_reviews / per_page)
    games = mongo.db.game_reviews.find().skip(start_index).limit(per_page)
    return render_template("game_reviews.html", games=games, per_page=per_page, total_reviews=total_reviews, total_pages=total_pages, page=page)


@app.route("/search_game")
def search_game():
    return render_template("search_game.html")


@app.route("/search_results", methods=["GET", "POST"])
def search_results():
    if request.method == "POST":
        query = request.form.get("query")
    else:
        query = request.args.get("query")

    page = request.args.get("page", 1, type=int)
    per_page = 5

    start_index = (page - 1) * per_page

    url = f"{RAWG_API_URL}?key={RAWG_API_KEY}&search={
        query}&page_size={per_page}&page={page}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        games = data.get("results", [])
        total_results = data.get("count", 0)

        total_pages = math.ceil(total_results / per_page)

        return render_template("search_results.html", games=games, total_results=total_results,
                               per_page=per_page, page=page, query=query, total_pages=total_pages)
    else:
        return "Error searching for the game."


@app.route("/game_info")
def game_info():
    game = request.args.get("game")
    game_dict = eval(game)
    url = f"{RAWG_API_URL}/{game_dict['id']}?key={RAWG_API_KEY}"
    url_tags = f"https://api.rawg.io/api/tags?key={RAWG_API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        game_data = response.json()
        response_tags = requests.get(url_tags)
        if response_tags.status_code == 200:
            tags_data = response_tags.json()

            game_tags = set(tag['slug'] for tag in tags_data['results'])
            relevant_tags = [tag['name'] for tag in game_data.get(
                'tags', []) if 'singleplayer' in tag['slug'] or 'multiplayer' in tag['slug']]
            return render_template("game_info.html", game_data=game_data, relevant_tags=relevant_tags)
        else:
            return f"Error fetching tags: {response_tags.status_code}"
    else:
        return f"Error fetching game details: {response.status_code}"


@app.route("/add_game", methods=["POST"])
def add_game():
    if request.method == "POST":
        username = session.get("user")
        game_id = request.form.get("game_id")
        name = request.form.get("name")
        background_image = request.form.get("background_image")
        description = request.form.get("description")
        released = request.form.get("released")
        genres = request.form.getlist("genres")
        developers = request.form.getlist("developers")
        publishers = request.form.getlist("publishers")
        platforms = request.form.getlist("platforms")
        tags = request.form.getlist("tags")
        review = request.form.get("review")
        rating = float(request.form.get("rating"))

        game = {
            "username": username,
            "game_id": game_id,
            "name": name,
            "background_image": background_image,
            "description": description,
            "released": released,
            "genres": genres,
            "developers": developers,
            "publishers": publishers,
            "platforms": platforms,
            "tags": tags,
            "review": review,
            "rating": rating
        }

        mongo.db.game_reviews.insert_one(game)

        flash("Game added successfully!")
        return redirect(url_for("search_game"))
    else:
        return "Method not allowed"


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    existing_review = mongo.db.game_reviews.find_one(
        {"_id": ObjectId(review_id)}
    )
    if request.method == "POST":
        if "user" not in session or session["user"] != existing_review["username"]:
            abort(403)
        review = request.form.get("review")
        rating = float(request.form.get("rating"))

        mongo.db.game_reviews.update_one(
            {"_id": ObjectId(review_id)},
            {"$set": {
                "review": review,
                "rating": rating
            }}
        )
        flash("Game review updated successfully!")
        return redirect(url_for("profile", username=session.get("user")))
    else:
        if existing_review:
            game_id = existing_review["game_id"]
            url = f"{RAWG_API_URL}/{game_id}?key={RAWG_API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                game_data = response.json()
                return render_template("profile.html", review=existing_review, game_data=game_data)
            else:
                flash("Error fetching game information")
                return redirect(url_for("profile", username=session.get("user")))
        else:
            flash("Review not found")
            return redirect(url_for("profile", username=session.get("user")))


@app.route("/delete_review/<review_id>", methods=["POST"])
def delete_review(review_id):
    review = mongo.db.game_reviews.find_one({"_id": ObjectId(review_id)})

    if not review:
        flash("Review not found")
        return redirect(url_for("profile", username=session.get("user")))

    if "user" not in session or session["user"] != review["username"]:
        abort(403)

    mongo.db.game_reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review deleted successfully")

    return redirect(url_for("profile", username=session.get("user")))


@app.route("/delete_account", methods=["POST"])
def delete_account():
    if "user" in session:
        mongo.db.users.delete_one({"username": session["user"]})

        mongo.db.game_reviews.delete_many({"username": session["user"]})

        session.pop("user")
        flash("Your account and associated reviews have been deleted successfully.")
        return redirect(url_for("home"))
    else:
        flash("You must be logged in to delete your account.")
        return redirect(url_for("log_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Make false when deployed!

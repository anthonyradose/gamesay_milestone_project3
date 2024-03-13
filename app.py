import os
import json
import requests
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
    return render_template("base.html")

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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("log_in"))

@app.route("/log_out")
def log_out():
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))

@app.route("/get_games")
def get_games():
    games = mongo.db.games.find()
    return render_template("games.html", games = games)

@app.route("/search_game")
def search_game():
    return render_template("search_game.html")


@app.route("/search_results", methods=["GET", "POST"])
def search_results():
    query = request.form.get("query")
    url = f"{RAWG_API_URL}?key={RAWG_API_KEY}&search={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        games = [game for game in data.get("results", [])]
        return render_template("search_results.html", games=games)
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
            
            relevant_tags = [tag['name'] for tag in game_data.get('tags', []) if tag['slug'] in game_tags]
            
            return render_template("game_info.html", game_data=game_data, relevant_tags=relevant_tags)
        else:
            return f"Error fetching tags: {response_tags.status_code}"
    else:
        return f"Error fetching game details: {response.status_code}"




if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True) #Make false when deployed!
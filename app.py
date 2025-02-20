import os  # Importing necessary modules
import requests
from requests.exceptions import HTTPError, RequestException
import math
from flask import (Flask, flash, render_template, redirect,
                   request, session, url_for, abort)
from flask_pymongo import PyMongo
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):  # Check if environment file exists
    import env


app = Flask(__name__)  # Initialize Flask app


# Setting up MongoDB connection
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Secret key for session management
app.secret_key = os.environ.get("SECRET_KEY")

# Initialize PyMongo
mongo = PyMongo(app)


# Get API key and base URL from environment variables
RAWG_API_KEY = os.environ.get("RAWG_API_KEY")
RAWG_API_URL = "https://api.rawg.io/api/games"


def fetch_api_data(url):
    """
    Utility function to fetch and return data from RAWG API.
    """
    try:
        response = requests.get(url)
        return response.json()
    except HTTPError as http_err:
        # Raise HTTPError to be handled by the caller
        raise RuntimeError(f"HTTP error occurred: {http_err}") from http_err
    except RequestException as req_err:
        # Raise RequestException to be handled by the caller
        raise RuntimeError(f"Request error occurred: {req_err}") from req_err
    except Exception as err:
        # Raise generic Exception to be handled by the caller
        raise RuntimeError(f"An unexpected error occurred: {err}") from err


@app.route("/")
def home():
    """
    Finds recent reviews and renders home page
    """
    recent_reviews = mongo.db.game_reviews.find().sort([('_id', -1)]).limit(3)
    return render_template("base.html", recent_reviews=recent_reviews)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    Handle user registration and redirection to the profile page.
    """
    # Prevent logged-in users from accessing the sign-up page
    if "user" in session:
        flash("You are already logged in.", 'warning')
        return redirect(url_for("profile", username=session["user"]))
    if request.method == "POST":
        try:
            email = request.form.get("email").lower()
            username = request.form.get("username").lower()
            password = request.form.get("password")
            # Check if the username or email already exists
            existing_email = mongo.db.users.find_one({"email": email})
            existing_user = mongo.db.users.find_one({"username": username})
            if existing_user:
                flash("User already exists.", 'warning')
                return redirect(url_for("sign_up"))
            if existing_email:
                flash("Email already exists.", 'warning')
                return redirect(url_for("sign_up"))
            # Create a new user document
            sign_up = {
                "email": email,
                "username": username,
                "password": generate_password_hash(password)
            }
            mongo.db.users.insert_one(sign_up)
            # Log the user in and redirect to their profile
            session["user"] = username
            flash("Sign up successful!", 'success')
            return redirect(url_for("profile", username=username))
        except PyMongoError:
            # Handle database-specific errors
            flash("A database error occurred. Please try again later.", "danger")
            return redirect(url_for("home"))
        except Exception:
            # Handle other unexpected errors
            flash("An unexpected error occurred. Please try again later.", "danger")
            return redirect(url_for("home"))
    # Render the sign-up page for GET requests
    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """
    Handle user authentication and redirection to the profile page.
    """
    # Prevent logged-in users from accessing the log-in page
    if "user" in session:
        flash("You are already logged in.")
        return redirect(url_for("profile", username=session["user"]))
    if request.method == "POST":
        try:
            username = request.form.get("username").lower()
            password = request.form.get("password")
            # Check if the user exists in the database
            existing_user = mongo.db.users.find_one({"username": username})
            if existing_user:
                # Verify the password
                if check_password_hash(existing_user["password"], password):
                    session["user"] = username
                    flash(f"Welcome, {username}!", "info")
                    return redirect(url_for("profile", username=username))
                else:
                    flash("Incorrect Username and/or Password.", "danger")
                    return redirect(url_for("log_in"))
            else:
                flash("User not found. Please check your username.", "danger")
                return redirect(url_for("log_in"))
        except PyMongoError:
            # Handle database-specific errors
            flash("A database error occurred. Please try again later.", "danger")
            return redirect(url_for("home"))
        except Exception:
            # Handle other unexpected errors
            flash("An unexpected error occurred. Please try again later.", "danger")
            return redirect(url_for("home"))
    # Render the log-in page for GET requests
    return render_template("log_in.html")


@app.route("/log_out")
def log_out():
    """
    Log out user and redirect to log in page.
    """
    if "user" in session:
        # User is logged in, perform logout
        flash("You've been logged out", "info")
        session.pop("user")
    else:
        # No user session found
        flash("You were not logged in.", "warning")
    return redirect(url_for("log_in"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Display user profile and associated reviews.
    """
    current_username = session.get("user")
    try:
        page = request.args.get("page", 1, type=int)
        per_page = 5
        start_index = (page - 1) * per_page
        user_reviews = mongo.db.game_reviews.find(
            {"username": username}
        ).skip(start_index).limit(per_page)

        total_reviews = mongo.db.game_reviews.count_documents(
            {"username": username}
        )
        total_pages = math.ceil(total_reviews / per_page)
        return render_template("profile.html",
                               username=username,
                               current_username=current_username,
                               user_reviews=user_reviews,
                               per_page=per_page,
                               total_reviews=total_reviews,
                               total_pages=total_pages,
                               page=page)
    except PyMongoError:
        flash("A database error occurred while fetching profile data. Please try again later.", "danger")
        return redirect(url_for("home"))
    except Exception:
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(url_for("home"))


def find_game_reviews(page, per_page):
    """
    Finds game reviews from database.
     """
    try:
        start_index = (page - 1) * per_page
        total_reviews = mongo.db.game_reviews.count_documents({})
        total_pages = math.ceil(total_reviews / per_page)
        games = mongo.db.game_reviews.find().skip(start_index).limit(per_page)
        return games, total_reviews, total_pages
    except PyMongoError as pymongo_err:
        # Raise RuntimeError for database errors
        raise RuntimeError(f"Database error occurred: {pymongo_err}") from pymongo_err
    except Exception as err:
        # Raise RuntimeError for unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {err}") from err


@app.route("/get_game_reviews")
def get_game_reviews():
    """
    Render game reviews from the database.
    """
    page = request.args.get("page", 1, type=int)
    per_page = 5
    try:
        games, total_reviews, total_pages = find_game_reviews(page, per_page)
    except RuntimeError as e:
        flash(str(e), "danger")
        return redirect(url_for("home"))
    return render_template("game_reviews.html",
                           games=games,
                           per_page=per_page,
                           total_reviews=total_reviews,
                           total_pages=total_pages,
                           page=page)


@app.route("/search_game")
def search_game():
    """
    Render the search game page.
    """
    # Check if user is logged in to access page.
    if 'user' not in session:
        flash("You need to be logged in to access the search page.", "warning")
        return redirect(url_for("log_in"))
    return render_template("search_game.html")


def handle_search_results(query, page, per_page):
    """
    Handle search results fetched from the RAWG API.
    """
    url = f"{RAWG_API_URL}?key={RAWG_API_KEY}&search={query}&page_size={per_page}&page={page}"
    try:
        data = fetch_api_data(url)
        games = data.get("results", [])
        total_results = data.get("count", 0)
        total_pages = math.ceil(total_results / per_page)
        return games, total_results, total_pages
    except RuntimeError as err:
        raise RuntimeError(f"Failed to handle search results: {err}") from err


@app.route("/search_results", methods=["GET", "POST"])
def search_results():
    """
    Display search results from the RAWG API.
    """
    if 'user' not in session:
        flash("You need to be logged in to view this page.", "warning")
        return redirect(url_for("log_in"))
    if request.method == "POST":
        query = request.form.get("query")
    else:
        query = request.args.get("query")
    page = request.args.get("page", 1, type=int)
    per_page = 5
    try:
        games, total_results, total_pages = handle_search_results(query, page, per_page)
        if not games:
            flash("No games found.", "info")
            return redirect(url_for("search_game"))
    except RuntimeError as err:
        flash(str(err), "danger")
        return redirect(url_for("search_game"))
    except Exception:
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(url_for("search_game"))
    return render_template("search_results.html",
                           games=games,
                           total_results=total_results,
                           per_page=per_page,
                           page=page,
                           query=query,
                           total_pages=total_pages)


@app.route("/game_info")
def game_info():
    """
    Fetch detailed information about a specific game.
    """
    # Check if user is logged in to access the page
    if 'user' not in session:
        flash("You need to be logged in to access game details.", "warning")
    game = request.args.get("game")
    if not game:
        flash("No game specified.", "warning")
        return redirect(url_for("search_game"))
    try:
        game_dict = eval(game)
        url = f"{RAWG_API_URL}/{game_dict['id']}?key={RAWG_API_KEY}"
        game_data = fetch_api_data(url)
        relevant_tags = [
            tag['name'] for tag in game_data.get('tags', [])
            if 'singleplayer' in tag['slug'] or 'multiplayer' in tag['slug'] or 'co-op' in tag['slug']
        ]
        return render_template("game_info.html", game_data=game_data, relevant_tags=relevant_tags)
    except RuntimeError as err:
        flash(str(err), "danger")
        return redirect(url_for("search_game"))
    except Exception:
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(url_for("search_game"))


@app.route("/add_game", methods=["POST"])
def add_game():
    """
    Add a game review
    """
    if request.method == "POST":
        username = session.get("user")
        game_id = request.form.get("game_id")
        # Check if the user has already reviewed the game
        existing_review = mongo.db.game_reviews.find_one(
            {"username": username, "game_id": game_id}
        )
        if existing_review:
            flash("You have already reviewed this game.", "warning")
            return redirect(url_for("profile", username=username))
        # If user hasn't reviewed the game, proceed with adding the review
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
        flash("Game added successfully!", "success")
        return redirect(url_for("search_game"))
    else:
        return "Method not allowed"


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Edit a game review
    """
    existing_review = mongo.db.game_reviews.find_one(
        {"_id": ObjectId(review_id)}
    )
    if request.method == "POST":
        if "user" not in session or \
                session["user"] != existing_review["username"]:
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
        flash("Game review updated successfully!", "success")
        return redirect(url_for("profile", username=session.get("user")))
    else:
        if existing_review:
            game_id = existing_review["game_id"]
            url = f"{RAWG_API_URL}/{game_id}?key={RAWG_API_KEY}"
            game_data = fetch_api_data(url)
            return render_template("profile.html", review=existing_review,
                                       game_data=game_data)
        else:
            flash("Review not found", "warning")
            return redirect(url_for("profile", username=session.get("user")))


@app.route("/delete_review/<review_id>", methods=["POST"])
def delete_review(review_id):
    """
    Delete a game review
    """
    review = mongo.db.game_reviews.find_one({"_id": ObjectId(review_id)})
    if not review:
        flash("Review not found", "warning")
        return redirect(url_for("profile", username=session.get("user")))
    if "user" not in session or session["user"] != review["username"]:
        abort(403)
    mongo.db.game_reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review deleted successfully", "success")
    return redirect(url_for("profile", username=session.get("user")))


@app.route("/delete_account", methods=["POST"])
def delete_account():
    """
    Delete user account and associated reviews
    """
    if "user" in session:
        mongo.db.users.delete_one({"username": session["user"]})
        mongo.db.game_reviews.delete_many({"username": session["user"]})
        session.pop("user")
        flash("Your account and associated reviews have been deleted "
              "successfully.", "success")
        return redirect(url_for("sign_up"))
    else:
        flash("You must be logged in to delete your account.", "warning")
        return redirect(url_for("log_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

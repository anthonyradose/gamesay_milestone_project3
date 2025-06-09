from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash
from pymongo.errors import PyMongoError

# Create the blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/sign_up", methods=["GET", "POST"])
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
            existing_email = auth_bp.mongo.db.users.find_one({"email": email})
            existing_user = auth_bp.mongo.db.users.find_one({"username": username})
            if existing_user:
                flash("User already exists.", 'warning')
                return redirect(url_for("auth.sign_up"))
            if existing_email:
                flash("Email already exists.", 'warning')
                return redirect(url_for("auth.sign_up"))
            # Create a new user document
            new_user = {
                "email": email,
                "username": username,
                "password": generate_password_hash(password)
            }
            auth_bp.mongo.db.users.insert_one(new_user)
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

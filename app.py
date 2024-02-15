import os

from cs50 import SQL
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    jsonify,
)
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from datetime import date, time, datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///diary.db")


# login required function, inspired from CS50 finance
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


# Profile to show diary
@app.route("/")
@login_required
def profile():
    # Write a table of date and time and duration of symptoms:
    user_id = session["user_id"]

    symptoms = db.execute(
        "SELECT * FROM symptoms WHERE user_id = ? ORDER BY date DESC", user_id
    )

    username_db = db.execute("SELECT username from users where id = ?", user_id)
    username = username_db[0]["username"]

    return render_template(
        "profile.html", symptoms=symptoms, user_id=user_id, username=username
    )


# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    #  User reached route via POST (as by submitting a form via POST)
    else:
        # access user input
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")

        if not username:
            error_message = "Please input a username, 403"
            return render_template("registrationfail.html", error_message=error_message)

        # Ensures user inputs an appopriate lenght of username
        if len(username) > 17:
            error_message = (
                "Username too long, username must be maximum 17 characters, 403"
            )
            return render_template("registrationfail.html", error_message=error_message)

        if not password:
            error_message = "Please input a password"
            return render_template("registrationfail.html", error_message=error_message)

        if not confirm_password:
            error_message = "Please confirm password"
            return render_template("registrationfail.html", error_message=error_message)

        if password != confirm_password:
            error_message = "Password and confirmation does not match"
            return render_template("registrationfail.html", error_message=error_message)

        # hash password to database
        hash_password = generate_password_hash(password)

        try:
            # inserting into database
            new_user = db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                hash_password,
            )
        except:
            error_message = "Username already exists"
            return render_template("registrationfail.html", error_message=error_message)

        session["user_id"] = new_user

        return redirect("/")


# Log out route, inspired from CS50 finance
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/index")


# Log in route, inspired from CS50 Finance
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            error_message = "Username Invalid"
            return render_template("loginfail.html", error_message=error_message)

        # Ensure password was submitted
        elif not request.form.get("password"):
            error_message = "Password Invalid"
            return render_template("loginfail.html", error_message=error_message)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            error_message = "Invalid username/ Invalid password"
            return render_template("loginfail.html", error_message=error_message)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


# write function
@app.route("/write", methods=["GET", "POST"])
@login_required
def write():
    # if request method == get to get wrote.html
    if request.method == "GET":
        return render_template("write.html")
    # if request method == post
    else:
        date = request.form.get("date")
        date_ended = request.form.get("date-ended")
        time_onset = request.form.get("time-onset")
        time_ended = request.form.get("time-ended")
        symptoms = request.form.get("symptoms")

        user_id = session["user_id"]

        if not date:
            error_message = "Please input the date the symptoms started"
            return render_template("write.html", error_message=error_message)

        if not date_ended:
            error_message = "Please input the date the symptoms ended"
            return render_template("write.html", error_message=error_message)

        if not time_onset:
            error_message = "Please input time the symptom started"
            return render_template("write.html", error_message=error_message)
        if not time_ended:
            error_message = "Please input time the symptom ended"
            return render_template("write.html", error_message=error_message)

        if not symptoms:
            error_message = "Please input symptoms"
            return render_template("write.html", error_message=error_message)

        # Inserts data input into diary.db
        db.execute(
            "INSERT INTO symptoms (user_id, date, time_onset, time_ended, symptoms, date_ended) VALUES (?, ?, ?, ?, ?, ?)",
            user_id,
            date,
            time_onset,
            time_ended,
            symptoms,
            date_ended,
        )

        flash("Symptom Written!")

        return redirect("/")


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "GET":
        return render_template("change_password.html")
    else:
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirmation")

        if not current_password:
            error_message = "Please input password, 403"
            return render_template("change_password.html", error_message=error_message)

        if not new_password:
            error_message = "Please input new password!, 403"
            return render_template("change_password.html", error_message=error_message)

        if not confirm_password:
            error_message = "Please confirm new password!, 403"
            return render_template("change_password.html", error_message=error_message)

        # find hash of password from database
        user_id = session["user_id"]

        password_hash = db.execute("SELECT hash FROM users WHERE id = ?", user_id)

        if len(password_hash) != 1 or not check_password_hash(
            password_hash[0]["hash"], current_password
        ):
            error_message = "Incorrect current password, 403"
            return render_template("change_password.html", error_message=error_message)

        # if new_password and confirmation password not the same return apology
        if new_password != confirm_password:
            error_message = "New password and confirmation password must match, 403"
            return render_template("change_password.html", error_message=error_message)

        # Generate new password hash and update database
        new_hash_password = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash_password, user_id)

        # show flash for user feedback
        flash("Password Changed Succesfully!")

        return redirect("/change_password")

from flask import Flask, render_template, request, url_for, redirect, \
    session
from dbconnect import connection
from passlib.hash import sha256_crypt
from pymysql import escape_string as thwart
import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    now = datetime.datetime.now()
    return render_template("/home.html", message="Home page", now=now)


@app.route("/search")
def search():
    return render_template("/search.html")


@app.route("/about")
def about():
    return render_template("/about.html", message="About page")

@app.route("/categories")
def categories():
    return render_template("/categories.html", message="Categories")



@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == "POST":
        attempted_username = request.form['username']
        attempted_password = request.form['password']

        if attempted_username == "admin" and attempted_password == "password":
            return redirect(url_for('search'))
        else:
            error = "Invalid credentials, try again..."

    return render_template("/login.html", error=error)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    error = ""
    if request.method == "POST":
        username = request.form['username']
        if username != "":
            return render_template('search.html', username=username)

    return render_template('/register.html', error=error)


if __name__ == "__main__":
 
    app.run(debug=True)
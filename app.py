from flask import Flask, render_template, request, url_for, redirect, flash, \
    session
from dbconnect import *
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
        name = request.form['username']
        psswd = request.form['password']
        hashed = sha256_crypt.encrypt(str(psswd))

        if attempted_username == "admin" and attempted_password == "password":
            return redirect(url_for('search'))
        else:
            error = "Invalid credentials, try again..."

    return render_template("/login.html", error=error)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    conn = requestConnection()
    c = requestCursor(conn)
    error = ""
    if request.method == "POST":
        username = request.form['username']
        psswd = request.form['password']
        confirm = request.form['confirm']

        if psswd == confirm:
            hashed = sha256_crypt.encrypt(str(psswd))
            
            sql = 'INSERT INTO users (login, password) VALUES (%s,%s)'
            val = (f'{username}', f'{hashed}')
            c.execute(sql, val)
            conn.commit()
            conn.close()

            return render_template('search.html', username=username)

    return render_template('/register.html', error=error)


if __name__ == "__main__":
 
    app.run(debug=True)
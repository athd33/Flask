from flask import Flask, render_template, request, url_for, redirect
from dbconnect import connection

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("/home.html", message="Home page")

@app.route("/search")
def search():
     return render_template("/search.html")

@app.route("/about")
def about():
     return render_template("/about.html", message="About page")

@app.route("/login", methods=['GET','POST'])
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


@app.route("/register", methods=['GET','POST'])
def register_page():
     try:
          c, conn = connection()
          return "ok"
     except Exception as e:
          return(str(e))






if __name__ == "__main__":
     app.run( debug=True)
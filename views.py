from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/search')
def search():
    return render_template('pages/search.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)  # debug permet de rafraichir sans relancer l'app
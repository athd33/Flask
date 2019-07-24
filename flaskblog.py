from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": 'Corey TOTO',
        "title": "Blog post 1",
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
    {
        "author": 'John TITI',
        "title": "Blog post 2",
        'content': 'Second post content',
        'date_posted': 'April 24, 2019'
    }
]




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # debug permet de rafraichir sans relancer l'app
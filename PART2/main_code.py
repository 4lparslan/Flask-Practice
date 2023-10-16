# PART2 home.html, about.html and layout.html
from flask import Flask, render_template, url_for

app = Flask(__name__)

# dummy data (like fetched from database)
posts = [
    {
        'author': 'Jhonny Bravo',
        'title': 'Romanticism',
        'content': 'Content 1',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Idealism',
        'content': 'Content 2',
        'date_posted': 'June 12, 2020'
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)
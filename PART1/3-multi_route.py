from flask import Flask

app = Flask(__name__)

@app.route("/home")     # both routers can work at the same time with same function.
@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)

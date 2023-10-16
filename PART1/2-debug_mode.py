from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

    # By adding 'debug=True' parameter, we can do real-time changes in our page. No need to restart the web server.

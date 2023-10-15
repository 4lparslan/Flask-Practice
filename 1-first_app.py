from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run()

    # '__name__ == '__main__'' condition allows us to run the script directly from terminal. It won't return True for importing the script as a module.
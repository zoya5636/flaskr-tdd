from flask import Flask


# configuration
DATABASE = "flaskr.db"

# create and initialize a new Flask app
app = Flask(__name__)

# load the config
app.config.from_object(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
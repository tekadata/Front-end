#  index_route
# Your mission

# Create a route named /
# that returns the message "Hello Santa!\n"

# $> curl "http://127.0.0.1:5000/"
# Hello Santa!
# $>

from flask import Flask

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/")
def index():
    return "Hello Santa!\n"


app.run(debug=True)

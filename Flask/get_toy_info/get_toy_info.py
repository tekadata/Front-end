#  get_toy_info
# Your mission

# Create a route that returns the information for a given toy.

# You will use a URL parameter to specify the toy,
# so your route will be of the form /toys/xxx.

# The route will return the message "I am the toy xxx\n".


# $> curl "http://127.0.0.1:5000/toys/actionman"
# I am the toy actionman
# $> curl "http://127.0.0.1:5000/toys/doll"
# I am the toy doll
# $> curl "http://127.0.0.1:5000/toys/whatever"
# I am the toy whatever
# $>

from flask import Flask

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys/<toy_id>")
def index(toy_id):
    return "I am the toy " + toy_id + "\n"


app.run(debug=True)

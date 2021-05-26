#  get_toy_owner
# Your mission

# Create a route that returns the owner of a given toy.

# The route will be of the form /toys/xxx/owner.
# The route will return the message "I don't know who my owner is\n".

# And, again, if the parameter is the string "unknown",
# the route will return a 404 error.


# $> curl "http://127.0.0.1:5000/toys/actionman/owner"
# I don't know who my owner is
# $> curl "http://127.0.0.1:5000/toys/unknown/owner"
# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
# <title>404 Not Found</title>
# <h1>Not Found</h1>
# <p>The requested URL was not found on the server.
# If you entered the URL manually please check your spelling and try again.</p>
# $> curl "http://127.0.0.1:5000/toys/doll/owner"
# I don't know who my owner is
# $>

from flask import Flask, abort

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys/<toy_id>/owner")
def index_2(toy_id):
    if toy_id == "unknown":
        abort(404)
    else:
        return "I don't know who my owner is\n"


app.run(debug=True)

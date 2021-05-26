#  delete_owner
# Your mission

# We saw GET, that you'd use whenever you aim to
# request information from the server.
# We saw POST, that you'd use to
# add (or modify) information to the server.

# Let's see the verb DELETE,
# that is typically used to delete information from the server.

# Create a route named /toys/xxx/owner in DELETE that
# returns the message "I deleted the owner!\n"

# The Sentinel will also test the GET and POST routes,
# so be sure to put them in your Python file as well.

# HTTP methods

# The method is the type of action you want the request to perform
# and is sent from the client to the server on every request.

# There are several HTTP methods
# but we're only going to cover 5 in this article:

#     GET - Used to fetch the specified resource
#     POST - Used to create new data at the specified resource
#     PUT - Used to create new data or
#           replace existing data at the specified resource
#     PATCH - Used to create new data or
#             update/modify existing data at the specified resource
#     DELETE - Used to delele existing data at the specified resource

# Requesting a URL is an example of a GET request,
# where your browser makes a request for resources
# at a specified location (the URL) and the server returns some HTML.
# GET requests are "safe" as they aren't able to modify state
# or data on the server.

# An example use case of a POST request
# would be creating a new account on a website
# or application, whereby the resource doesn't already exist.


# $> curl -X DELETE "http://127.0.0.1:5000/toys/spiderman/owner"
# I deleted the owner!
# $> curl "http://127.0.0.1:5000/toys/spiderman/owner"
# I don't know who my owner is
# $>

from flask import Flask, request, abort

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys/<toy_id>/owner", methods=["GET", "POST", "DELETE"])
def post_new_owner(toy_id):
    if toy_id == "unknown":
        abort(404)
    elif request.method == "POST":
        return "I added a new owner!\n"
    elif request.method == "DELETE":
        return "I deleted the owner!\n"
    else:
        return "I don't know who my owner is\n"


app.run(debug=True)

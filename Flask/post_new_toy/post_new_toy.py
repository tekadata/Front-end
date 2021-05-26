#  post_new_toy
# Your mission

# All your routes so far implemented the GET verb implicitly.
# Let's try to implement other HTTP verbs!

# Create a route named /toys in POST that returns
# the message "I have added a new toy!\n"

# Of course, the route /toys in GET must still return
# the message "Get all the toys\n"

# ! Read more about how to play with HTTP methods here.
# Flask supports the common HTTP methods, including GET, POST,
# PUT, PATCH, DELETE and working with them is extremely simple,
# allowing us to build URL's and endpoints
# which only listen for certain HTTP methods.

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


# $> curl -X POST "http://127.0.0.1:5000/toys"
# I have added a new toy!
# $> curl "http://127.0.0.1:5000/toys"
# Get all the toys
# $>

from flask import Flask, request

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys", methods=["GET", "POST"])
def post_new_toy():
    if request.method == "POST":
        return "I have added a new toy!\n"
    elif request.method == "GET":
        return "Get all the toys\n"


@app.route("/toys/unknown", methods=["GET", "POST"])
def post_new_toy_3():
    return 404


app.run(debug=True)

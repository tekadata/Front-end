# get_query_data
# Your mission

# Right, so just now we implemented GET and POST routes
# without caring about data. We simply requested a URL.

# But we can actually join data to our request
# That's what happens when you fill a form on a website:
# when you hit "enter", a request is sent to the server
# with what you put in the form.

# Let's pretend the information was sent from
# a regular form (which uses GET by default),
# and let's see how we can get it from the server.

# Modify the /toys route in GET, so that:

#     if no query parameters are present,
#        it still returns "Get all the toys\n"
#     if there are some query parameters,
#        it returns them

# Read more about query parameters here.


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


# $> curl "http://127.0.0.1:5000/toys?owner=mathieu"
# {"owner":"mathieu"}
# $> curl "http://127.0.0.1:5000/toys?category=water&owner=laurie"
# {"category":"water","owner":"laurie"}
# $> curl "http://127.0.0.1:5000/toys"
# Get all the toys
# $>

from flask import Flask, request, abort

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys", methods=["GET", "POST", "DELETE"])
def get_query_data():
    if request.args:
        my_query = ",".join(f" {k} : {v} " for k, v in request.args.items())
        my_query = "{" + my_query.replace(' ', '"') + "}\n"
        return my_query
    else:
        return "Get all the toys\n"


app.run(debug=True)

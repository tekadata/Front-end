#  return_post_data
# Your mission

# Now, you just saw how to retrieve query parameters that
# are sent with a GET request.

# You can also send data with a POST request.
# This time the data won't be apparent in the URL,
# but it will be encrypted in the body of the request.
# It allows you to hide sensitive information (like a password).

# Modify the /toys/xxx/owner route in POST, so that:

#     if there's no POST data, it still returns "I added a new owner!\n"
#     if there is POST data, it returns that data

# You can simulate POST data with curl by using
# the -d option to specify the data.


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


# $> curl -d "name=Sentinel&email=hope_wrecker@gmail.com" -X
# POST "http://127.0.0.1:5000/toys/spiderman/owner"
# {"email":"hope_wrecker@gmail.com","name":"Sentinel"}
# $> curl -X POST "http://127.0.0.1:5000/toys/spiderman/owner"
# I added a new owner!
# $>

from flask import Flask, request, abort

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys/<toy_id>/owner", methods=["GET", "POST"])
def post_new_owner(toy_id):
    posted_data = ''
    if toy_id == "unknown":
        abort(404)
    elif request.method == "POST":
        if request.form:
            posted_data = ",".join(f" {k} : {v} \
" for k, v in request.form.items())
            posted_data = "{" + posted_data.replace(' ', '"') + "}\n"
            return posted_data
        else:
            return "I added a new owner!\n"


app.run(debug=True)

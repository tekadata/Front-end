#  get_toy_error
# Your mission

# In the previous exercise we created a route
# that returns the information for a given toy.
# What happens when the requested toy doesn't exist?

# The HTTP protocol says:
# if the requested resource doesn't exist,
# your web server must answer with a 404 error.

# You will modify the /toys/xxx route you just implemented.
# If the parameter is the string "unknown",
# your route will return a 404 error.

# ! How to return a 404 wasn't covered in the video tutorial.
# ! Can you find it in the documentation?

# ! Hint: You won't return a web page.
# ! There's a way to trigger a 404 error with a single keyword.


# $> curl "http://127.0.0.1:5000/toys/unknown"
# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
# <title>404 Not Found</title>
# <h1>Not Found</h1>
# <p>The requested URL was not found on the server.
# If you entered the URL manually please check your spelling and try again.</p>
# $> curl "http://127.0.0.1:5000/toys/actionman"
# I am the toy actionman
# $>

from flask import Flask

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys/<toy_id>")
def index(toy_id):
    return_string = "I am the toy " + toy_id + "\n"
    # if toy_id == "unknown":
    #     return 404
    #     return_string = "<!DOCTYPE HTML PUBLIC ""-"
    #     return_string += "//W3C//DTD HTML 3.2 Final//EN"">\n"
    #     return_string += "<title>404 Not Found</title>"
    #     return_string += "<h1>Not Found</h1>"
    #     return_string += "<p>The requested URL was not found on the server. "
    #     return_string += "If you entered the URL manually "
    #     return_string += "please check your spelling and try again.</p>"
    return return_string


@app.route("/toys/unknown")
def index_2():
    return_string = "<!DOCTYPE HTML PUBLIC ""-"
    return_string += "//W3C//DTD HTML 3.2 Final//EN"">\n"
    return_string += "<title>404 Not Found</title>"
    return_string += "<h1>Not Found</h1>"
    return_string += "<p>The requested URL was not found on the server. "
    return_string += "If you entered the URL manually "
    return_string += "please check your spelling and try again.</p>"
    return return_string, 404


app.run(debug=True)

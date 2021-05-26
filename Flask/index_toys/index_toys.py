#  index_toys
# Your mission

# Create a route named /toys
# that returns the message "Get all the toys\n"

# $> curl "http://127.0.0.1:5000/toys"
# Get all the toys
# $>

from flask import Flask

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/toys")
def index():
    return "Get all the toys\n"


app.run(debug=True)

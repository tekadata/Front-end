from flask import Flask, request

app = Flask(__name__)

# Flask decorator above a function:
# -> basic route


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "Data saved"
    else:
        return "Hello, World!"


@app.route("/products/<product_id>")
def show_product(product_id):
    return product_id


app.run(debug=True)

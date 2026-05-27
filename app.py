from flask import Flask, render_template, request
from services.api import search_products, get_product

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    query = request.args.get("query", "")
    products = search_products(query) if query else []
    return render_template("partials/results.html", products=products)

@app.route("/product/<barcode>")
def product(barcode):
    product = get_product(barcode)
    return render_template("product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from services.api import search_products, get_product
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("foodsearch.html")

@app.route("/search")
def search():
    query = request.args.get("query", "")
    products = search_products(query) if query else []
    return jsonify(products)

@app.route("/product/<barcode>")
def product(barcode):
    prod = get_product(barcode)
    return jsonify(prod)

if __name__ == "__main__":
    app.run(debug=True)
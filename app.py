from flask import Flask, render_template, request, jsonify, send_from_directory
from services.api import search_products, get_product

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("templates", "foodfinder.html")

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
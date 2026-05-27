from flask import Flask, render_template, request, jsonify
from services.api import search_products, get_product
from services.vision import identify_food_from_image
from dotenv import load_dotenv

load_dotenv()

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
    prod = get_product(barcode)

    grade_colors = {
        'a': 'bg-green-500',
        'b': 'bg-lime-400',
        'c': 'bg-yellow-400',
        'd': 'bg-orange-400',
        'e': 'bg-red-500'
    }

    nutrients = [
        ('Energia', 'energy-kcal_100g', 'kcal'),
        ('Carboidratos', 'carbohydrates_100g', 'g'),
        ('Acucares', 'sugars_100g', 'g'),
        ('Gorduras totais', 'fat_100g', 'g'),
        ('Gorduras saturadas', 'saturated-fat_100g', 'g'),
        ('Fibras', 'fiber_100g', 'g'),
        ('Proteinas', 'proteins_100g', 'g'),
        ('Sal', 'salt_100g', 'g'),
        ('Sodio', 'sodium_100g', 'g')
    ]

    return render_template("product.html",
        product=prod,
        grade_colors=grade_colors,
        grades=['a', 'b', 'c', 'd', 'e'],
        nutrients=nutrients
    )

if __name__ == "__main__":
    app.run(debug=True)
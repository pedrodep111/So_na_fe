import requests # Biblioteca para fazer chamadas HTTP

BASE_URL = "https://world.openfoodfacts.org" # Endereço da API, armazenado numa variável para não precisar repetir

HEADERS = {
    "User-Agent": "FoodFinder/1.0 (contato@exemplo.com)"
}

# Query = texto que o usuário digitou
def search_products(query):
    try:
        response = requests.get(f"{BASE_URL}/cgi/search.pl", headers=HEADERS, params={
            "search_terms": query,
            "json": 1,
            "page_size": 20,
            "fields": "code,product_name,brands,image_url,nutriscore_grade"
        })
        data = response.json()
        return data.get("products", [])
    except Exception as e:
        print(f"Erro na busca: {e}")
        return []

def get_product(barcode):
    try:
        response = requests.get(f"{BASE_URL}/api/v0/product/{barcode}.json", headers=HEADERS)
        data = response.json()
        return data.get("product", {})
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
        return {}
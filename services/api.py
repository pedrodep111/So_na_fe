import requests # Biblioteca para fazer chamadas HTTP

BASE_URL = "https://world.openfoodfacts.org" # Endereço da API, armazenado numa variável para não precisar repetir

HEADERS = {
    "User-Agent": "FoodFinder/1.0 (contato@exemplo.com)"
}

# Query = texto que o usuário digitou
def search_products(query):
    try:
        # Adiciona um timeout para evitar que a requisição fique pendente por muito tempo
        response = requests.get(
            f"{BASE_URL}/cgi/search.pl",
            headers=HEADERS,
            params={
                "search_terms": query,
                "json": 1,
                "page_size": 20,
                "fields": "code,product_name,brands,image_url,nutriscore_grade",
            },
            timeout=5,
        )

        # Verifica status HTTP antes de tentar decodificar JSON
        if response.status_code != 200:
            print(f"Erro na busca: status {response.status_code}")
            # Imprime uma amostra do corpo para ajudar no debug
            print(f"Resposta: {response.text[:200]}")
            return []

        try:
            data = response.json()
        except ValueError as e:
            # JSON inválido (por exemplo corpo vazio ou HTML de erro)
            print(f"Erro ao decodificar JSON na busca: {e}")
            print(f"Resposta (texto): {response.text[:200]}")
            return []

        return data.get("products", [])
    except requests.exceptions.RequestException as e:
        # Erros de conexão, timeout, DNS, etc.
        print(f"Erro na busca (request): {e}")
        return []

def get_product(barcode):
    try:
        response = requests.get(f"{BASE_URL}/api/v0/product/{barcode}.json", headers=HEADERS, timeout=5)

        if response.status_code != 200:
            print(f"Erro ao buscar produto: status {response.status_code}")
            print(f"Resposta: {response.text[:200]}")
            return {}

        try:
            data = response.json()
        except ValueError as e:
            print(f"Erro ao decodificar JSON do produto: {e}")
            print(f"Resposta (texto): {response.text[:200]}")
            return {}

        return data.get("product", {})
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar produto (request): {e}")
        return {}
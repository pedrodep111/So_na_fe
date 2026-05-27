import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def identify_food_from_image(image_bytes, mime_type):
    model = genai.GenerativeModel("gemini-2.0-flash")

    image_part = {
        "mime_type": mime_type,
        "data": image_bytes
    }

    prompt = """Olhe para esta imagem e identifique o alimento ou produto alimentício.
    Responda APENAS com o nome do produto em português, sem explicações.
    Exemplo: 'coca cola', 'whey protein chocolate', 'arroz integral'
    Se não conseguir identificar um alimento, responda apenas: 'não identificado'"""

    response = model.generate_content([prompt, image_part])
    return response.text.strip()
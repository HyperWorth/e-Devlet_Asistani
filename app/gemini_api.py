import os
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_request(user_input: str):
    prompt = f"""
Sen bir vatandaş hizmetleri asistanısın. Aşağıdaki vatandaşın başvuru isteğini analiz et.

Vatandaşın ifadesi: "{user_input}"

Cevabını aşağıdaki başlıklara göre sade, net ve resmi bir dille maddeler halinde yaz:

1. Başvuru konusu nedir?
2. Gerekli belgeler nelerdir?
3. Hangi kuruma yapılır?
4. Başvuru nasıl yapılır? (Adım adım)
5. Ek uyarılar veya dikkat edilmesi gerekenler varsa belirt.

Sadece Türkçe cevap ver. Listeleme yap. Cümleleri kısa ve açık tut.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

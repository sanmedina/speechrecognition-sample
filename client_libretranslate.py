import requests


def detect_language(text: str):
    response = requests.post(
        "http://localhost:5000/detect",
        json={
            "q": text,
            "api_key": ""
        }
    )
    result = response.json()
    return result[0]["language"]


def select_to_translate(language: str):
    return "en" if language == "es" else "es"


def translate(text: str, source_language: str, target_language: str):
    response = requests.post(
        "http://localhost:5000/translate",
        json={
            "q": text,
            "source": source_language,
            "target": target_language,
            "format": "text",
            "api_key": ""
        }
    )
    result = response.json()
    return result["translatedText"]

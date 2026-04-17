import requests
from config import API_KEY, BASE_URL, UNITS, LANG


def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNITS}&lang={LANG}"

        response = requests.get(url, timeout=5)
        data = response.json()

        # ❌ erreur API (ville inconnue, etc.)
        if response.status_code != 200:
            return {
                "error": data.get("message", "Erreur inconnue")
            }

        # ✔ données propres
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "wind": data["wind"]["speed"],
            "humidity": data["main"]["humidity"]
        }

        return weather

    except requests.exceptions.RequestException:
        return {"error": "Problème de connexion internet"}

    except Exception as e:
        return {"error": str(e)}
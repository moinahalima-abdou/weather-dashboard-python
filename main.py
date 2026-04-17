from services.weather_api import get_weather
from models.weather import Weather
from utils.history import History


def main():
    history = History()

    while True:
        city = input("\n🌍 Entrer une ville (ou 'exit'): ")

        if city.lower() == "exit":
            break

        data = get_weather(city)

        if "error" in data:
            print("❌ Erreur:", data["error"])
            continue

        weather = Weather(
            city=data["city"],
            temp=data["temp"],
            description=data["description"],
            wind=data["wind"],
            humidity=data["humidity"]
        )

        print("\n" + str(weather))

        history.add_city(city)


if __name__ == "__main__":
    main()
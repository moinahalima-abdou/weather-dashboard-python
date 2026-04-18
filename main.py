from services.weather_api import get_weather
from models.weather import Weather
from utils.history import History


def show_menu():
    print("\n===== WEATHER APP =====")
    print("1. Rechercher une ville")
    print("2. Voir l'historique")
    print("3. Quitter")


def main():
    history = History()

    while True:
        show_menu()
        choice = input("Choisis une option : ")

        if choice == "1":
            city = input("🌍 Entrer une ville : ")

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

        elif choice == "2":
            history.show_history()

        elif choice == "3":
            print("Au revoir 👋")
            break

        else:
            print("Option invalide")


if __name__ == "__main__":
    main()
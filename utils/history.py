import json
from datetime import datetime


class History:
    def __init__(self, filename="data/history.json"):
        self.filename = filename

    def add_city(self, city):
        history = self.load_history()

        entry = {
            "city": city,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        history.append(entry)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)

    def load_history(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def show_history(self):
        history = self.load_history()

        if not history:
            print("📭 Aucun historique.")
            return

        print("\n📜 Historique des recherches :")
        for i, item in enumerate(history, 1):
            print(f"{i}. {item['city']} ({item['date']})")
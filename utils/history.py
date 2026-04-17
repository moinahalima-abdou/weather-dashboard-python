import json


class History:
    def __init__(self, filename="data/history.json"):
        self.filename = filename

    def add_city(self, city):
        history = self.load_history()

        history.append(city)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)

    def load_history(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
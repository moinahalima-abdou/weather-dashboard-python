class Weather:
    def __init__(self, city, temp, description, wind, humidity):
        self.city = city
        self.temp = temp
        self.description = description
        self.wind = wind
        self.humidity = humidity

    def __str__(self):
        return (
            f"📍 Ville: {self.city}\n"
            f"🌡️ Température: {self.temp}°C\n"
            f"☁️ Description: {self.description}\n"
            f"💨 Vent: {self.wind} m/s\n"
            f"💧 Humidité: {self.humidity}%"
        )
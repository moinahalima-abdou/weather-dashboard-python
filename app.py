import streamlit as st
from services.weather_api import get_weather
from utils.history import History

history = History()

st.title("🌦️ Weather App")

city = st.text_input("Entrer une ville")

if st.button("Rechercher"):
    data = get_weather(city)

    if "error" in data:
        st.error(data["error"])
    else:
        st.success(f"Météo à {data['city']}")
        st.write(f"🌡️ Température : {data['temp']}°C")
        st.write(f"☁️ Description : {data['description']}")
        st.write(f"💨 Vent : {data['wind']} m/s")
        st.write(f"💧 Humidité : {data['humidity']}%")

        history.add_city(city)

# affichage historique
if st.checkbox("Voir l'historique"):
    hist = history.load_history()

    if not hist:
        st.info("Aucun historique")
    else:
        for item in hist:
            st.write(f"{item['city']} - {item['date']}")
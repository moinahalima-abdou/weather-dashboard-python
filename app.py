
import matplotlib.pyplot as plt
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

       
        # 📊 AFFICHAGE DONNÉES
        
        st.write(f"🌡️ Température : {data['temp']}°C")
        st.write(f"☁️ Description : {data['description']}")
        st.write(f"💨 Vent : {data['wind']} m/s")
        st.write(f"💧 Humidité : {data['humidity']}%")

       
        # 💾 HISTORIQUE
        
        history.add_city(city)

        
        # 📊 GRAPHIQUES
       
        labels = ["Température", "Humidité", "Vent"]
        values = [data["temp"], data["humidity"], data["wind"]]

        st.subheader("📊 Graphiques météo")

        # --- BAR CHART ---
        st.write("📊 Graphique en barres")
        fig1, ax1 = plt.subplots()
        ax1.bar(labels, values)
        ax1.set_title(f"Météo de {data['city']}")
        st.pyplot(fig1)

        # --- LINE CHART ---
        st.write("📈 Graphique en courbe (bonus)")
        fig2, ax2 = plt.subplots()
        ax2.plot(labels, values, marker="o")
        ax2.set_title(f"Tendance météo de {data['city']}")
        st.pyplot(fig2)


# 📜 HISTORIQUE

st.subheader("📜 Historique")

if st.checkbox("Voir l'historique"):
    hist = history.load_history()

    if not hist:
        st.info("Aucun historique")
    else:
        for item in hist:
            st.write(f"{item['city']} - {item['date']}")
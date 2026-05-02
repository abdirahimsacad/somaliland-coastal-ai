import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import random

# 1. Habaynta Bogga
st.set_page_config(page_title="AI Ilaalinta Xeebaha Somaliland", layout="wide")
st.title("🌊 Agentic AI: Ilaalinta iyo La socodka Xeebaha")

# 2. Xogta Goobaha (Coordinates)
locations = {
    "Berbera": {"lat": 10.4396, "lon": 45.0119},
    "Saylac": {"lat": 11.3533, "43.4683": 43.4683},
    "Maydh": {"lat": 11.0000, "lon": 47.1167},
    "Lughaya": {"lat": 10.6833, "lon": 43.9333},
}

# 3. AI Logic (Simulated)
def get_coastal_status():
    status_data = []
    for name, coords in locations.items():
        # AI-gu wuxuu halkan ku falanqaynayaa khatarta
        wind = random.randint(10, 50)
        risk_level = "Green"
        if wind > 35: risk_level = "Red"
        elif wind > 25: risk_level = "Orange"
        
        status_data.append({
            "City": name,
            "Lat": coords['lat'],
            "Lon": coords.get('lon', 43.4683), # fix for Saylac dict key
            "Wind": wind,
            "Risk": risk_level
        })
    return status_data

data = get_coastal_status()

# 4. Abuurista Khariidadda (Google Maps Style)
st.subheader("Khariidadda Khatarta Waqtiga-Dhabta ah")
m = folium.Map(location=[10.5, 45.0], zoom_start=7, tiles="CartoDB positron")

# Ku dar dhibcaha khariidadda
for place in data:
    color = "green"
    if place['Risk'] == "Red": color = "red"
    elif place['Risk'] == "Orange": color = "orange"
    
    folium.Marker(
        location=[place['Lat'], place['Lon']],
        popup=f"{place['City']}: Dabaysha {place['Wind']} knots",
        tooltip=place['City'],
        icon=folium.Icon(color=color, icon="info-sign")
    ).add_to(m)

# Muuji khariidadda
st_folium(m, width=1200, height=500)

# 5. Dashboard-ka dhinaca (Sidebar)
st.sidebar.header("Xaaladda Maanta")
for p in data:
    st.sidebar.metric(label=p['City'], value=f"{p['Wind']} kt", delta=p['Risk'])

# 6. Action Button
if st.button("Dir Digniin SMS ah (dhammaan goobaha cas)"):
    red_zones = [p['City'] for p in data if p['Risk'] == "Red"]
    if red_zones:
        st.error(f"SMS digniin ah ayaa loo diray: {', '.join(red_zones)}")
    else:
        st.success("Ma jiraan goobo khatar ah hadda.")

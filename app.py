import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import plotly.express as px
import pandas as pd
from simulate import simulate_data
from streamlit_folium import st_folium
import folium
from simulate import simulate_data  # if your function is in a file named simulate.py
# OR just paste simulate_data() directly in app.py if not in another file
st.set_page_config(layout="wide")
st_autorefresh(interval=10000, key="datarefresh")

df = simulate_data()  # This generates new data every time app runs

st.title(" Resilient Grid Dashboard – Cyclone Outage Monitor")

st.write("Last Updated:", datetime.now().strftime("%H:%M:%S"))

df["timestamp"] = pd.date_range(start='2025-06-01', periods=len(df), freq='H')  # Add a time column if not present

# Add colorful metric cards
col1, col2, col3 = st.columns(3)
col1.metric(" Max Wind Speed", f"{df['wind_speed'].max():.1f} km/h")
col2.metric(" Max Rainfall", f"{df['rainfall'].max():.1f} mm")
col3.metric(" Outage Zones", df['outage_risk'].sum())

st.markdown("---")

# Wind Speed and Rainfall Over Time
fig1 = px.area(df, x="timestamp", y="wind_speed", color_discrete_sequence=['#1f77b4'])
fig2 = px.bar(df, x="timestamp", y="rainfall", color_discrete_sequence=['#00cc96'])

st.subheader(" wind_speed &  Rainfall Over Time")
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

# Power Output Simulation
fig3 = px.line(df, x="timestamp", y="power_output", color="outage_risk",
               color_discrete_map={0: "green", 1: "red"},
               markers=True, title=" Power Output Simulation")
st.subheader(" Grid Power Output with Outage Alerts")
st.plotly_chart(fig3, use_container_width=True)

# Map view with outage status
st.subheader(" Grid Zones - Live Status")

zones = {
    "Zone A": [13.0827, 80.2707],
    "Zone B": [12.9716, 77.5946],
    "Zone C": [11.0168, 76.9558]
}
map_ = folium.Map(location=[12.5, 78.5], zoom_start=6)

for i, (zone, coords) in enumerate(zones.items()):
    outage = df.iloc[i]["outage_risk"]
    color = "red" if outage else "green"
    folium.CircleMarker(location=coords, radius=15,
                        color=color, fill=True, fill_opacity=0.7,
                        tooltip=f"{zone} - {'⚠️ Outage' if outage else '✅ Stable'}").add_to(map_)

st_folium(map_, width=700, height=450)

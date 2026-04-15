import streamlit as st
import folium
from streamlit_folium import st_folium

if "lat_max" not in st.session_state:
    st.session_state.lat_max = 48.8566
if "lon_max" not in st.session_state:
    st.session_state.lon_max = 2.3522

st.title("📍 Study Area")

mode = st.radio(
    "Method of entering coordinates",
    options=["📌 Click on the map", "⌨️ Manual entry"],
    horizontal=True,
)

def build_map():
    m = folium.Map(
        location=[st.session_state.lat_max, st.session_state.lon_max],
        zoom_start=7,
        tiles="OpenStreetMap"
    )
    folium.Marker(
        location=[st.session_state.lat_max, st.session_state.lon_max],
        popup="Position",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)
    return m


if mode == "📌 Click on the map":
    st.markdown("**Click on the map to set the study point**")
    
    m = build_map()
    map_data = st_folium(
        m,
        key="study_map_click",
        width=700,
        height=450,
        returned_objects=["last_clicked"],
    )

    if map_data and map_data.get("last_clicked"):
        clicked = map_data["last_clicked"]
        if (clicked["lat"] != st.session_state.lat_max or 
            clicked["lng"] != st.session_state.lon_max):
            st.session_state.lat_max = round(clicked["lat"], 4)
            st.session_state.lon_max = round(clicked["lng"], 4)
            st.rerun()

else:  
    with st.form("form_zone_etude"):
        col_lat, col_lon = st.columns(2)
        with col_lon:
            new_lon = st.number_input(
                "Longitude (°)",
                value=float(st.session_state.lon_max),
                format="%.4f",
            )
        with col_lat:
            new_lat = st.number_input(
                "Latitude (°)",
                value=float(st.session_state.lat_max),
                format="%.4f",
            )
        
        submitted = st.form_submit_button("Confirm")
        
        if submitted:
            st.session_state.lon_max = new_lon
            st.session_state.lat_max = new_lat
            st.success("Coordinates saved!")
            st.rerun() 
    m = build_map()
    st_folium(m, key="map_manual", width=700, height=300, returned_objects=[])

st.markdown("---")
st.markdown("### Selected Coordinates")
c1, c2 = st.columns(2)
c1.metric("Longitude", f"{st.session_state.lon_max:.4f}°")
c2.metric("Latitude", f"{st.session_state.lat_max:.4f}°")

if st.button("Next", type='primary', use_container_width=True):
    st.switch_page("pages/4_Economie.py")
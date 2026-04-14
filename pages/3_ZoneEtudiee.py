import streamlit as st
import folium
from streamlit_folium import st_folium
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

# À adapter si tu as déjà REGIONS ailleurs dans ton projet
REGIONS = [
    "Europe",
    "Afrique",
    "Asie",
    "Amérique du Nord",
    "Amérique du Sud",
    "Océanie",
]

# Initialisation session_state pour que la page soit autonome
if "region" not in st.session_state:
    st.session_state.region = REGIONS[0]

if "lat_min" not in st.session_state:
    st.session_state.lat_min = 48.8566

if "lon_min" not in st.session_state:
    st.session_state.lon_min = 2.3522

if "lat_max" not in st.session_state:
    st.session_state.lat_max = 48.8566

if "lon_max" not in st.session_state:
    st.session_state.lon_max = 2.3522

st.title("📍 Study area")


mode = st.radio(
    "Method of entering coordinates",
    options=["📌 Click on the map ", "⌨️ Manual entry"],
    horizontal=True,
)

def build_map():
    center_lat = (st.session_state.lat_min + st.session_state.lat_max) / 2
    center_lon = (st.session_state.lon_min + st.session_state.lon_max) / 2

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=7,
        tiles="OpenStreetMap"
    )

    folium.Marker(
        location=[st.session_state.lat_min, st.session_state.lon_min],
        popup="Position",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

    if (
        st.session_state.lat_min != st.session_state.lat_max
        or st.session_state.lon_min != st.session_state.lon_max
    ):
        folium.Marker(
            location=[st.session_state.lat_max, st.session_state.lon_max],
            popup="Point max",
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(m)

        folium.Rectangle(
            bounds=[
                [st.session_state.lat_min, st.session_state.lon_min],
                [st.session_state.lat_max, st.session_state.lon_max],
            ],
            color="#2563eb",
            fill=True,
            fill_opacity=0.15,
        ).add_to(m)

    return m

if mode == "📌 Click on the map":
    st.markdown("**Click on the map to set the study point**")
    st.caption("The last click sets the coordinates.")

    m = build_map()

    map_data = st_folium(
        m,
        key="study_map",
        width=700,
        height=450,
        returned_objects=["last_clicked"],
    )

    if map_data and map_data.get("last_clicked"):
        clicked_lat = map_data["last_clicked"]["lat"]
        clicked_lng = map_data["last_clicked"]["lng"]

        st.session_state.lat_min = round(clicked_lat, 4)
        st.session_state.lon_min = round(clicked_lng, 4)
        st.session_state.lat_max = round(clicked_lat, 4)
        st.session_state.lon_max = round(clicked_lng, 4)

        st.rerun()

else:
    st.caption("Laisser min = max pour un point unique.")

    with st.form("form_zone_etude"):

            lon_max = st.number_input(
                "Longitude  (°)",
                value=float(st.session_state.lon_max),
                step=0.01,
                format="%.4f",
            )
            lat_max = st.number_input(
                "Latitude  (°)",
                value=float(st.session_state.lat_max),
                step=0.01,
                format="%.4f",
            )

            submitted = st.form_submit_button("Confirm")

    if submitted:
        st.session_state.lon_max = lon_max
        st.session_state.lat_max = lat_max

        st.success("Datas saved successfully")

    m = build_map()
    st_folium(
        m,
        key="study_map_manual",
        width=700,
        height=400,
        returned_objects=[],
    )

st.markdown("### Set coordinates")
col1, col2 = st.columns(2)

with col1:
    st.metric("Longitude ", f"{st.session_state.lon_max:.4f}°")
with col2:
    st.metric("Latitude ", f"{st.session_state.lat_max:.4f}°")

if st.button("Next", type='primary'):
    st.switch_page("pages/4_Economie.py")
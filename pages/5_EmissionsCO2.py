import streamlit as st
import pandas as pd
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu ()
st.title("🌿  Émissions CO₂")

with st.form("form_CO2"):
    col1, col2 = st.columns(2)
    with col1:
        pv_emissions = st.number_input("PV (gCO₂eq/Wp)", value=st.session_state.pv_emissions, step=10, key="em_pv")
        inverter_emissions = st.number_input("Onduleur (gCO₂eq/Wp)", value=st.session_state.inverter_emissions, step=5, key="em_inv")
        ms_emissions = st.number_input("Structures (gCO₂eq/Wp)", value=st.session_state.ms_emissions, step=1.0, format="%.1f", key="em_ms")
    with col2:
        rms_emissions = st.number_input("Câblage (gCO₂eq/Wp)", value=st.session_state.rms_emissions, step=1, key="em_rms")
        mp_emissions = st.number_input("Moto-pompe (gCO₂eq/W)", value=st.session_state.mp_emissions, step=5, key="em_mp")

    em_data = pd.DataFrame({
        "Composant": ["PV", "Onduleur", "Structures", "Câblage", "Moto-pompe"],
        "gCO₂eq/Wp": [
            pv_emissions,
            inverter_emissions,
            ms_emissions,
            rms_emissions,
            mp_emissions,
        ]
    }).set_index("Composant")
    st.bar_chart(em_data, height=250, color="#16a34a")

    submitted = st.form_submit_button("Valider")

if submitted:
    st.session_state.pv_emissions = pv_emissions
    st.session_state.inverter_emissions = inverter_emissions
    st.session_state.ms_emissions = ms_emissions
    st.session_state.rms_emissions = rms_emissions
    st.session_state.mp_emissions = mp_emissions

    st.success("Configuration sauvegardée !")
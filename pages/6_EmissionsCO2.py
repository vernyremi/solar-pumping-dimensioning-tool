import streamlit as st
import pandas as pd
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu ()
st.title("🌿  CO$_{2}$ emissions")

with st.form("form_CO2"):
    col1, col2 = st.columns(2)
    with col1:
        pv_emissions = st.number_input("Photovoltaic emissions (gCO₂eq/Wp)", value=st.session_state.pv_emissions, step=10)
        inverter_emissions = st.number_input("Converter emissions (gCO₂eq/Wp)", value=st.session_state.inverter_emissions, step=5)
        ms_emissions = st.number_input("Structure emissions (gCO₂eq/Wp)", value=st.session_state.ms_emissions, step=1.0, format="%.1f")
    with col2:
        rms_emissions = st.number_input("Wiring emissions (gCO₂eq/Wp)", value=st.session_state.rms_emissions, step=1)
        mp_emissions = st.number_input("Motor pumping emissions (gCO₂eq/W)", value=st.session_state.mp_emissions, step=5)

    submitted = st.form_submit_button("Confirm")

if submitted:
    st.session_state.pv_emissions = pv_emissions
    st.session_state.inverter_emissions = inverter_emissions
    st.session_state.ms_emissions = ms_emissions
    st.session_state.rms_emissions = rms_emissions
    st.session_state.mp_emissions = mp_emissions

    st.success("Datas saved successfully")

if st.button("Next", type='primary',use_container_width=True):
    st.switch_page('pages/7_Hydrogeologie.py')
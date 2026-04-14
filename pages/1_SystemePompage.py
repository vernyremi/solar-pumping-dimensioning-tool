import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

CATALOGUE_POMPES = {
    "SQF5A-7": {"label": "SQF 5A-7 (Grundfos)", "P_max": 1400, "TDH_max": 70},
    "SOLAR_103_DCSSP_9000": {"label": "SOLAR 103 DCSSP 9000", "P_max": 9000, "TDH_max": 120},
}

CONFIGURATIONS = ["Network", "Photovoltaics", "Hybride"]
# acquisition données à remplacer par les API

st.title("⚙️ Pomping system choice")

with st.form("form_pompe"):

    col1, col2 = st.columns(2)
    
    with col1:
        motor_pump = st.selectbox(
            "Motor pump",
            options=list(CATALOGUE_POMPES.keys()),
            format_func=lambda k: CATALOGUE_POMPES[k]["label"],
            index=list(CATALOGUE_POMPES.keys()).index(st.session_state.motor_pump),
        )

    with col2:
        configuration = st.selectbox(
            "Configuration",
            options=CONFIGURATIONS,
            index=CONFIGURATIONS.index(st.session_state.configuration),
        )

    p_max = st.number_input(
        "Maximum power in entrance (W)",
        value=st.session_state.p_max,
        step=100,
    )

    revente = st.checkbox(
        "Electricity resell to the network",
        value=st.session_state.revente
    )

    submitted = st.form_submit_button("Confirm")

# Mise à jour uniquement si validé
if submitted:
    st.session_state.motor_pump = motor_pump
    st.session_state.configuration = configuration
    st.session_state.p_max = p_max
    st.session_state.revente = revente

    st.success("Datas saved successfully !")
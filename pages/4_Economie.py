import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

st.title("💰  Économie")

with st.form("form_economie"):
    life_expectancy = st.number_input("Durée de vie du système (ans)", value=st.session_state.life_expectancy, min_value=1, step=1)

    st.markdown("#### Coûts unitaires")
    col1, col2, col3 = st.columns(3)
    with col1:
        grid_elec_cost = st.number_input("Électricité réseau (INR/kWh)", value=st.session_state.grid_elec_cost, step=0.1, format="%.2f")
        pv_cost = st.number_input("Modules PV (INR/Wc)", value=st.session_state.pv_cost, step=0.5, format="%.1f")
        inverter_cost = st.number_input("Onduleur (INR/W)", value=st.session_state.inverter_cost, step=0.5, format="%.1f")
    with col2:
        grid_elec_cost_resail = st.number_input("Revente élec. (INR/kWh)", value=st.session_state.grid_elec_cost_resail, step=0.1, format="%.2f")
        mp_cost = st.number_input("Moto-pompe (INR/W)", value=st.session_state.mp_cost, step=0.1, format="%.1f")
        ms_cost = st.number_input("Structures montage (INR/Wc)", value=st.session_state.ms_cost, step=0.1, format="%.1f")
    with col3:
        wf_cost = st.number_input("Main d'œuvre (INR)", value=st.session_state.wf_cost, step=500)
        rms_cost = st.number_input("Câblage / capteurs (INR/Wc)", value=st.session_state.rms_cost, step=0.01, format="%.2f")

    st.markdown("#### Durées de vie des composants (ans)")
    col1, col2, col3 = st.columns(3)
    with col1:
        lt_pv = st.number_input("PV", value=st.session_state.lt_pv, min_value=1, step=1)
        lt_mp = st.number_input("Moto-pompe", value=st.session_state.lt_mp, min_value=1, step=1)
    with col2:
        lt_inverter = st.number_input("Onduleur", value=st.session_state.lt_inverter, min_value=1, step=1)
        lt_ms = st.number_input("Structures", value=st.session_state.lt_ms, min_value=1, step=1)
    with col3:
        lt_rms = st.number_input("Câblage", value=st.session_state.lt_rms, min_value=1, step=1)
        lt_pipe = st.number_input("Tuyaux", value=st.session_state.lt_pipe, min_value=1, step=1)

    st.markdown("#### Taux")
    col1, col2 = st.columns(2)
    with col1:
        dr = st.number_input("Taux d'actualisation (%)", value=st.session_state.dr, step=0.5, format="%.1f")
    with col2:
        maintenance_rate = st.number_input("Maintenance annuelle (% du coût initial)", value=st.session_state.maintenance_rate, step=0.1, format="%.1f")

    submitted = st.form_submit_button("Valider")


if submitted:
    st.session_state.life_expectancy = life_expectancy
    st.session_state.grid_elec_cost = grid_elec_cost
    st.session_state.pv_cost = pv_cost
    st.session_state.inverter_cost = inverter_cost
    st.session_state.grid_elec_cost_resail = grid_elec_cost_resail
    st.session_state.mp_cost = mp_cost 
    st.session_state.ms_cost = ms_cost
    st.session_state.wf_cost = wf_cost
    st.session_state.rms_cost = rms_cost
    st.session_state.lt_pv = lt_pv
    st.session_state.lt_mp = lt_mp
    st.session_state.lt_inverter = lt_inverter
    st.session_state.lt_ms = lt_ms
    st.session_state.lt_rms = lt_rms
    st.session_state.lt_pipe = lt_pipe
    st.session_state.dr = dr
    st.session_state.maintenance_rate = maintenance_rate
    

    st.success("Configuration sauvegardée !")
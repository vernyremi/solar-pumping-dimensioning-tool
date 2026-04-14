import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

st.title("💰  Economy")

with st.form("form_economie"):

    st.markdown("#### Unitary costs (default parameters)")
    st.write("The below parameters are to be changed only if you have different datas to specify")
    col1, col2, col3 = st.columns(3)
    with col1:
        grid_elec_cost = st.number_input("Cost of electricity on the network (INR/kWh)", value=st.session_state.grid_elec_cost, step=0.1, format="%.2f")
        pv_cost = st.number_input("Cost of photovoltaic module (INR/Wc)", value=st.session_state.pv_cost, step=0.5, format="%.1f")
        inverter_cost = st.number_input("Cost of inverter (INR/W)", value=st.session_state.inverter_cost, step=0.5, format="%.1f")
    with col2:
        grid_elec_cost_resail = st.number_input("Cost of electricity resell (INR/kWh)", value=st.session_state.grid_elec_cost_resail, step=0.1, format="%.2f")
        mp_cost = st.number_input("Cost of motor pumping (INR/W)", value=st.session_state.mp_cost, step=0.1, format="%.1f")
        ms_cost = st.number_input("Assembly structures (INR/Wc)", value=st.session_state.ms_cost, step=0.1, format="%.1f")
    with col3:
        wf_cost = st.number_input("Workforce cost (INR)", value=st.session_state.wf_cost, step=500)
        rms_cost = st.number_input("Cost of wiring/captors/etc (INR/Wc)", value=st.session_state.rms_cost, step=0.01, format="%.2f")

    submitted = st.form_submit_button("Confirm")


if submitted:

    st.session_state.grid_elec_cost = grid_elec_cost
    st.session_state.pv_cost = pv_cost
    st.session_state.inverter_cost = inverter_cost
    st.session_state.grid_elec_cost_resail = grid_elec_cost_resail
    st.session_state.mp_cost = mp_cost 
    st.session_state.ms_cost = ms_cost
    st.session_state.wf_cost = wf_cost
    st.session_state.rms_cost = rms_cost
    

    st.success("Datas saved successfully")

if st.button("Next", type='primary'):
    st.switch_page('pages/5_EmissionsCO2.py')

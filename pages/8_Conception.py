import streamlit as st 
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu ()
st.title("🔧  Conception")

epsilon_val = st.number_input("Pipe roughness (m)", value=st.session_state.epsilon_val, step=1e-5, format="%.6f")

with st.expander("Additional parameters"):

    col1, col2 = st.columns(2)
    with col1:
        gamma_val = st.number_input("Temperature loss coefficient of photovoltaic pannels  (%/°C)", value=st.session_state.gamma_val, step=0.01, format="%.2f")
        cpv_loss = st.number_input("Other photovoltaic pannels loss (-)", value=st.session_state.cpv_loss, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
    with col2:
        noct_val = st.number_input("NOCT (Nominal Operating Cell Temperature) (°C)", value=st.session_state.noct_val, step=1)
        ht_val = st.number_input("Height of the water outlet (m)", value=st.session_state.ht_val, step=0.1, format="%.1f")
        eta_inv = st.number_input("Energy eficciency of the inverter (-)", value=st.session_state.eta_inv, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
        
    submitted = st.button("Confirm")


if submitted:
    st.session_state.gamma_val = gamma_val
    st.session_state.epsilon_val = epsilon_val
    st.session_state.cpv_loss = cpv_loss
    st.session_state.noct_val = noct_val
    st.session_state.ht_val = ht_val
    st.session_state.eta_inv = eta_inv
    
    st.success("Data saved successffully")

if st.button('Calculate', type='primary', use_container_width=True):
    st.switch_page("pages/9_Results.py")
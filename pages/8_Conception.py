import streamlit as st 
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu ()
st.title("🔧  Conception")


with st.form("form_conception"):

    col1, col2, col3 = st.columns(3)
    with col1:
        gamma_val = st.number_input("Coeff. perte temp. PV γ (%/°C)", value=st.session_state.gamma_val, step=0.01, format="%.2f")
        epsilon_val = st.number_input("Rugosité tuyau ε (m)", value=st.session_state.epsilon_val, step=1e-5, format="%.6f")
        cpv_loss = st.number_input("Pertes PV cpv_loss (-)", value=st.session_state.cpv_loss, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
    with col2:
        noct_val = st.number_input("NOCT (°C)", value=st.session_state.noct_val, step=1)
        ht_val = st.number_input("Hauteur sortie eau Ht (m)", value=st.session_state.ht_val, step=0.1, format="%.1f")
        eta_inv = st.number_input("Rendement onduleur η_inv (-)", value=st.session_state.eta_inv, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")
    with col3:
        beta_val = st.number_input("Pertes forage β (m²/s⁵)", value=st.session_state.beta_val, step=100)

    submitted = st.form_submit_button("Valider")


if submitted:
    st.session_state.gamma_val = gamma_val
    st.session_state.epsilon_val = epsilon_val
    st.session_state.cpv_loss = cpv_loss
    st.session_state.noct_val = noct_val
    st.session_state.ht_val = ht_val
    st.session_state.eta_inv = eta_inv
    st.session_state.beta_val = beta_val

    st.success("Configuration sauvegardée !")
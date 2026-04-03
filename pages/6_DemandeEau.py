import streamlit as st
import pandas as pd 
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu ()
st.title("💧  Demande en eau")

MOIS = ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun", "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"]

with st.form("form_demande_eau"):
    col1, col2, col3 = st.columns(3)
    with col1:
        crop_area = st.number_input("Surface cultivée (ha)", value=st.session_state.crop_area, step=0.1, format="%.1f")
    with col2:
        percolation_rate = st.number_input("Taux percolation riz (mm/j)", value=st.session_state.percolation_rate, step=0.5, format="%.1f")
    with col3:
        conveyance_eff = st.number_input("Efficacité convoyage (-)", value=st.session_state.conveyance_eff, step=0.01, min_value=0.0, max_value=1.0, format="%.2f")

    st.markdown("#### Demande mensuelle brute (m³/mois par hax10)")

    gw = st.session_state.gw_demand
    cols = st.columns(6)
    new_gw = list(gw)
    for i in range(12):
        with cols[i % 6]:
            new_gw[i] = st.number_input(MOIS[i], value=float(gw[i]), step=0.01, format="%.5f", key=f"gw_{i}")
    gw_demand = new_gw

    chart_df = pd.DataFrame({"Mois": MOIS, "Demande (m³)": new_gw}).set_index("Mois")
    st.bar_chart(chart_df, height=220, color="#2563eb")

    submitted = st.form_submit_button("Valider")


if submitted:
    st.session_state.crop_area = crop_area
    st.session_state.percolation_rate = percolation_rate
    st.session_state.conveyance_eff = conveyance_eff
    st.session_state.gw_demand = new_gw
    
    st.success("Configuration sauvegardée !")
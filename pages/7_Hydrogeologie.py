import streamlit as st
import pandas as pd
from utils.menu import show_menu

show_menu()

MOIS = ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun", "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"]

st.title("🪨  Hydrogéologie")

with st.form("form_hydrogeologie"):

    col1, col2 = st.columns(2)
    with col1:
        time_step = st.number_input("Pas de temps (min)", value=st.session_state.time_step, min_value=1, step=10)
    with col2:
         dt_val= st.number_input("Temps d'arrêt dt (min)", value=st.session_state.dt_val, min_value=1, step=10, help="Doit être ≥ time_step")

    st.markdown("#### Profondeur statique mensuelle Hbs (m)")
    hbs = st.session_state.hbs_mat
    cols = st.columns(6)
    new_hbs = list(hbs)
    for i in range(12):
        with cols[i % 6]:
            new_hbs[i] = st.number_input(MOIS[i], value=float(hbs[i]), step=0.1, format="%.1f", key=f"hbs_{i}")
    hbs_mat = new_hbs

    hbs_df = pd.DataFrame({"Mois": MOIS, "Profondeur (m)": new_hbs}).set_index("Mois")
    st.line_chart(hbs_df, height=200, color="#7c3aed")

    col1, col2 = st.columns(2)
    with col1:
        t_mat = st.number_input("Transmissivité T (m²/s)", value=st.session_state.t_mat, step=1e-3, format="%.4f")
    with col2:
        s_mat = st.number_input("Emmagasinement S (-)", value=st.session_state.s_mat, step=0.001, format="%.4f", min_value=0.0, max_value=1.0)

    submitted = st.form_submit_button("Valider")


if submitted: 

    st.session_state.time_step = time_step
    st.session_state.dt_val = dt_val
    st.session_state.hbs_mat = hbs_mat
    st.session_state.t_mat = t_mat
    st.session_state.s_mat = s_mat

    st.success("Configuration sauvegardée !")
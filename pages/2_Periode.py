import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

st.title("📅 Choix de la période")

with st.form("form_periode"):

    col1, col2 = st.columns(2)
    with col1:
        year = st.number_input("Année", value=st.session_state.year, min_value=2000, max_value=2100, step=1)
    with col2:
        nbr_jour_annee = st.number_input("Jours dans l'année", value=st.session_state.nbr_jour_annee, min_value=365, max_value=366, step=1, help="366 si bissextile")

    col3, col4 = st.columns(2)
    with col3:
        nbr_j_etu_par_mois = st.number_input("Jours étudiés par mois", value=st.session_state.nbr_j_etu_par_mois, min_value=1, max_value=31, step=1, help="Si >28 → mois complets")
    with col4:
        nbr_mois_etudies = st.number_input("Nombre de mois étudiés", value=st.session_state.nbr_mois_etudies, min_value=1, max_value=12, step=1)

    submitted = st.form_submit_button("Valider")

if submitted:
    st.session_state.year = year
    st.session_state.nbr_jour_annee = nbr_jour_annee
    st.session_state.nbr_j_etu_par_mois = nbr_j_etu_par_mois
    st.session_state.nbr_mois_etudies = nbr_mois_etudies

    st.success("Configuration sauvegardée !")
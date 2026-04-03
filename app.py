import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

st.set_page_config(page_title="Accueil", layout="centered")


st.title("☀️ Dimensionnement d'un système de pompage solaire")
st.write("Bienvenue dans cette application Streamlit multi-pages.")

st.markdown("""
### Navigation
Utilisez le menu à gauche pour :
- Remplir le formulaire
- Choisir des options
- Voir les résultats
""")


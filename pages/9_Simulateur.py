import streamlit as st 
from utils.menu import show_menu
from utils.init_session import init_session_defaults
from application.application_main import main 

init_session_defaults()
show_menu ()
st.title("🔧  Simulateur")

if st.button("Lancer la simulation"):
    main ()
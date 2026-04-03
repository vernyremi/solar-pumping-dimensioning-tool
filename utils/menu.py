import streamlit as st


def show_menu():
    st.sidebar.title("📌 Navigation")

    st.sidebar.page_link("app.py", label="🏠 Accueil")
    st.sidebar.page_link("pages/1_SystemePompage.py", label="⚙️ Système de pompage")
    st.sidebar.page_link("pages/2_Periode.py", label="📅 Période")
    st.sidebar.page_link("pages/3_ZoneEtudiee.py", label="📍 Zone étudiée")
    st.sidebar.page_link("pages/4_Economie.py", label="💰 Économie")
    st.sidebar.page_link("pages/5_EmissionsCO2.py", label="🌿  Émissions CO₂")
    st.sidebar.page_link("pages/6_DemandeEau.py", label="💧 Demande en eau")
    st.sidebar.page_link("pages/7_Hydrogeologie.py", label="🪨  Hydrogéologie")
    st.sidebar.page_link("pages/8_Conception.py", label="🔧  Conception")
    st.sidebar.page_link("pages/9_Simulateur.py", label="🔧  Simulateur")
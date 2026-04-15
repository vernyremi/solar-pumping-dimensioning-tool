import streamlit as st


def show_menu():
    st.sidebar.title("📌 Browsing")

    st.sidebar.page_link("app.py", label="🏠 Homepage")
    st.sidebar.page_link("pages/1_SystemePompage.py", label="⚙️ Pumping system choice")
    st.sidebar.page_link("pages/2_Periode.py", label="📅 Period choice")
    st.sidebar.page_link("pages/3_ZoneEtudiee.py", label="📍 Study area")
    st.sidebar.page_link("pages/4_Economie.py", label="💰 Economy")
    st.sidebar.page_link("pages/5_EmissionsCO2.py", label="🌿 CO₂ emissions")
    st.sidebar.page_link("pages/6_DemandeEau.py", label="💧 Water demand")
    st.sidebar.page_link("pages/7_Hydrogeologie.py", label="🪨  Hydrgeology")
    st.sidebar.page_link("pages/8_Conception.py", label="🔧  Conception")
    st.sidebar.page_link("pages/9_Results.py", label="📊  Results")

import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

st.title("📅 Period choice")

with st.form("form_periode"):
    st.write('In order to do the correct calculations, please enter a year with normal conditions of sunshine and precipitation.')
    year = st.number_input("Année", value=st.session_state.year, min_value=2000, max_value=2100, step=1)

    submitted = st.form_submit_button("Confirm")

if submitted:
    st.session_state.year = year

    st.success("Data saved successfully")

if st.button("Next", type='primary',use_container_width=True):
    st.switch_page("pages/3_ZoneEtudiee.py")
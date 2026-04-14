import streamlit as st
import pandas as pd 
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu ()
st.title("💧  Water demand")

MOIS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

with st.form("form_demande_eau"):
    st.markdown("#### Monthly raw demand in water (m³/month)")

    gw = st.session_state.gw_demand
    cols = st.columns(6)
    new_gw = list(gw)
    for i in range(12):
        with cols[i % 6]:
            new_gw[i] = st.number_input(MOIS[i], value=float(gw[i]), step=0.01, format="%.5f", key=f"gw_{i}")
    gw_demand = new_gw

    chart_df = pd.DataFrame({"Mois": MOIS, "Demande (m³)": new_gw})
    chart_df["Mois"] = pd.Categorical(chart_df["Mois"], categories=MOIS, ordered=True)
    chart_df = chart_df.set_index("Mois")
    st.bar_chart(chart_df, height=220, color="#2563eb")
    
    submitted = st.form_submit_button("Confirm")

st.write("""
### Help
If you do not know your monthly needs for water, you may enter the total area of land you want to irrigate in the box below 
""")
crop_area = st.number_input("Area with cultures (ha)", value=st.session_state.crop_area, step=0.1, format="%.1f")
sub = st.button("Confirm")

if submitted or sub:
    st.session_state.crop_area = crop_area
    st.session_state.gw_demand = new_gw
    
    st.success("Datas saved successfully")

if st.button("Next", type='primary'):
    st.switch_page('pages/7_Hydrogeologie.py')
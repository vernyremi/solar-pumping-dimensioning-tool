import streamlit as st
import pandas as pd
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

MOIS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

st.title("🪨  Hydrogeology")

with st.form("form_hydrogeologie"):

    #col1, col2 = st.columns(2)
    #with col1:
        #time_step = st.number_input("Pas de temps (min)", value=st.session_state.time_step, min_value=1, step=10)
    #with col2:
         #dt_val= st.number_input("Temps d'arrêt dt (min)", value=st.session_state.dt_val, min_value=1, step=10, help="Doit être ≥ time_step")
    
    st.markdown("#### Monthly static depth (m)")
    hbs = st.session_state.hbs_mat
    cols = st.columns(6)
    new_hbs = list(hbs)
    for i in range(12):
        with cols[i % 6]:
            new_hbs[i] = st.number_input(MOIS[i], value=float(hbs[i]), step=0.1, format="%.1f", key=f"hbs_{i}")
    hbs_mat = new_hbs

    hbs_df = pd.DataFrame({"Mois": MOIS, "Profondeur (m)": new_hbs})
    hbs_df["Mois"] = pd.Categorical(hbs_df["Mois"], categories=MOIS, ordered=True)
    hbs_df = hbs_df.set_index("Mois")
    st.line_chart(hbs_df, height=200, color="#7c3aed")

    submitted = st.form_submit_button("Confirm")

with st.expander(" Additional parameters") :
    col1, col2, col3 = st.columns(3)
    with col1:
        t_mat = st.number_input("Transmissibility  (m²/s)", value=st.session_state.t_mat, step=1e-3, format="%.4f")
    with col2:
        s_mat = st.number_input("Storage  (-)", value=st.session_state.s_mat, step=0.001, format="%.4f", min_value=0.0, max_value=1.0)
    with col3:
        beta_val = st.number_input("Drilling losses (m²/s⁵)", value=st.session_state.beta_val, step=100)

    sub = st.button("Confirm")
if submitted or sub: 

    #st.session_state.time_step = time_step
    #st.session_state.dt_val = dt_val
    st.session_state.hbs_mat = hbs_mat
    st.session_state.t_mat = t_mat
    st.session_state.s_mat = s_mat
    st.session_state.beta_val = beta_val

    st.success("Datas saved successfully")

if st.button("Next", type='primary'):
    st.switch_page('pages/8_Conception.py')
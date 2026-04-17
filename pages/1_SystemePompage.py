import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

CATALOGUE_POMPES = {
    "SQF5A-7": {"label": "SQF 5A-7 (Grundfos)", "P_max": 1400, "TDH_max": 70},
    "SOLAR_103_DCSSP_9000": {"label": "SOLAR 103 DCSSP 9000", "P_max": 9000, "TDH_max": 120},
}

CONFIGURATIONS = ["Network", "Photovoltaics", "Hybride"]

st.title("⚙️ Pumping System Configuration")

with st.form("form_pompe"):

    col1, col2 = st.columns(2)
    
    # ---------------- MOTOR PUMP ----------------
    with col1:
        st.markdown("### 🔧 Motor Pump")
        with st.expander("ℹ️ About Motor Pump"):
            st.markdown("""
Select the **motor pump model** used in the system.

Each pump is defined by:
- **P_max**: Maximum electrical power  
- **TDH_max**: Maximum **Total Dynamic Head**

This choice directly affects the **performance** and **capacity** of the system.
""")

        motor_pump = st.selectbox(
            "",
            options=list(CATALOGUE_POMPES.keys()),
            format_func=lambda k: CATALOGUE_POMPES[k]["label"],
            index=list(CATALOGUE_POMPES.keys()).index(st.session_state.motor_pump),
        )

    # ---------------- CONFIGURATION ----------------
    with col2:
        st.markdown("### ⚙️ Configuration")
        with st.expander("ℹ️ About Configuration"):
            st.markdown("""
Choose the **system configuration**:

- **Network**: Powered by the electrical grid  
- **Photovoltaics**: Powered by solar panels  
- **Hybrid**: Combination of **solar energy** and grid

Defines the **energy source** and system behavior.
""")

        configuration = st.selectbox(
            "",
            options=CONFIGURATIONS,
            index=CONFIGURATIONS.index(st.session_state.configuration),
        )

    # ---------------- RESALE ----------------
    st.markdown("### 🔄 Electricity Resell to the Network")
    with st.expander("ℹ️ About Electricity Resell"):
        st.markdown("""
Indicates if **excess electricity** can be sent back to the grid.

- Enables **energy resale**  
- Useful in **photovoltaic** or **hybrid systems**  
- Improves **energy efficiency**
""")

    revente = st.checkbox(
        "",
        value=st.session_state.revente
    )

    submitted = st.form_submit_button("Confirm")


# Update only if submitted
if submitted:
    st.session_state.motor_pump = motor_pump
    st.session_state.configuration = configuration
    st.session_state.revente = revente

    st.success("Data saved successfully!")

if st.button("Next", type="primary"):
    st.switch_page("pages/2_Periode.py")
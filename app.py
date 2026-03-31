import streamlit as st
from utils.menu import show_menu

st.set_page_config(page_title="Accueil", layout="centered")

show_menu()

st.title("☀️ Dimensionnement d'un système de pompage solaire")
st.write("Bienvenue dans cette application Streamlit multi-pages.")

st.markdown("""
### Navigation
Utilisez le menu à gauche pour :
- Remplir le formulaire
- Choisir des options
- Voir les résultats
""")


# variables par défaut 
defaults = {
    "motor_pump": "SOLAR_103_DCSSP_9000",
    "configuration": "Hybride",
    "p_max": 9000,
    "revente": True,
    "sauvegarder": False,
    "year": 2024,
    "nbr_jour_annee": 366,
    "nbr_j_etu_par_mois": 31,
    "nbr_mois_etudies": 12,
    "region": "IGB",
    "lon_min": 74.81, "lat_min": 30.44,
    "lon_max": 74.81, "lat_max": 30.44,
    "life_expectancy": 20,
    "grid_elec_cost": 6.5, "grid_elec_cost_resail": 6.5,
    "pv_cost": 36.0, "mp_cost": 3.7, "inverter_cost": 9.0,
    "ms_cost": 5.6, "rms_cost": 2.40, "wf_cost": 15000,
    "lt_pv": 25, "lt_mp": 10, "lt_inverter": 10,
    "lt_ms": 50, "lt_rms": 5, "lt_pipe": 50,
    "dr": 10.0, "maintenance_rate": 1.0,
    "pv_emissions": 2485, "inverter_emissions": 124,
    "ms_emissions": 60.6, "rms_emissions": 5, "mp_emissions": 60,
    "crop_area": 3.0, "percolation_rate": 6.0, "conveyance_eff": 0.85,
    "gw_demand": [99.26065, 0.0, 0.0, 0.0, 0.0, 682.89945, 244.24558, 200.76050, 260.27346, 195.94975, 31.80126, 98.38408],
    "time_step": 60, "dt_val": 60,
    "hbs_mat": [13.1, 13.1, 13.1, 12.9, 12.6, 12.8, 13.9, 14.9, 15.1, 14.8, 14.8, 14.8],
    "t_mat": 2.9e-2, "s_mat": 0.072,
    "gamma_val": -0.4, "noct_val": 44, "beta_val": 2400,
    "epsilon_val": 1.28e-4, "ht_val": 1.0,
    "cpv_loss": 0.0, "eta_inv": 0.96,
    "t0_val": 50, "n_pts": 5, "n_segments": 5,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v
import streamlit as st
from utils.menu import show_menu
from utils.init_session import init_session_defaults

init_session_defaults()
show_menu()

st.set_page_config(page_title="Homepage", layout="centered")


st.title("☀️ Sizing of your Solar Water Pumping System")


st.markdown("""
### Our Mission
Our platform is designed to help farmers change the way they access their most vital resource : **Water**. \n
By transitioning from traditional thermal engines and unstable grid electricity to solar-powered systems, we aim to provide a sustainable, cost-effective, and autonomous future for rural communities.

### What We Offer
We provide a precision dimensioning tool that calculates the ideal configuration for your water pumping system. Our algorithm processes your own informations in order to deliver a customized answer to your request.

### Geographic & Climate Analysis 
We integrate local meteorological data and groundwater depth (aquifer levels) to ensure system reliability.

### Tailored Agricultural Needs
Every farm is different. Our tool factors in crop types, field surface area, and specific daily water requirements to size the perfect pump and solar array.

### Who Is This For?
**For Farmers:** To help you reduce operational costs, eliminate the need for expensive fuel, and gain complete energy independence.

**For NGOs & Field Agents:** A technical companion to help you design, justify, and implement irrigation projects with scientific accuracy and speed.

### Why Choose Solar Pumping?
**Economic Freedom:** Stop spending a significant portion of your income on gasoline or diesel. Once installed, the sun provides energy for free that can even be resold if your production exceeds your consumption.

**Reliability:** Unlike national power grids, which can be prone to frequent blackouts, solar energy is consistent and available where you need it most.

**Environmental Stewardship:** Reduce your carbon footprint. Solar pumping is a clean technology that preserves the air quality and health of your local ecosystem.

**Resilience:** Empower communities to be self-sufficient and resilient in the face of fluctuating global energy prices.

""")

st.write("""
### How to do ?
The process is simple. You may just follow the procedure on the following pages and enter your datas to allow the aglorithm to do his work. \n
When it is done you will get for results the motor pump model and solar installation size you need according to what you have entered. \n
Informations are at your disposal next to the different datas you must give to help you in your approach.     
 """)

if st.button("Start", type="primary",use_container_width=True):
    st.switch_page("pages/1_SystemePompage.py")
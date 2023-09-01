import pandas as pd 
import plotly.express as px
import streamlit as st 
import warnings
import pymysql
import plotly.graph_objects as go
from plotly.subplots import make_subplots
warnings.filterwarnings("ignore")
st.set_page_config(layout="wide", initial_sidebar_state="auto")

@st.cache_resource
# Set the background color
def set_background():
    # Add CSS to change the background color
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #371560;
            color: magneta;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# Call the function to set the background color 6739B7
set_background()

st.markdown("<h1 style='text-align: left; font-weight: bold; color: #A05EEA; font-size: 45px;'>PhonePe Pulse Visualization Dashboard</h1>", unsafe_allow_html=True)
    
# INDIA MAP ANALYSIS
st.write("# :green[PHONEPE INDIA MAP]")
c1,c2=st.columns(2)
with c1:
    Year = st.selectbox(
            'Select the Year',
            ('2018', '2019', '2020','2021','2022'))
with c2:
    Quarter = st.selectbox(
            'Select the Quarter',
            ('Q1 (Jan-Mar)', 'Q2 (Apr-Jun)', 'Q3 (Jul-Sep)','Q4 (Oct-Dec)'))
year=int(Year)
string_value = Quarter
quarter= int(''.join(filter(str.isdigit, string_value)))

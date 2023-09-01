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

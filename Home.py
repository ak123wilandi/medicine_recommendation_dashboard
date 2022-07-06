from streamlit_option_menu import option_menu
from menu import (
    About as about, 
    Chart as chart, 
    Patient_Review as patient_review, 
    Print_Documents as print, 
    Tables as table
)

import streamlit as st
import pandas as pd
import numpy as pd


with open('style/Home.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def home():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Tables', 'Charts', 'Print', 'Review'],
        icons = ['house', 'table', 'file-bar-graph', 'printer', 'file-earmark-check'],
        menu_icon = 'house-fill', 
        default_index = 0,
        orientation = "horizontal"
    )
    
    if selected == 'About': about.about()
    if selected == 'Tables': table.tables()
    if selected == 'Charts': chart.chart()
    if selected == 'Print': print.print_docs()
    if selected == 'Review': patient_review.patient_review()

home()
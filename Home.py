from fpdf import FPDF as pdf
from menu import (
    About as about, 
    Chart as chart, 
    Patient_Review as patient_review, 
    Print_Documents as print_docs, 
    Tables as table
)
from streamlit_option_menu import option_menu

import streamlit as st
import pandas as pd
import numpy as pd


# with open('style/Home.css') as file:
#     st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def home():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Tables', 'Charts', 'Print', 'Review'],
        icons = ['house_fill', 'table', 'file-bar-graph', 'printer', 'file-earmark-check'],
        menu_icon = 'house-fill', 
        default_index = 0,
        orientation = "horizontal",
        styles = {
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#31333F", "font-size": "20px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#ff4b4b"},
        } 
    )
    
    if selected == 'About': about.about()
    if selected == 'Tables': table.tables()
    if selected == 'Charts': chart.chart()
    if selected == 'Print Document': print_docs.print_docs()
    if selected == 'Patient Review': patient_review.patient_review()

home()
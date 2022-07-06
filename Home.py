from fpdf import FPDF as pdf

import streamlit as st
import pandas as pd
import numpy as pd

with open('home.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def start_home():
    st.title("Welcome to Medicine Recommendation We Apps")

if __name__ == '__main__':
    start_home()
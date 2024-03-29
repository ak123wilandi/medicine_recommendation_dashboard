from random import randint
import streamlit as st
import pandas as pd
import os

DATA = './data/indonesian_medicine_dataset.csv'

with open('style/Tables.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)


def tables():
    st.title("Table Data")
    data = pd.DataFrame(pd.read_csv(DATA))
    name, desc = data['Name'].head(5).to_list(), data[['Overview']].head(5)
    st.metric(name[0], 15)

    
    

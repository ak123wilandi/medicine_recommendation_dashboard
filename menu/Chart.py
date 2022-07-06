import streamlit as st

with open('style/Chart.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def check():
    pass

def chart():
    st.title("Data Visualization")

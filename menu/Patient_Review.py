import streamlit as st

with open('style/Patient_Review.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def patient_review():
    st.title("Patient Reviews")


import streamlit as st

with open('style/Patient_Review.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def start_home():
    st.title("Patient Reviews")


if __name__ == '__main__':
    start_home()
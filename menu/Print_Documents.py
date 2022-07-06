import streamlit as st

with open('style/Print_Documents.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def print_docs():
    st.title("Print the Recommendation Document")



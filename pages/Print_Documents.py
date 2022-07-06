import streamlit as st

with open('style/Print_Documents.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def start_home():
    st.title("Print the Recommendation Document")


if __name__ == '__main__':
    start_home()
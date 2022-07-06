import streamlit as st

with open('charts.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def start_home():
    st.title("Data Visualization")


if __name__ == '__main__':
    start_home()
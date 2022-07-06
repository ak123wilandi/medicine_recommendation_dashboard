import streamlit as st


with open('style/About.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)


def about():
    st.title("About the Project")
    st.subheader("1. The Introduction")
    st.markdown("This project are created for the **educational purposes**. All the reviews are the developer\
                assumptions by journal and research in brainstorming schedules.")

    st.subheader("2. The Introduction")
    st.markdown("The Dataset are recorded by using Web Scrapping with \
                [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) \
                and [Requests](https://requests.readthedocs.io/en/latest/) \
                methods for **educational purposes**")




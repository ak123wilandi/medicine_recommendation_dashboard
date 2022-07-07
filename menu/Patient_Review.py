import streamlit as st
from streamlit_disqus import st_disqus
import pandas as pd

with open('style/Patient_Review.css') as file:
    st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)

def patient_review():
    st.title("Patient Reviews")
    # st_disqus("Streamlit")

    form = st.form(key='my_form')
    name = form.text_input(label='Your Full Name : ', placeholder = 'Your Name')
    email = form.text_input(label='Your Email : ', placeholder = 'Your Email')
    disease_one = form.selectbox('What the most disease that your feel right now?',
                                 ('Cough', 'High Temperature', 'Low Temperature'))
    disease_two = form.selectbox('Another disease that you feel ? ',
                                  ('Headache', 'hallucination', 'Blurred Vision'))
    blood_type = form.selectbox('Blood type', 
                                  ('A', 'O', 'B', 'AB'))
    submit_button = form.form_submit_button(label='Submit')
    

    info_list = []
    if submit_button:
        user_info = {
            'Name': f'{name}',
            'Email': f'{email}',
            'Disease': f'{disease_one},{disease_two}',
            'BloodType': f'{blood_type}'
        }
        info_list.append(user_info)
        df = pd.DataFrame(info_list)
        df.to_csv('data/user_info.csv', mode = 'a', header = False, index = False)  
        
        st.markdown(f"Hello, **{name}**.\
                      \nYour diseases are: \
                      \n 1. {disease_one}\
                      \n2. {disease_two}\
                      \nAnd your blood type is **{blood_type}**")
        
        st.markdown('Your Data are Saved as our Patient Review')


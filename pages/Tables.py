from random import randint, random
import streamlit as st
import pandas as pd
import os

DATA = './data/medicine_dataset.csv'


def start_home():
    st.title("Table Data")
    data = pd.DataFrame(pd.read_csv(DATA))
    name, desc = data['Name'].head(5).to_list(), data[['Description']].head(5)
    for n in name:
        st.metric(n, randint(10, 16))


if __name__ == '__main__':
    start_home()
from fpdf import FPDF as pdf

import streamlit as st
import pandas as pd
import numpy as pd

class Home:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_user_info(self):
        pass

    def get_dasboard(self):
        pass

    def get_foobar(self):
        pass

    def start_home(self):
        st.write("Hello World!!!!")


if __name__ == '__main__':
    home = Home('Samuel', 20)

    home.start_home()
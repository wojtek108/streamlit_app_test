import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

header = st.container()
dataExploration = st.container() 

with header:
    st.title("Workouts review")
    st.text('A simple streamlit webapp with dataframe containing my workout loggs')

with dataExploration:
    data = pd.read_csv('data/data.csv')
    reversed_data = data[::-1]  # Reverse the order of the dataframe
    st.dataframe(reversed_data.head(1050))


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

header = st.container()
dataExploration = st.container() 

with header:
    st.title("Workouts review")
    st.text('A simple streamlit webapp with dataframe containing my workout loggs')

with dataExploration:
    data = pd.read_csv('data/data.csv')
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')      
    # Reverse the order of the dataframe
    reversed_data = data[::-1]  
    st.dataframe(reversed_data.head(1050))

    st.subheader('Chart: Workouts per Month')
    fig, ax = plt.subplots(figsize=(12, 6))
    data['Date'].value_counts().sort_index().plot(kind='line', ax=ax)
    monthly_workouts = data.groupby(data['Date'].dt.to_period('M')).size()  
    monthly_workouts.plot(kind='bar', ax=ax)
    plt.xlabel('Month')
    plt.ylabel('Workouts')
    st.pyplot(fig)
                            

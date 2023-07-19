import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

header = st.container()
dataExploration = st.container()

with header:
    st.title("Workouts review")
    st.text('A simple Streamlit web app with a dataframe containing my workout logs')

with dataExploration:
    data = pd.read_csv('data/data.csv')
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    # Reverse the order of the dataframe
    reversed_data = data[::-1]
    st.dataframe(reversed_data.head(1050))

    st.subheader('Chart: Workouts per Month')
    monthly_workouts = data.groupby(data['Date'].dt.to_period('M')).size().reset_index(name='Workouts')
    chart = alt.Chart(monthly_workouts).mark_bar().encode(
        x=alt.X('Date:T', title='Month'),
        y=alt.Y('Workouts:Q', title='Workouts'),
        tooltip=['Date:T', 'Workouts']
    ).properties(
        width=800,
        height=400
    )
    st.altair_chart(chart, use_container_width=True)

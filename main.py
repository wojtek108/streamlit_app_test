import streamlit as st
import pandas as pd

header = st.container()
dataExploration = st.container() 
newFeatures = st.container() 
modelTraining = st.container()

with header:
    st.title("Welcome to my app")
    st.text('In this project I look into streamlit app')

with dataExploration:
    st.header('Sample dataset')
    data = pd.read_csv('data/student.csv')
    st.write(data.head(50))
    st.header('Sample bar chart')
    mark_distribution = pd.DataFrame(data['mark'].value_counts()).head(50)
    st.bar_chart(mark_distribution)


with newFeatures:
    st.header('Some text from markdown')
    st.markdown('**This text is in bold**') 



with modelTraining:
    st.header('Columns in webapp UI')
    first_col, second_col = st.columns(2)

    first_col.subheader('Column I')
    second_col.subheader('Column II')
    

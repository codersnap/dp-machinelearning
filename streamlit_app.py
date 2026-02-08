import streamlit as st
import pandas as pd

st.title('🤖 machine learning APP')

st.info('This is app builds a machine learning model')

with st.expander('Data'):
    st.write('**Raw Data**')
    df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
    df

    st.write('**x**')
    x=df.drop('species',axis=1)
    x


    st.write('**y**')
    y=df.species
    y

with st.expander('Data visualtion'):

    st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')

with st.sidebar:
    st.header('Input feature')
    island=st.selectbox('Island',('Biscoe','Dream','Torgerson'))
    gender=st.selectbox('Gender',('male','female'))
    bill_length_mm=st.slider('Bill length (mm)',32.1,59.6,43.9)


        

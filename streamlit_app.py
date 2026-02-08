import streamlit as st
import pandas as pd

st.tittle('🤖 machine learning APP')

st.info('This is app builds a machine learning model')

with st.expand('Data'):
    st.write('**Raw Data**')
    df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
    df

    st.writez('**x**')
    x=df.drop('species',axis=1)
    x


    st.write('**y**')
    y=df.species
    y

with st.expand('Data visualtion'):

    st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')


        

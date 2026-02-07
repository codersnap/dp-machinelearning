import streamlit as st
import pandas as pd
st.title('🤖 Machine learning app')

st.info('This is a machine learning app')
with st.expander('Data'):
  
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  
  st.write('**X**')
  x = df.drop('species',axis=1)
  x
  
  st.write('**y**')
  y=df.species
  y
  
with st.expander('**Data visualisation**'):
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')

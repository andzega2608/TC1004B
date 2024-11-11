import streamlit as st
import pandas as pd
import numpy as np
st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv("Policev1.csv")
st.markdown("The data shown below belogs to incident reports in the city of San Francisco from the year 2018 to 2020, with details fron each case such as date, day of week, police strict, neighborhood in which happened, type of accident in category, exact location and resolution")
df
mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df ['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
mapa
subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
  subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]
                        
  

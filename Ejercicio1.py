import streamlit as st
import pandas as pd

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv("Policev1.csv")

st.markdown("The data shown below belogs to incident reports in the city of San Francisco from the year 2018 to 2020, with details fron each case such as date, day of week, police strict, neighborhood in which happened, type of accident in category, exact location and resolution")


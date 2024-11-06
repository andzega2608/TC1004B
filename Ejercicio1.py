import streamlit as st
import pandas as pd

st.title('Police Incident: Reportort from 2018 to 2020 in San Francisco')
df = pd.read_csv("PoliceV1.csv")
df


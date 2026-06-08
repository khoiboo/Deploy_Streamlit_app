import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.write("Here is a test of Streamlit app")

fig = plt.figure()
plt.bar(x = range(5), height = [9, 8, 7, 6, 5])
plt.xlabel("X-axis")
plt.title("A random graph")
st.pyplot(fig)

selected = st.selectbox(label = "Choose an option", options = ["AAA", "BBB", "CCC"])
st.write(f"You have selected {selected}")

PATH_INCIDENT_FOLDER = "./Raw_Data/Incident/"
PATH_MOBILISATION_FOLDER = "./Raw_Data/Mobilisation/"

@st.cache_data
def read_incident():
    incident_18_23 = pd.read_excel(PATH_INCIDENT_FOLDER + "LFB Incident data from 2018 - 2023.xlsx")
    incident_from_24 = pd.read_excel(PATH_INCIDENT_FOLDER + "LFB Incident data from 2024 onwards.xlsx")

    merged_incident = pd.concat([incident_18_23, incident_from_24], axis = 0)
    merged_incident = merged_incident[merged_incident.CalYear >= 2021]

    print(f"From 2021 the shape of incident is {merged_incident.shape}")

    return merged_incident

merged_incident = read_incident()

@st.cache_data
def read_mobilisation():
    mobilisation_18_24 = pd.read_csv(PATH_MOBILISATION_FOLDER + "LFB Mobilisation data from 2021 - 2024.csv")
    mobilisation_from_25 = pd.read_csv(PATH_MOBILISATION_FOLDER + "LFB Mobilisation data from 2025.csv")

    merged_mobilisation = pd.concat([mobilisation_18_24, mobilisation_from_25], axis = 0)
    merged_mobilisation = merged_mobilisation[merged_mobilisation.CalYear >= 2021]

    return merged_mobilisation

merged_mobilisation = read_mobilisation()

st.write(f"The shape of incident is {merged_incident.shape}")
st.write(f"The shape of mobilisation is {merged_mobilisation.shape}")





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

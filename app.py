import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


st.title("My first App")
st.header("Module is EDAB")
st.subheader("Its a fun module")

# Generate random time series data
time_series = np.random.randn(100)

variable = st.button("My button")
if variable
  time_series = np.random.randn(2000)
  fig, ax = plt.subplots()
  ax.plot(time_series)
  ax.set_title("my graph")
  ax.set_xlabel("units")
  ax.set_ylabel("value")
  st.pyplot(fig)



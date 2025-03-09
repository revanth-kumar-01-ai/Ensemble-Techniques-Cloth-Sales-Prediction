import streamlit as st
import pandas as pd

# Title
st.title("📊 Data Exploration")

# Histogram for Sales
st.subheader("📉 Sales Distribution (Histogram)")
st.image('StreamlitUI/assets/hist.png')
st.write("The histogram shows how sales are distributed in the dataset.")

# Outliers Detection
st.subheader("🚨 Outliers in the Data")
st.image('StreamlitUI/assets/outliers.png')
st.write("The following features have outliers: **Price, CompPrice, and Sales**.")

# Q-Q Plot Analysis
st.subheader("📈 Q-Q Plot Analysis")
st.image('StreamlitUI/assets/qq.png')
st.write("The dataset is mostly **normally distributed**, but some values show slight deviations.")

st.markdown("🔍 **This analysis helps understand data distribution and outliers.**")





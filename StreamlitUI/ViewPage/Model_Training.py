import streamlit as st  

# Page Title
st.header("📌 Model Training")

# Model Training Description
st.markdown("""
### 🔥 Ensemble Learning for Clothing Sales Prediction  
This project uses various **Ensemble Learning** techniques to improve accuracy.  
We apply different models and compare their performance.  
""")

# Models Used
st.subheader("🛠️ Models Used in Training")

st.markdown("""
- **Stacking** (KNN, Logistic Regression, Random Forest, Decision Tree)  
- **Voting** (KNN, Logistic Regression, Random Forest, Decision Tree)  
- **Bagging**  
  - AdaBoost + Random Forest  
  - Gradient Boosting  
  - XGBoost Classifier  
""")

# Model Performance Comparison
st.subheader("📊 Model Performance Comparison")

st.markdown("""
| 🚀 **Ensemble Method**                      | 🎯 **Train Accuracy** | 📈 **Test Accuracy** |
|--------------------------------------------|----------------------|----------------------|
| 🗳️ **Voting**                              | **0.8833**           | **0.9179**           |
| 🏗️ **Stacking**                            | **0.8917**           | **0.9071**           |
| 🎭 **Bagging (AdaBoost + RF as Estimators)** | **0.8583**           | **0.9750**           |
| 🌱 **Bagging (Gradient Boosting)**          | **0.8500**           | **0.9857**           |
| 🚀 **Bagging (XGBoost Classifier)**         | **0.8500**           | **0.9536**           |
""", unsafe_allow_html=True)

st.markdown("🔍 **Higher test accuracy indicates better model performance on unseen data.**")

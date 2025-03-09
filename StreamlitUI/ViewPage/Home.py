import streamlit as st  

# Home Page Title
st.title("🛍️ Ensemble Techniques for Cloth Sales Prediction")

# Project Overview
st.markdown(
    """
    **Welcome to the Cloth Sales Prediction App!**  
    This app implements various Ensemble Learning techniques such as **Bagging, Boosting (AdaBoost, Gradient Boost, XGBoost), Stacking, and Voting** to improve sales prediction accuracy. 🚀  
    """
)

# Model Optimization
st.subheader("📊 Model Optimization")
st.markdown(
    """
    - **Train, test, and compare models** using performance metrics.  
    - **Hyperparameter tuning** with GridSearchCV to improve predictions.  
    """
)

# Workflow Steps
st.subheader("🚀 WorkFlow")
workflow_steps = [
    "Update 🛠️ config.yaml", "Update 📜 schema.yaml", "Update ⚙️ params.yaml",
    "Update 🏗️ the entity", "Update 📝 the configuration manager in src/config",
    "Update 🧩 the components", "Update 🔄 the pipeline", "Update 🚀 main.py",
    "Update 🌐 app.py"
]
st.write("\n".join([f"✅ {step}" for step in workflow_steps]))

# CRISP Methodology
st.subheader("📌 CRISP Methodology")
crisp_steps = [
    "✅ Business & Data Understanding 📊🔍", "✅ Data Preparation 🧹📂",
    "✅ Model Building 🤖⚙️", "✅ Model Evaluation 📈✅",
    "✅ Model Deployment 🚀💻", "✅ Maintenance & Monitoring 🛠️👀"
]
st.write("\n".join(crisp_steps))

# Business Understanding
st.subheader("📂 Business & Data Understanding")
st.markdown(
    """
    **Problem Statement:**  
    A **cloth manufacturing company** 🏭 wants to identify key factors that contribute to **high sales** 📈.  
    The goal is to build **Decision Tree 🌳 and Random Forest 🌲 models**, with Sales as the target variable.
    """
)

# Business Objectives & Constraints
st.subheader("🎯 Business Objectives & Constraints")
st.write("✅ Business Objective: Maximize profits 💰")
st.write("✅ Business Constraint: Minimize time to identify key attributes ⏳")

# Success Criteria
st.subheader("📊 Success Criteria")
st.write("📈 Business Success: Increase sales by 20%")
st.write("🤖 ML Success: Accuracy above 80%")
st.write("💰 Economic Success: Ensure profits exceed $3,000 USD")

# Data Understanding
st.subheader("📂 Data Understanding")
st.write("The dataset contains **11 features** and **400 rows**, provided by a trusted institute 🏛️.")

# Display Feature Descriptions in Table
import pandas as pd
feature_data = {
    "Feature": ["Sales", "CompPrice", "Income", "Advertising", "Population",
                "Price", "ShelveLoc", "Age", "Education", "Urban", "US"],
    "Description": [
        "📈 Target variable (Product Sales)", "💲 Competitor's product price",
        "💰 Customer's annual income", "📢 Marketing budget spent",
        "🌍 Population in the area", "🏷️ Product selling price",
        "📌 Shelf display location", "🎂 Customer’s age group",
        "🎓 Years of education", "🏙️ Urban or rural location", "🇺🇸 Customer in the US"
    ]
}
df = pd.DataFrame(feature_data)
st.dataframe(df)

# Footer
st.markdown("🚀 **Let's build an accurate sales prediction model!** 🚀")

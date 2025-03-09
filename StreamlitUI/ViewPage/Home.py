import streamlit as st  
import pandas as pd  

# 🎯 App Title
st.title("🛍️ Ensemble Techniques for Cloth Sales Prediction")

# 📌 Project Overview
st.markdown(
    """
    **Welcome to the Cloth Sales Prediction App!**  
    This application utilizes **Ensemble Learning** techniques—including **Bagging, Boosting (AdaBoost, Gradient Boost, XGBoost), Stacking, and Voting**—to enhance sales prediction accuracy. 🚀  
    """
)

# 📊 Model Optimization
st.subheader("⚙️ Model Optimization")
st.markdown(
    """
    - **Train, test, and evaluate models** using key performance metrics.  
    - **Hyperparameter tuning** (e.g., GridSearchCV) to optimize model performance.  
    """
)

# 🚀 Workflow Steps
st.subheader("🔄 Workflow")
st.markdown(
    """
    1️⃣ **Update** 🛠️ `config.yaml` (Configuration settings)  
    2️⃣ **Update** 📜 `schema.yaml` (Data schema)  
    3️⃣ **Update** ⚙️ `params.yaml` (Hyperparameters)  
    4️⃣ **Define** 🏗️ **Entities**  
    5️⃣ **Configure** 📝 **Configuration Manager (`src/config`)**  
    6️⃣ **Develop** 🧩 **Components**  
    7️⃣ **Build** 🔄 **Pipeline**  
    8️⃣ **Run** 🚀 `main.py`  
    9️⃣ **Deploy** 🌐 `app.py`  
    """
)

# 📌 CRISP-DM Methodology
st.subheader("📈 CRISP-DM Methodology")
st.markdown(
    """
    ✅ **Business & Data Understanding** 📊🔍  
    ✅ **Data Preparation** 🧹📂  
    ✅ **Model Building** 🤖⚙️  
    ✅ **Model Evaluation** 📈✅  
    ✅ **Model Deployment** 🚀💻  
    ✅ **Monitoring & Maintenance** 🛠️👀  
    """
)

# 📂 Business & Data Understanding
st.subheader("📂 Business & Data Understanding")

st.markdown(
    """
    ### 🎯 **Problem Statement**  
    A **clothing manufacturing company** 🏭 aims to identify key factors influencing **high sales** 📈.  
    The goal is to build **Decision Tree** 🌳 and **Random Forest** 🌲 models, with **Sales** as the **target variable**, which needs to be converted into a **categorical variable** 🎯.  

    ### 📌 **Business Objectives & Constraints**  
    - ✅ **Objective:** Maximize profits 💰  
    - ⏳ **Constraint:** Minimize the time required to identify key sales attributes  

    ### 📊 **Success Criteria**  
    - 📈 **Business Success:** Increase sales by **20%**  
    - 🤖 **ML Success:** Achieve an accuracy above **80%**  
    - 💰 **Economic Success:** Ensure business profits exceed **$3,000 USD**  
    """
)

# 🏷️ Feature Descriptions
st.subheader("📊 Feature Descriptions")

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

# 🚀 Final Message
st.markdown("✅ **Let's build an accurate and data-driven sales prediction model!** 🚀")

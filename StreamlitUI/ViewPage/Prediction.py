import streamlit as st
import pandas as pd
import joblib
import os

st.header("🛒 Clothing Sales Prediction - User Input")

# Function for One-Hot Encoding
def encode_category(value, options):
    return [1 if value == opt else 0 for opt in options[:-1]]  # Drop last category

# Create three columns
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # Categorical Inputs
    shelve_loc = st.selectbox("📌 Select Shelve Location", ["Good", "Medium", "Bad"])
    urban = st.selectbox("🏙️ Urban Area?", ["Yes", "No"])
    us = st.selectbox("🇺🇸 Customer in the US?", ["Yes", "No"])

with col2:
    # Numerical Inputs - Part 1
    comp_price = st.number_input("💲 Competitor's Price", min_value=0.0, step=1.0)
    income = st.number_input("💰 Customer's Income", min_value=0.0, step=1.0)
    advertising = st.number_input("📢 Advertising Budget", min_value=0.0, step=1.0)
    population = st.number_input("🌍 Population", min_value=0.0, step=1.0)

with col3:
    # Numerical Inputs - Part 2
    price = st.number_input("🏷️ Product Price", min_value=0.0, step=1.0)
    age = st.number_input("🎂 Customer's Age", min_value=0, step=1)
    education = st.number_input("🎓 Education Level", min_value=0, step=1)

# Apply Encoding
shelve_loc_good, shelve_loc_medium = encode_category(shelve_loc, ["Good", "Medium", "Bad"])
urban_yes, = encode_category(urban, ["Yes", "No"])
us_yes, = encode_category(us, ["Yes", "No"])

# Create a dictionary for JSON conversion
user_inputs_dict = {
    "CompPrice": comp_price,
    "Income": income,
    "Advertising": advertising,
    "Population": population,
    "Price": price,
    "Age": age,
    "Education": education,
    "ShelveLoc_Good": shelve_loc_good,
    "ShelveLoc_Medium": shelve_loc_medium,
    "Urban_Yes": urban_yes,
    "US_Yes": us_yes,
}

# Submit Button
if st.button("🔍 Predict"):
    try:
        st.subheader("🔹 Selected & Encoded Values (JSON)")
        df = pd.DataFrame([user_inputs_dict])
        st.table(df)

        # Check if model file exists before loading
        model_path = './StreamlitUI/models/finialModel.joblib'
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            res = model.predict(df)

            # Display Prediction Result
            st.subheader("📢 Prediction Result")
            if res[0] >= 1:
                st.success("🟢 **High Sales Prediction!**")
            else:
                st.warning("🟠 **Low Sales Prediction!**")
        else:
            st.error("⚠️ Model file not found! Please check the path.")

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")



import streamlit as st

st.header("📌 Conclusion Page")

st.write(
    """
    The **Clothing Sales Prediction** project used **Ensemble Learning** techniques like 
    Bagging, Boosting, Stacking, and Voting to improve prediction accuracy.  

    These are the **Ensemble Learning** model accuracies for the project. Based on the results:  
    🔥 **Stacking is the preferred choice** as it has **low bias and variance** ✅  
    """
)

# Model Performance Summary
st.subheader("🏆 Best Model Performance")
st.table(
    {
        "🏗️ **Model**": ["Stacking"],
        "🎯 **Train Accuracy**": [0.8917],
        "📈 **Test Accuracy**": [0.9071],
    }
)

st.write(
    """
    📌 **Key Takeaways:**  
    - **Stacking performed best** among all models.  
    - It **balances bias and variance**, making it a **stable** and **reliable** choice.  
    - Other models like **Bagging (XGBoost, Gradient Boosting)** also showed good accuracy but had higher variance.  

    🎯 **Next Steps:**  
    - Further fine-tuning can improve accuracy.  
    - Real-world deployment requires continuous monitoring.  
    - Feature engineering and additional data can enhance the model's performance.  

    🚀 Thank you for exploring this project!  
    """
)

# Ensemble-Techniques-Cloth-Sales-Prediction
🛍️ Ensemble Learning: Implement Bagging, Boosting (AdaBoost, Gradient Boost, XGBoost), Stacking, and Voting on the dataset to enhance accuracy. 📊 Model Optimization: Train, test, and compare models using performance metrics. Apply GridSearchCV to find the best hyperParameters for improved predictions. 🚀

## 🚀 WorkFlow  
1️⃣ **Update** 🛠️ `config.yaml`  
2️⃣ **Update** 📜 `schema.yaml`  
3️⃣ **Update** ⚙️ `params.yaml`  
4️⃣ **Update** 🏗️ **the entity**  
5️⃣ **Update** 📝 **the configuration manager in `src/config`**  
6️⃣ **Update** 🧩 **the components**  
7️⃣ **Update** 🔄 **the pipeline**  
8️⃣ **Update** 🚀 `main.py`  
9️⃣ **Update** 🌐 `app.py`  

## 📌 **CRISP Methodology**  
✅ **Business & Data Understanding** 📊🔍  
✅ **Data Preparation** 🧹📂  
✅ **Model Building** 🤖⚙️  
✅ **Model Evaluation** 📈✅  
✅ **Model Deployment** 🚀💻  
✅ **Maintenance & Monitoring** 🛠️👀  

## 📂 **Business & Data Understanding**  

### 📌 **Problem Statement**  
A **cloth manufacturing company** 🏭 wants to identify key attributes that contribute to **high sales** 📈. The goal is to build **Decision Tree** 🌳 and **Random Forest** 🌲 models, with **Sales** as the **target variable**, which must first be **converted into a categorical variable** 🎯.  

### 🎯 **Business Objectives & Constraints**  
✅ **Business Objective:** Maximize profits 💰  
✅ **Business Constraint:** Minimize the time required to identify key attributes ⏳  

### 📊 **Success Criteria**  
- **📈 Business Success Criteria:** Increase sales by **20%**  
- **🤖 ML Success Criteria:** Achieve an accuracy of over **80%**  
- **💰 Economic Success Criteria:** Ensure business profits exceed **$3,000 USD**  

## 📂 **Data Understanding**  

The dataset is provided by a **trusted institute** 🏛️ and contains:  
- **11 features** 📊  
- **400 rows** 📝  

### 🔢 **Feature Names & Descriptions**  
- **Sales** 📈 – Target variable, product sales  
- **CompPrice** 💲 – Competitor's product price  
- **Income** 💰 – Customer's annual income  
- **Advertising** 📢 – Marketing budget spent  
- **Population** 🌍 – Population in the area  
- **Price** 🏷️ – Product selling price  
- **ShelveLoc** 📌 – Shelf display location  
- **Age** 🎂 – Customer’s age group  
- **Education** 🎓 – Years of education  
- **Urban** 🏙️ – Urban or rural location  
- **US** 🇺🇸 – Customer in the US


# 📊 Accuracy  

These are the **Ensemble Learning** model accuracies for the **Clothing Sales Prediction** project. Based on the results, **🔥 Stacking is the preferred choice** as it has **low bias and variance**. ✅  

### 📌 Model Performance Comparison  

| 🚀 **Ensemble Method**                      | 🎯 **Train Accuracy** | 📈 **Test Accuracy** |
|--------------------------------------------|----------------------|----------------------|
| 🗳️ **Voting**                              | 0.8833               | 0.9179               |
| 🏗️ **Stacking**                            | 0.8917               | 0.9071               |
| 🎭 **Bagging (AdaBoost + RF as Estimators)** | 0.8583               | 0.9750               |
| 🌱 **Bagging (Gradient Boosting)**          | 0.8500               | 0.9857               |
| 🚀 **Bagging (XGBoost Classifier)**         | 0.8500               | 0.9536               |

📌 **Conclusion:** Among all the ensemble methods tested, **Stacking** is chosen as the best model due to its **balanced bias-variance tradeoff**. 🏆🎯  



## 🔗 MLflow Link  

[Ensemble Techniques - Cloth Sales Prediction](https://dagshub.com/revanth-kumar-01-ai/Ensemble-Techniques-Cloth-Sales-Prediction.mlflow) 🚀


## 🚀 Streamlit App  

🔗 [Ensemble Techniques - Cloth Sales Prediction](https://ensemble-techniques-cloth-sales-prediction-ba49kfhpnjfesfsy7pf.streamlit.app/) 🌟  


# 📊 Customer Churn Prediction  

## 🚀 Project Overview  
This project predicts **customer churn** (whether a customer will leave the bank) using machine learning.  
We trained, tuned, and evaluated models, then deployed a **Streamlit app** for easy usage.  

---

## ✅ Achievements  

### 🔹 Data & Preprocessing  
- Dataset: **10,000 bank customers** with demographic & account features.  
- Dropped irrelevant columns: `RowNumber`, `CustomerId`, `Surname`.  
- Preprocessing pipeline:  
  - **Numerical features** → imputed + scaled.  
  - **Categorical features** → imputed + one-hot encoded.  

---

### 🔹 Modeling  
- Baseline: **RandomForestClassifier**.  
- Imbalance handled with `class_weight={0:1, 1:3}`.  
- Models compared: RandomForest, XGBoost, LightGBM.  
- Evaluation metrics: **ROC-AUC, Precision-Recall, F1, Confusion Matrix**.  

---

### 🔹 Key Results  
- **Final choice:** RandomForest (tuned) with threshold **0.4**.  
- **Performance on test set (threshold=0.4):**  
  - Recall (churners): **73%** → catches ~3 out of 4 churners.  
  - Precision: **55%** → about half of flagged are true churners.  
  - F1-score: **0.62**.  
  - Accuracy: **82%**.  
- Confusion Matrix:  
  - True Negatives: 1346  
  - False Positives: 247  
  - False Negatives: 111  
  - True Positives: 296  

---

### 🔹 Deployment  
- Saved pipeline as `churn_model.pkl`.  
- Chosen threshold saved in `churn_threshold.txt`.  
- Built **Streamlit app (`app.py`)**:  
  - Upload CSV of customers.  
  - Get churn probabilities & predictions.  
  - Download results as CSV.  

---

## 🛠️ Usage  

### 1. Run Jupyter Notebook  
Train the model and save it:  
```bash
jupyter notebook Churn_Prediction_Bank_Final.ipynb
```

### 2. Launch Streamlit App  
```bash
streamlit run app.py
```

### 3. Upload Data  
- Use `churn_test_customers.csv` (provided) or your own customer dataset.  
- The app will output:  
  - **Churn probability**  
  - **Final prediction (0 = stay, 1 = churn)**  

---

## 📈 Next Steps  
- Host app on **Streamlit Cloud / Heroku / AWS**.  
- Add **explainability (SHAP feature importance)**.  
- Automate **batch predictions** for CRM integration.  
- Monitor model drift & re-train periodically.  

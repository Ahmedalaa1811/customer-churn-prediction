import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load model & threshold
model = joblib.load("models/churn_model.pkl")
with open("models/churn_threshold.txt", "r") as f:
    threshold = float(f.read().strip())

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")
st.title("📊 Customer Churn Prediction App")

st.markdown("""
Choose how you want to predict churn:
1. Upload a CSV file with multiple customers.
2. Enter details of a single customer manually.
""")

# ================== SINGLE CUSTOMER FORM ==================
st.header("👤 Single Customer Prediction")

with st.form("single_customer_form"):
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
    geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure (Years at bank)", min_value=0, max_value=50, value=5)
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)
    products = st.number_input("Number of Products", min_value=1, max_value=5, value=1)
    has_card = st.selectbox("Has Credit Card?", [0, 1])
    active = st.selectbox("Is Active Member?", [0, 1])
    salary = st.number_input("Estimated Salary", min_value=0.0, value=60000.0)

    submitted = st.form_submit_button("Predict")

    if submitted:
        single_df = pd.DataFrame([{
            "CreditScore": credit_score,
            "Geography": geography,
            "Gender": gender,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance,
            "NumOfProducts": products,
            "HasCrCard": has_card,
            "IsActiveMember": active,
            "EstimatedSalary": salary
        }])

        prob = model.predict_proba(single_df)[:, 1][0]
        pred = int(prob >= threshold)

        st.write(f"### Prediction: {'❌ Will Churn' if pred==1 else '✅ Will Stay'}")
        st.write(f"**Churn Probability:** {prob:.2f}")

# ================== MULTI CUSTOMER UPLOAD ==================
st.header("📂 Predict Churn from CSV")

uploaded_file = st.file_uploader("Upload customer data (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data")
    st.dataframe(data.head())

    # Predictions
    probs = model.predict_proba(data)[:, 1]
    preds = (probs >= threshold).astype(int)

    results = data.copy()
    results["Churn_Probability"] = probs
    results["Churn_Prediction"] = preds

    st.write("### Predictions")
    st.dataframe(results)

    # Download
    csv = results.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Predictions as CSV",
        data=csv,
        file_name="churn_predictions.csv",
        mime="text/csv"
    )

    # ================== DASHBOARD METRICS ==================
    st.markdown("---")
    st.header("📊 Dataset Insights")

    churn_rate = (results["Churn_Prediction"].mean()) * 100
    churn_count = results["Churn_Prediction"].sum()
    stay_count = len(results) - churn_count

    st.metric("Churn Rate", f"{churn_rate:.1f}%")
    st.metric("Churners", churn_count)
    st.metric("Non-Churners", stay_count)

    # Plots
# Smaller side-by-side dashboards
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn by Geography")
        fig, ax = plt.subplots(figsize=(4,3))
        sns.countplot(data=results, x="Geography", hue="Churn_Prediction", ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("Age Distribution by Churn")
        fig2, ax2 = plt.subplots(figsize=(4,3))
        sns.kdeplot(data=results, x="Age", hue="Churn_Prediction", fill=True, ax=ax2)
        st.pyplot(fig2)


import streamlit as st
import pandas as pd
import joblib

# Load model & threshold
model = joblib.load("models/churn_model.pkl")
with open("models/churn_threshold.txt", "r") as f:
    threshold = float(f.read().strip())

st.title("📊 Customer Churn Prediction App (Bank Dataset)")

st.write("Upload a CSV file with customer data (same structure as training dataset).")

# Upload CSV
uploaded_file = st.file_uploader("Upload customer data (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data")
    st.dataframe(data.head())

    # Predict churn probabilities
    probs = model.predict_proba(data)[:, 1]

    # Apply threshold
    preds = (probs >= threshold).astype(int)

    # Results
    results = data.copy()
    results["Churn_Probability"] = probs
    results["Churn_Prediction"] = preds

    st.write("### Predictions")
    st.dataframe(results)

    # Download predictions
    csv = results.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Predictions as CSV",
        data=csv,
        file_name="churn_predictions.csv",
        mime="text/csv"
    )

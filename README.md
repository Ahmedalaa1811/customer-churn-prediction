# 📊 Customer Churn Prediction App

This project is a **Streamlit web app** that predicts whether customers are likely to **churn (leave)** or **stay** based on their data.  
It was built using **scikit-learn, LightGBM, XGBoost, and RandomForest**, with the best tuned model saved and deployed.

---

## 🚀 Features
- 🔮 **Single Prediction** → form for one customer.  
- 📂 **Batch Prediction** → upload a CSV with customer data.  
- 📊 **Insights Dashboard** → compact graphs with **auto-generated insights**:  
  - Churn by Geography  
  - Churn by Age Distribution  
  - Churn by Gender  
  - Churn by Number of Products  
  - Churn by Tenure  
- 📥 **Downloadable Reports**:  
  - CSV with predictions  
  - PDF with metrics, charts, and top 10 high-risk customers  
- ☁️ **Deployable via Streamlit Cloud** or **Docker**  

---

## 📦 Installation

Clone this repository:
```bash
git clone https://github.com/Ahmedalaa1811/customer-churn-prediction.git
cd customer-churn-prediction
```

Install requirements:
```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally
```bash
streamlit run app.py
```

Then open in your browser:
```
http://localhost:8501
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push this repo to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io).  
3. Click **New App** → select your GitHub repo.  
4. Set the **entrypoint** to `app.py`.  
5. Add a **Secrets section** if you need environment variables (not required here).  
6. Click **Deploy** 🚀.  

Your app will be live at:  
```
https://customer-churn-prediction-rhq6ymdj5t3xkeqnab2qnm.streamlit.app/
```

---

## 📊 Example Input
```csv
CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary
619,France,Female,42,2,0.00,1,1,1,101348.88
608,Spain,Female,41,1,83807.86,1,0,1,112542.58
```

## 📊 Example Output
```csv
CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Churn_Probability,Churn_Prediction
619,France,Female,42,2,0.00,1,1,1,101348.88,0.82,1
608,Spain,Female,41,1,83807.86,1,0,1,112542.58,0.12,0
```

---

## 📷 Screenshots
### App Home  
![App Home](screenshots/app_home.png)

### Single Customer Prediction  
![Single Prediction](screenshots/single_prediction.png)

### Batch Predictions & Insights  
![Batch Predictions](screenshots/file_predictions.png)

### Dashboard with Insights  
![Dashboard](screenshots/dashboard.png)

---

## 🧪 Test It Yourself
Use the included [sample_customers.csv](sample_customers.csv) to try predictions instantly.
## 👨‍💻 Author
Built during **Data Science Diploma Project**.  
Contact: [LinkedIn](https://www.linkedin.com/in/ahmed-alaa-elsheikh-98a4b5182/) | [Email](mailto:ahmed.alaa181197@gmail.com)

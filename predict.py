import joblib
import pandas as pd

# Modeli yükle
model = joblib.load("telco_churn_pipeline.joblib")

# Örnek müşteri (EĞİTİMDE KULLANILAN KOLONLARIN AYNISI)
sample_customer = pd.DataFrame([{
    "Count": 1,
    "Latitude": 34.05,
    "Longitude": -118.24,
    "Tenure Months": 12,
    "Monthly Charges": 70.5,
    "Total Charges": 845.5,
    "CLTV": 3500,

    "Gender": "Female",
    "Senior Citizen": "No",
    "Partner": "Yes",
    "Dependents": "No",
    "Phone Service": "Yes",
    "Multiple Lines": "No",
    "Internet Service": "Fiber optic",
    "Online Security": "No",
    "Online Backup": "Yes",
    "Device Protection": "No",
    "Tech Support": "No",
    "Streaming TV": "Yes",
    "Streaming Movies": "Yes",
    "Contract": "Month-to-month",
    "Paperless Billing": "Yes",
    "Payment Method": "Electronic check"
}])

# Tahmin
prediction = model.predict(sample_customer)
probability = model.predict_proba(sample_customer)[0][1]

print("Churn Tahmini:", "Yes" if prediction[0] == 1 else "No")
print("Churn Olasılığı:", round(probability, 2))

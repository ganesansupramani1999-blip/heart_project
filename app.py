import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("heart_model.pkl")

st.title("❤️ Heart Disease Prediction App")

# Mode selector
mode = st.radio("Select Mode:", ["Patient Mode (Simple)", "Doctor Mode (Detailed)"])

if mode == "Patient Mode (Simple)":
    st.subheader("🧑‍⚕️ Patient Mode – Simple Inputs")

    age = st.number_input("Age", min_value=1, max_value=120, value=40)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Do you feel chest pain?", ["No", "Mild", "Moderate", "Severe"])
    trestbps = st.number_input("Resting Blood Pressure (if known)", min_value=50, max_value=250, value=120)
    chol = st.number_input("Cholesterol Level (if known)", min_value=100, max_value=600, value=200)

    # Map inputs to model values
    sex_val = 1 if sex == "Male" else 0
    cp_val = ["No", "Mild", "Moderate", "Severe"].index(cp)

    # Default values for missing features
    thalach = 150
    exang = 0
    oldpeak = 1.0
    slope = 1
    ca = 0
    thal = 2

    input_list = [age, sex_val, cp_val, trestbps, chol, thalach, exang, oldpeak, slope, ca, thal]

else:
    st.subheader("👨‍⚕️ Doctor Mode – Detailed Inputs")

    age = st.number_input("Age", min_value=1, max_value=120, value=40)
    sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=250, value=120)
    chol = st.number_input("Cholesterol Level", min_value=100, max_value=600, value=200)
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [1, 0])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (0–2)", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed, 3 = Reversible)", [1, 2, 3])

    input_list = [age, sex, cp, trestbps, chol, thalach, exang, oldpeak, slope, ca, thal]


# Prediction button
if st.button("🔍 Predict"):
    features = np.array([input_list], dtype=float)
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ The patient is at risk of Heart Disease.")
    else:
        st.success("✅ The patient is not at risk of Heart Disease.")

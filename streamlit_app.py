import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/car_service_model.pkl")

st.title("🚗 Car Service Prediction System")
st.info("Predict whether a car needs servicing using ML")

km = st.number_input("KM since last service", 0, 20000)
speed = st.number_input("Average speed (km/h)", 0, 120)
oil = st.number_input("KM since oil change", 0, 15000)
brake = st.number_input("Brake pad thickness (mm)", 0.0, 10.0)
clutch = st.number_input("Clutch pad thickness (mm)", 0.0, 10.0)
style = st.selectbox("Driving style", ["Smooth", "Aggressive"])

style = 0 if style == "Smooth" else 1

if st.button("Predict Service Requirement"):
    input_data = pd.DataFrame([[km, speed, oil, brake, clutch, style]],
        columns=[
            "km_since_last_service",
            "avg_speed_kmph",
            "engine_oil_km",
            "brake_pad_thickness_mm",
            "clutch_pad_thickness_mm",
            "driving_style"
        ]
    )

    result = model.predict(input_data)[0]

    if result == 1:
        st.error("🔧 Service Required")
    else:
        st.success("✅ No Service Needed")

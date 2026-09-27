import streamlit as st
import joblib
import pandas as pd


# Load the trained model
model = joblib.load("salary_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="centered"
)


# Title and introduction
st.title("💼 Salary Prediction App")

st.write(
    "Enter your years of professional experience below "
    "to get an estimated salary based on our machine learning model."
)


# User input
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)


# Prediction button
if st.button("Predict Salary"):

    input_data = pd.DataFrame(
        {"Experience Years": [experience]}
    )

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Salary: {prediction:,.0f}"
    )
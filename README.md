# Salary Prediction App

This project predicts salary based on years of professional experience using a machine learning model.

I used a salary dataset, trained a Linear Regression model, and built a Streamlit app where users can enter their experience and get an estimated salary.

## Model

Linear Regression

## Evaluation

The model was evaluated using the test data.

- MAE: 4,056.34
- MSE: 23,745,684.25
- RMSE: 4,872.95
- R² Score: 0.9831

## Dataset

Salary Dataset provided for the Machine Learning assignment.

## What I used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Files

- `app.py` – Streamlit application
- `salary_dataset.csv` – dataset used for the project
- `salary_model.pkl` – trained model
- `Salary_Prediction_ML_ProjectMalaikaKhan.ipynb` – model training and evaluation
- `requirements.txt` – required Python libraries
- `.gitignore` – files excluded from Git

## How it works

The user enters their years of professional experience and clicks **Predict Salary**. The app loads the trained model and gives an estimated salary.

## Live App

[Salary Prediction App](https://salary-prediction-app-89avgi6xupgwdahayxwvp2.streamlit.app/)

import streamlit as st
import pandas as pd
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("columns.pkl", "rb") as f:
    columns = pickle.load(f)

st.title("🏠 Loan Prediction App")

st.write("Enter details to predict target value")

city = st.selectbox("City", ["Hyderabad", "Chennai", "Bangalore"])
employment_type = st.selectbox("Employment Type", ["Salaried", "Self-employed"])
loan_type = st.selectbox("Loan Type", ["Home", "Personal"])

income = st.number_input("Income", value=50000)
age = st.number_input("Age", value=30)

input_dict = {
    "income": income,
    "age": age
}

input_df = pd.DataFrame([input_dict])

input_df = pd.get_dummies(input_df)

for col in columns:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[columns]

if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Value: {prediction[0]:.2f}")

import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("BikeRental_Model.pkl")

# Load Feature Names
feature_columns = joblib.load("feature_columns.pkl")

st.title("🚲 Bike Rental Demand Prediction")

st.write("Enter the feature values below.")

user_input = {}

for feature in feature_columns:

    user_input[feature] = st.number_input(
        feature,
        value=0.0
    )

input_df = pd.DataFrame([user_input])

prediction = model.predict(input_df)

st.subheader("Predicted Bike Rentals")

st.success(f"{prediction[0]:.2f}")

import streamlit as st
import joblib
import pandas as pd
import sklearn

# Load the model
model = joblib.load('crop_recommendation_model.pkl')  # Use the correct file name

# Title of the app
st.title("Crop Recommendation System")

# Input fields for user
st.header("Enter Soil and Weather Conditions")
N = st.number_input("Nitrogen (N)", min_value=0, max_value=140)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=145)
K = st.number_input("Potassium (K)", min_value=0, max_value=205)
temperature = st.number_input("Temperature (°C)", min_value=8.0, max_value=43.0)
humidity = st.number_input("Humidity (%)", min_value=14.0, max_value=99.0)
ph = st.number_input("Soil pH", min_value=3.5, max_value=9.9)
rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=298.0)

# Predict button
if st.button("Recommend Crop"):
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    input_df = pd.DataFrame(input_data, columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    prediction = model.predict(input_df)
    st.success(f"Recommended Crop: {prediction[0]}")
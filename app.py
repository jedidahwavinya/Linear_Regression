
#!pip install streamlit
import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# App title
st.title("🚗 Car Price Prediction App")

st.write("Fill in the details below to predict the car price.")

st.header("Enter Car Details:")

# Create input fields for each feature
year = st.number_input("Year", min_value=1980, max_value=2024, value=2015)
km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG'])
seller_type = st.selectbox("Seller Type", ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])
owner = st.selectbox("Owner Type", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
mileage = st.number_input("Mileage (km/ltr/kg)", min_value=0.0, value=18.0)
engine = st.number_input("Engine (CC)", min_value=0.0, value=1200.0)
max_power = st.number_input("Max Power (bhp)", min_value=0.0, value=80.0)
seats = st.number_input("Number of Seats", min_value=1.0, value=5.0)

# Create a button to trigger prediction
if st.button("Predict Price"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'year': [year],
        'km_driven': [km_driven],
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner],
        'mileage(km/ltr/kg)': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'seats': [seats]
    })

    # Apply preprocessing to the input data
    input_data_processed = preprocessing_pipeline.transform(input_data)

    # Make a prediction
    predicted_price = model.predict(input_data_processed)

    # Display the prediction
    st.subheader("Predicted Selling Price:")
    st.write(f"₹ {predicted_price[0]:,.2f}")

import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("House Price Prediction")

size = st.number_input("Enter house size")

if st.button("Predict"):
    prediction = model.predict(np.array([[size]]))
    st.success(f"Predicted price: {prediction[0]}")

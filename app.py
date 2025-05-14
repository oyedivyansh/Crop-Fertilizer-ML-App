import streamlit as st
import joblib
import pandas as pd

# Load models
crop_model = joblib.load("crop_model.pkl")
fertilizer_model = joblib.load("fertilizer_model.pkl")

st.set_page_config(page_title="Crop & Fertilizer Recommender", layout="centered")
st.title("🌱 Crop & Fertilizer Recommendation System")

tab1, tab2 = st.tabs(["🌾 Crop Recommendation", "💊 Fertilizer Recommendation"])

with tab1:
    st.header("Crop Recommendation")
    N = st.slider("Nitrogen (N)", 0, 140, 50)
    P = st.slider("Phosphorus (P)", 5, 145, 50)
    K = st.slider("Potassium (K)", 5, 205, 50)
    temperature = st.number_input("Temperature (°C)", 0.0, 60.0, 25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 50.0)
    ph = st.number_input("pH", 0.0, 14.0, 6.5)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, 100.0)

    if st.button("🔍 Recommend Crop"):
        input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                                  columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"])
        try:
            prediction = crop_model.predict(input_data)

            # Correct crop list (1-based index from model)
            crop_labels = [
                "rice", "maize", "chickpea", "kidneybeans", "pigeonpeas", "mothbeans", "mungbean", "blackgram",
                "lentil", "pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "apple",
                "orange", "papaya", "coconut", "cotton", "jute", "coffee"
            ]

            predicted_crop = crop_labels[prediction[0] - 1]  # -1 because list is 0-indexed
            st.success(f"✅ Recommended Crop: **{predicted_crop.capitalize()}**")
        except Exception as e:
            st.error(f"🚨 Error: {e}")

with tab2:
    st.header("Fertilizer Recommendation")
    crop_options = ["rice", "wheat", "maize", "sugarcane", "cotton", "millets", "barley"]
    crop_name = st.selectbox("Select Crop", crop_options)
    N = st.slider("Nitrogen Level (N)", 0, 140, 50, key="fn")
    P = st.slider("Phosphorus Level (P)", 5, 145, 50, key="fp")
    K = st.slider("Potassium Level (K)", 5, 205, 50, key="fk")

    if st.button("🔍 Recommend Fertilizer"):
        input_data = pd.DataFrame([[crop_name, N, P, K]], columns=["Crop", "N", "P", "K"])
        try:
            prediction = fertilizer_model.predict(input_data)
            st.success(f"✅ Recommended Fertilizer: **{prediction[0]}**")
        except Exception as e:
            st.error(f"🚨 Error: {e}")

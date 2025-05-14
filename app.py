import streamlit as st
import joblib
import pandas as pd

# Load models
crop_model = joblib.load("crop_model.pkl")
fertilizer_model = joblib.load("fertilizer_model.pkl")

# Crop dictionary (ID to name)
crop_dict = {
    1: "rice",
    2: "maize",
    3: "chickpea",
    4: "kidneybeans",
    5: "pigeonpeas",
    6: "mothbeans",
    7: "mungbean",
    8: "blackgram",
    9: "lentil",
    10: "pomegranate",
    11: "banana",
    12: "mango",
    13: "grapes",
    14: "watermelon",
    15: "muskmelon",
    16: "apple",
    17: "orange",
    18: "papaya",
    19: "coconut",
    20: "cotton",
    21: "jute",
    22: "coffee"
}

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
        st.write("📥 Input Data:", input_data)
        try:
            prediction = crop_model.predict(input_data)
            predicted_class = int(prediction[0])
            predicted_crop = crop_dict.get(predicted_class, "Unknown")
            st.success(f"✅ Recommended Crop: **{predicted_crop.capitalize()}**")
        except Exception as e:
            st.error(f"🚨 Error during prediction: {e}")

with tab2:
    st.header("Fertilizer Recommendation")

    crop_options = ["rice", "wheat", "maize", "sugarcane", "cotton", "millets", "barley"]
    crop_name = st.selectbox("Select Crop", crop_options)
    fn = st.slider("Nitrogen Level (N)", 0, 140, 50, key="fn")
    fp = st.slider("Phosphorus Level (P)", 5, 145, 50, key="fp")
    fk = st.slider("Potassium Level (K)", 5, 205, 50, key="fk")

    if st.button("🔍 Recommend Fertilizer"):
        input_data = pd.DataFrame([[crop_name, fn, fp, fk]], columns=["Crop", "N", "P", "K"])
        st.write("📥 Input Data:", input_data)
        try:
            prediction = fertilizer_model.predict(input_data)
            st.success(f"✅ Recommended Fertilizer: **{prediction[0]}**")
        except Exception as e:
            st.error(f"🚨 Error during prediction: {e}")

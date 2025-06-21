import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from app.predictor import predict
from app.explainer import explain_prediction

# Page config
st.set_page_config(page_title="PulseAI — Heart Rhythm Screener", page_icon="🫀", layout="centered")

# Inject background CSS
st.markdown("""
    <style>
        .stApp {
            background-image: url("ui/assets/bg.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .title {
            text-align: center;
            color: #fff;
            font-size: 40px;
            margin-bottom: 0;
        }
        .subtitle {
            text-align: center;
            color: #ddd;
            font-size: 18px;
        }
        .footer {
            text-align: center;
            color: #aaa;
            font-size: 12px;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Logo + Title
st.image("ui/assets/logo.png", width=120)
st.markdown("<h1 class='title'>PulseAI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Heart Rhythm Screener — Upload your ECG</p>", unsafe_allow_html=True)

# Upload ECG file
uploaded_file = st.file_uploader("📤 Upload ECG CSV (.csv or .txt)", type=["csv", "txt"])

if uploaded_file:
    try:
        data = np.loadtxt(uploaded_file, delimiter=",")
        if len(data.shape) == 2:
            data = data[:, 0]
        if len(data) < 360:
            st.error("❌ ECG signal must be at least 360 samples.")
            st.stop()

        st.success("✅ ECG file loaded successfully!")
        st.line_chart(data[:500])

        sample = data[:360].reshape(1, 360, 1).astype("float32")
        prediction = predict(sample)
        explanation = explain_prediction(prediction)

        st.markdown(f"### 🩺 Prediction: <span style='color: limegreen; font-size: 22px;'>`{prediction}`</span>", unsafe_allow_html=True)
        st.markdown(f"**🧠 Model Explanation:** {explanation}")
    except Exception as e:
        st.error(f"❌ Error reading ECG file: `{e}`")
else:
    st.info("Upload a single-column `.csv` or `.txt` file with ECG data.")

st.markdown("<div class='footer'>Made with ❤️ by PulseAI</div>", unsafe_allow_html=True)

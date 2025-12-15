import streamlit as st
import numpy as np
from PIL import Image
import onnxruntime as ort
import requests
import os

from data.descriptions import DESCRIPTIONS   


st.set_page_config(
    page_title="Prediction Machine",
    page_icon="🌿",
    layout="wide"
)

with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    url = "https://drive.google.com/uc?export=download&id=1KKrqA_xJI_NJcajcjMTJXTcg_7c2x6aQ"
    file = "model.onnx"

    if not os.path.exists(file):
        r = requests.get(url)
        open(file, "wb").write(r.content)

    return ort.InferenceSession(file)

session = load_model()


class_names = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy',
]


IMG_SIZE = 160


st.markdown("<h1 class='title-main'>🌿 Leafy AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Plant Disease Classifier (ONNX Optimized)</p>", unsafe_allow_html=True)


uploaded = st.file_uploader("Upload leaf image", type=["jpg", "jpeg", "png"])

if uploaded:
    col1, col2 = st.columns([1, 1])

    with col1:
        img = Image.open(uploaded).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img_resized = img.resize((IMG_SIZE, IMG_SIZE))
    arr = np.array(img_resized).astype("float32") / 255.0
    arr = np.expand_dims(arr, axis=0)

    inputs = {session.get_inputs()[0].name: arr}
    preds = session.run(None, inputs)[0][0]

    idx = np.argmax(preds)
    class_raw = class_names[idx]          # nama raw, sesuai description.py
    pretty = class_raw.replace("___", " — ").replace("_", " ")
    confidence = preds[idx] * 100


    description = DESCRIPTIONS.get(class_raw, "No description available.")

    with col2:
        # MAIN RESULT CARD
        st.markdown(f"""
        <div class='main-card'>
            <div class='pred-title'>{pretty}</div>
            <div class='pred-sub'>Confidence: {confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='main-card'>
            <h3 style='color:white; margin-bottom:8px;'>📘 Description</h3>
            <p style='color:#d4d4d4; font-size:16px;'>{description}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='top5-title'>Top 5 Predictions</div>", unsafe_allow_html=True)

        top5_idx = preds.argsort()[::-1][:5]
        for i in top5_idx:
            pretty_i = class_names[i].replace("___", " — ").replace("_", " ")
            st.markdown(
                f"""
                <div class='top5-card'>
                    <div class='top5-label'>{pretty_i}</div>
                    <div class='top5-conf'>{preds[i]*100:.2f}%</div>
                </div>
                """,
                unsafe_allow_html=True
            )

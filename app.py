import streamlit as st
import numpy as np
from PIL import Image
import onnxruntime as ort

st.set_page_config(page_title="Leafy — Plant Disease AI", layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return ort.InferenceSession("model.onnx")

session = load_model()

class_names = [
    'Apple — Apple scab',
    'Apple — Black rot',
    'Apple — Cedar apple rust',
    'Apple — Healthy',
    'Blueberry — Healthy',
    'Cherry — Powdery mildew',
    'Cherry — Healthy',
    'Corn — Cercospora',
    'Corn — Common rust',
    'Corn — Northern leaf blight',
    'Corn — Healthy',
    'Grape — Black rot',
    'Grape — Black measles',
    'Grape — Leaf blight',
    'Grape — Healthy',
    'Orange — Citrus greening',
    'Peach — Bacterial spot',
    'Peach — Healthy',
    'Pepper — Bacterial spot',
    'Pepper — Healthy',
    'Potato — Early blight',
    'Potato — Late blight',
    'Potato — Healthy',
    'Raspberry — Healthy',
    'Soybean — Healthy',
    'Squash — Powdery mildew',
    'Strawberry — Leaf scorch',
    'Strawberry — Healthy',
    'Tomato — Bacterial spot',
    'Tomato — Early blight',
    'Tomato — Late blight',
    'Tomato — Leaf mold',
    'Tomato — Septoria',
    'Tomato — Spider mites',
    'Tomato — Target spot',
    'Tomato — YLCV',
    'Tomato — Mosaic virus',
    'Tomato — Healthy',
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
    img2 = img.resize((IMG_SIZE, IMG_SIZE))
    arr = np.array(img2).astype("float32") / 255.0
    arr = np.expand_dims(arr, axis=0)

    inputs = {session.get_inputs()[0].name: arr}
    preds = session.run(None, inputs)[0][0]

    idx = np.argmax(preds)
    confidence = preds[idx] * 100

    with col2:
        st.markdown(f"""
        <div class='main-card'>
            <div class='pred-title'>{class_names[idx]}</div>
            <div class='pred-sub'>Confidence: {confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='top5-title'>Top 5 Predictions</div>", unsafe_allow_html=True)

        top5_idx = preds.argsort()[::-1][:5]
        for i in top5_idx:
            st.markdown(
                f"""
                <div class='top5-card'>
                    <div class='top5-label'>{class_names[i]}</div>
                    <div class='top5-conf'>{preds[i]*100:.2f}%</div>
                </div>
                """,
                unsafe_allow_html=True
            )


import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="PlantScope AI",
    page_icon="🌿",
    layout="wide"
)

with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("densenet_best.h5")

model = load_model()

IMG_SIZE = 160

st.markdown("<h1 class='title'>🌿 PlantScope AI</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])

if uploaded_file:
    col1, col2 = st.columns([1,1])
    with col1:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

    img_resized = img.resize((IMG_SIZE, IMG_SIZE))
    arr = np.expand_dims(np.array(img_resized)/255.0, 0)
    pred = model.predict(arr)

    idx = np.argmax(pred)
    confidence = pred[0][idx] * 100

    class_names = [...]
    def pretty(c): return c.replace("___"," — ").replace("_"," ")
    with col2:
        st.markdown(f"""
        <div class='card'>
            <div class='pred-label'>{pretty(class_names[idx])}</div>
            <div class='confidence'>Confidence: {confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    # Top-5 bar chart
    top_k = 5
    indices = np.argsort(pred[0])[::-1][:top_k]
    labels = [pretty(class_names[i]) for i in indices]
    probs = pred[0][indices]

    fig = px.bar(
        x=probs,
        y=labels,
        orientation='h',
        color=probs
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#e0e0e0"
    )
    st.plotly_chart(fig, use_container_width=True)

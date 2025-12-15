import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

st.set_page_config(
    page_title="Leafy — Plant Disease AI",
    page_icon="🌱",
    layout="wide"
)

with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("densenet_best.h5")

model = load_model()

IMG_SIZE = 160

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

def clean_label(name):
    return name.replace("___", " — ").replace("_", " ")

st.sidebar.markdown("""
<div class='sidebar-title'>🌱 LEAFY</div>
<div class='sidebar-sub'>Plant Disease AI Scanner</div>
<hr style='border:1px solid #666'>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-main'>🌿 Leafy — Plant Disease Classifier</h1>", unsafe_allow_html=True)
st.write("<p class='subtitle'>Upload gambar daun dan Leafy akan mendeteksi penyakitnya.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload leaf image", type=["jpg","jpeg","png"])

if uploaded_file:
    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

    img_r = img.resize((IMG_SIZE, IMG_SIZE))
    arr = np.expand_dims(np.array(img_r)/255.0, 0)
    pred = model.predict(arr)

    idx = np.argmax(pred)
    confidence = pred[0][idx] * 100
    label = clean_label(class_names[idx])

    with col2:
        st.markdown(f"""
        <div class="main-card">
            <div class="pred-title">{label}</div>
            <div class="pred-sub">Confidence: {confidence:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='top5-title'>Top 5 Predictions</div>", unsafe_allow_html=True)

        top_idx = np.argsort(pred[0])[::-1][:5]

        for i in top_idx:
            st.markdown(f"""
            <div class="top5-card">
                <div class="top5-label">{clean_label(class_names[i])}</div>
                <div class="top5-conf">{pred[0][i]*100:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)

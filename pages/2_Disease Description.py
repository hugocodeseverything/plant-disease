import streamlit as st

st.set_page_config(page_title="Disease Description", page_icon="📘")

st.title("📘 Plant Disease Description")
st.write("Penjelasan lengkap untuk setiap class yang digunakan model DenseNet121.")


st.markdown("""
<style>
.accordion {
    background: #1b1f27;
    padding: 16px;
    border-radius: 10px;
    margin-bottom: 10px;
    box-shadow: 0 0 20px rgba(0,255,200,0.10);
}
.label {
    font-size: 20px;
    font-weight: 700;
    color: #86e1ff;
}
.desc {
    font-size: 15px;
    color: #d4d4d4;
}
</style>
""", unsafe_allow_html=True)


# ===== DESCRIPTION DATABASE =====
DESCRIPTIONS = {

    "Apple___Apple_scab": {
        "Symptoms": "Bercak coklat zaitun pada daun dan buah. Daun bisa melengkung dan berubah warna.",
        "Cause": "Jamur *Venturia inaequalis*. Menyukai kondisi lembab.",
        "Treatment": "Potong daun terinfeksi, gunakan fungisida sulfur atau captan."
    },

    "Apple___Black_rot": {
        "Symptoms": "Daun memiliki bercak coklat konsentris. Buah membusuk menjadi hitam.",
        "Cause": "Jamur *Botryosphaeria obtusa*.",
        "Treatment": "Buang buah/ranting terinfeksi dan lakukan sanitasi kebun."
    },

    "Apple___Cedar_apple_rust": {
        "Symptoms": "Bercak oranye terang. Kadang ada 'tanduk' gelatinous di musim hujan.",
        "Cause": "Jamur *Gymnosporangium juniperi-virginianae*. Butuh cedar sebagai host kedua.",
        "Treatment": "Jaga jarak dari pohon cedar, gunakan fungisida protektif."
    },

    "Apple___healthy": {
        "Symptoms": "Daun hijau segar tanpa bercak.",
        "Cause": "—",
        "Treatment": "Tanaman dalam kondisi optimal."
    },

    "Blueberry___healthy": {
        "Symptoms": "Daun hijau cerah, tidak ada perubahan warna.",
        "Cause": "—",
        "Treatment": "Tidak diperlukan."
    },

    "Cherry_(including_sour)___Powdery_mildew": {
        "Symptoms": "Lapisan putih seperti bedak pada daun dan batang.",
        "Cause": "Jamur *Podosphaera clandestina*.",
        "Treatment": "Kontrol kelembaban, gunakan fungisida berbasis sulfur."
    },

    "Cherry_(including_sour)___healthy": {
        "Symptoms": "Daun mengkilap hijau tua.",
        "Cause": "—",
        "Treatment": "Tidak ada tindakan."
    },

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "Symptoms": "Bercak panjang kelabu dengan tepi kuning.",
        "Cause": "Jamur *Cercospora zeae-maydis*.",
        "Treatment": "Rotasi tanaman dan fungisida preventif."
    },

    "Corn_(maize)___Common_rust_": {
        "Symptoms": "Pustula berwarna merah karat di daun.",
        "Cause": "Jamur *Puccinia sorghi*.",
        "Treatment": "Gunakan varietas tahan dan fungisida."
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "Symptoms": "Lesi panjang fusiform, coklat keabu-abuan.",
        "Cause": "Jamur *Exserohilum turcicum*.",
        "Treatment": "Fungisida dan varietas tahan."
    },

    "Corn_(maize)___healthy": {
        "Symptoms": "Daun panjang hijau simetris.",
        "Cause": "—",
        "Treatment": "Tidak diperlukan."
    },

    "Grape___Black_rot": {
        "Symptoms": "Buah mengering dan menghitam seperti mumi.",
        "Cause": "Jamur *Guignardia bidwellii*.",
        "Treatment": "Buang buah mumi dan gunakan fungisida."
    },

    "Grape___Esca_(Black_Measles)": {
        "Symptoms": "Bercak gelap seperti 'measles' di daun.",
        "Cause": "Kompleks jamur trunk disease.",
        "Treatment": "Pruning area mati dan perbaiki drainase."
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "Symptoms": "Bercak sudut-sudut (angular spots) pada daun.",
        "Cause": "Jamur *Isariopsis*.",
        "Treatment": "Pemangkasan dan fungisida rutin."
    },

    "Grape___healthy": {
        "Symptoms": "Daun besar hijau tebal.",
        "Cause": "—",
        "Treatment": "Tidak perlu tindakan."
    },

    "Orange___Haunglongbing_(Citrus_greening)": {
        "Symptoms": "Daun menguning tidak merata, buah kecil dan pahit.",
        "Cause": "Bakteri *Candidatus Liberibacter*. Menular via kutu psyllid.",
        "Treatment": "Tidak ada obat total. Kontrol vektor dan cabut pohon parah."
    },

    "Peach___Bacterial_spot": {
        "Symptoms": "Spot kecil seperti pecahan peluru (shot-hole).",
        "Cause": "Bakteri *Xanthomonas arboricola*.",
        "Treatment": "Semprotan tembaga dan pengelolaan kelembaban."
    },

    "Peach___healthy": {
        "Symptoms": "Daun halus hijau cerah.",
        "Cause": "—",
        "Treatment": "Tidak perlu tindakan."
    },

    "Pepper,_bell___Bacterial_spot": {
        "Symptoms": "Lesi gelap berair yang berubah menjadi bercak coklat.",
        "Cause": "Bakteri *Xanthomonas campestris*.",
        "Treatment": "Rotasi, sanitasi, dan fungisida tembaga."
    },

    "Pepper,_bell___healthy": {
        "Symptoms": "Daun tebal hijau tua.",
        "Cause": "—",
        "Treatment": "Tanaman sehat."
    },

    "Potato___Early_blight": {
        "Symptoms": "Cincin konsentris seperti target (bullseye).",
        "Cause": "Jamur *Alternaria solani*.",
        "Treatment": "Fungisida rutin dan rotasi tanaman."
    },

    "Potato___Late_blight": {
        "Symptoms": "Daun coklat kehitaman, lembek. Penyakit paling mematikan kentang.",
        "Cause": "Oomycete *Phytophthora infestans*.",
        "Treatment": "Fungisida sistemik dan sanitasi ketat."
    },

    "Potato___healthy": {
        "Symptoms": "Daun oval lebar hijau penuh.",
        "Cause": "—",
        "Treatment": "Tidak perlu aksi."
    },

    "Raspberry___healthy": {
        "Symptoms": "Daun berkerut alami tapi sehat.",
        "Cause": "—",
        "Treatment": "Tidak ada tindakan."
    },

    "Soybean___healthy": {
        "Symptoms": "Daun simetris di tiap node.",
        "Cause": "—",
        "Treatment": "Tanaman sehat."
    },

    "Squash___Powdery_mildew": {
        "Symptoms": "Lapisan putih tipis di atas daun.",
        "Cause": "Jamur *Erysiphe cichoracearum*.",
        "Treatment": "Kurangi kelembaban + fungisida sulfur."
    },

    "Strawberry___Leaf_scorch": {
        "Symptoms": "Bercak merah kecoklatan kecil di daun.",
        "Cause": "Jamur *Diplocarpon earlianum*.",
        "Treatment": "Buang daun terinfeksi dan kontrol kelembaban."
    },

    "Strawberry___healthy": {
        "Symptoms": "Daun tiga-lobus hijau cerah.",
        "Cause": "—",
        "Treatment": "Tidak perlu tindakan."
    },

    "Tomato___Bacterial_spot": {
        "Symptoms": "Bercak basah kecil lalu mengering hitam.",
        "Cause": "Bakteri *Xanthomonas*.",
        "Treatment": "Semprotan tembaga dan sanitasi."
    },

    "Tomato___Early_blight": {
        "Symptoms": "Cincin konsentris 'bullseye' klasik di daun.",
        "Cause": "Jamur *Alternaria solani*.",
        "Treatment": "Fungisida rutin."
    },

    "Tomato___Late_blight": {
        "Symptoms": "Daun hitam cepat menyebar, penyakit paling destruktif.",
        "Cause": "Oomycete *Phytophthora infestans*.",
        "Treatment": "Fumigasi & fungisida sistemik."
    },

    "Tomato___Leaf_Mold": {
        "Symptoms": "Lapisan mold kuning–hijau di bawah daun.",
        "Cause": "Jamur *Passalora fulva*.",
        "Treatment": "Perbaiki ventilasi greenhouse."
    },

    "Tomato___Septoria_leaf_spot": {
        "Symptoms": "Bercak kecil bundar seragam.",
        "Cause": "Jamur *Septoria lycopersici*.",
        "Treatment": "Sanitasi & fungisida protektif."
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "Symptoms": "Bintik halus + jaring tipis.",
        "Cause": "Tungau laba-laba dua titik.",
        "Treatment": "Akarisida & kontrol suhu."
    },

    "Tomato___Target_Spot": {
        "Symptoms": "Bercak bulat coklat dengan tepi gelap.",
        "Cause": "Jamur *Corynespora cassiicola*.",
        "Treatment": "Fungisida sesuai rekomendasi lokal."
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "Symptoms": "Daun menguning dan melengkung ke atas.",
        "Cause": "Virus TYLCV, disebarkan whiteflies.",
        "Treatment": "Kontrol kutu kebul intensif."
    },

    "Tomato___Tomato_mosaic_virus": {
        "Symptoms": "Sering muncul pola mosaik kuning–hijau.",
        "Cause": "TMV — salah satu virus paling tahan lama.",
        "Treatment": "Sanitasi maksimal, buang tanaman terinfeksi."
    },

    "Tomato___healthy": {
        "Symptoms": "Daun hijau segar seragam.",
        "Cause": "—",
        "Treatment": "Tidak perlu tindakan."
    },
}


for cls, info in DESCRIPTIONS.items():
    pretty = cls.replace("___", " — ").replace("_", " ")
    with st.expander(pretty):
        st.markdown(f"<div class='desc'><b>Symptoms:</b> {info['Symptoms']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'><b>Cause:</b> {info['Cause']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='desc'><b>Treatment:</b> {info['Treatment']}</div>", unsafe_allow_html=True)

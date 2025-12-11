**Plant Disease Detection Project**

**Member Of The Group:**
- Hugo Sachio Wijaya (2702261151) (Main Contributor)

  Tugas:

  -Membuat Model Densenet, Training, dan Validasi

  -Membuat app.py

  -Membuat file requirements

  -Menulis readme.md
  
- Erick Susanto (2702277710)

(Side Contributor -> menentukan ide, membantu programming)

- Ergi Hendrarto Putra (2702351696)

(Side Contributor -> menentukan ide, membantu programming)

**1.Pembukaan**

  Project ini adalah projek yang berisi sistem kasifikasi penyakit tanaman menggunakan
  model deeplearning CNN pre-trained DenseNet121. Dataset yang digunakan berasal dari
  Website Kaggle https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset.
  Data yang kami gunakan terdiri dari 38 kelas, baik itu tanaman yang sakit maupun yang
  sehat dan terdiri dari 87.000 images. Model kami dilatih dengan DenseNet dengan akurasi
  sebesar 93% yang kami tingkatkan lagi menggunakan finetuning dan akurasinya menjadi sebesar
  95%. Model ini dilatih menggunakan transfer learning dan finetuning dan hasil akhirnya
  kami letakkan di streamlit agar bisa langsung digunakan menggunakan streamlit.

**2.Project Structure**

│

├── app.py                     
├── densenet121_plant_disease.h5

├── deep_learning_project_final.py   
├── README.md              
├── .gitignore   
└── requirements.txt

**3. Dataset**
   
  Dataset kami menggunakan New Plant Disease Dataset (Augmented) dari Kaggle
  Isinya 38 kelas tanaman berpenyakit dan tanaman yang tidak sehat.
  Struktur dataset:
  train/
  valid/
  test/

**4.Model Architecture:**

DenseNet121 (pretrained ImageNet)
Global Average Pooling
Dense 256 (ReLU)
Dropout 0.3
Output Softmax (38 kelas)

**1. Transfer Learning**
Base model frozen
LR = 1e−3
Epoch = 10

**2. Fine Tuning**
80 layer terakhir dibuka (trainable)
LR = 1e−5
Epoch = 5
Callbacks:

ModelCheckpoint

EarlyStopping

ReduceLROnPlateau

**5. Cara menjalankan**

Pada streamlit, yang perlu dilakukan hanyalah memasukan gambar tanaman
berupa file jpeg, jpg, atau png dan klik run dan akan tertera confident rate
dan nama penyakit tanaman atau tanaman sehat.

**6.Fitur yang tersedia**

Fitur:
Upload gambar

Real-time prediction

Menampilkan kelas & confidence

Model inference cepat menggunakan DenseNet121

**7.License**

Bebas dipakai oleh siapapun, tidak perlu credit apapun, hanya tugas kuliah, Open License

**8.Cara Deploy To SreamLit**

Deploy ke https://share.streamlit.io

Langkah-langkah:

1. Login Streamlit Cloud

https://share.streamlit.io

Pilih "Continue with GitHub".

2. Klik "New app"

Di dashboard → klik New app.

3. Pilih repo

Repository: hugocodeseverything/plant-disease

Branch: main

Main file: app.py

4. Deploy

Klik Deploy → Streamlit akan mulai build environment berdasarkan requirements.txt.

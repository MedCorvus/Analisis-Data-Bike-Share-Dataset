# Proyek Analisis Data - Dicoding (BIKE SHARING DATASET)

## Deskripsi
Proyek ini merupakan bagian dari persyaratan kelulusan kursus **"Belajar Analisis Data Dengan Python"** di Dicoding. Pada proyek ini, analisis data dilakukan dengan menggunakan Python dan alat-alat analitik lain, serta hasilnya ditampilkan melalui dashboard interaktif menggunakan Streamlit.

## Struktur Direktori
Berikut adalah struktur direktori proyek ini:

- `/dashboard`: 
  - **dashboard.py**: File Python untuk menjalankan dashboard Streamlit.
  - **cleaned_dataset.csv**: Dataset yang telah dibersihkan dan digunakan untuk analisis lebih lanjut.
  - **image/**: Folder berisi gambar yang digunakan di dalam dashboard, seperti gambar tanggal atau visual lain.
  
- `/data`: 
  - Folder ini berisi dataset mentah yang digunakan untuk analisis data.

- **ProyekAnalisisData.ipynb**: File Jupyter Notebook (dijalankan di Google Colab) yang berisi langkah-langkah analisis data, mulai dari pembersihan data hingga visualisasi.

- **README.md**: File ini berisi deskripsi proyek dan cara menjalankannya.

- **requirements.txt**: File ini berisi daftar library yang digunakan dalam proyek ini untuk memudahkan penginstalan.

- **url.txt**: Berisi URL untuk mengakses dashboard Streamlit yang sudah di-hosting.

## Cara Menjalankan Dashboard Streamlit
Untuk menjalankan dashboard Streamlit secara lokal, ikuti langkah-langkah berikut:

1. Pastikan semua library yang diperlukan sudah terinstal. Jika belum, jalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
streamlit run dashboard/dashboard.py

Library yang Digunakan
Beberapa library yang digunakan dalam proyek ini, di antaranya:

Pandas
NumPy
Matplotlib
Seaborn
Streamlit

URL Dashboard
Jika Anda ingin melihat dashboard tanpa menjalankannya secara lokal, silakan kunjungi URL berikut: https://ridho-nur-fauzi-bike-share-dataset.streamlit.app/
# Flask Project - Cek Umur dan Fakta Teknologi

Proyek ini menggunakan framework Flask untuk membuat aplikasi web yang memiliki dua fitur utama:
1. **Cek Umur**: Menghitung umur pengguna berdasarkan tahun lahir yang dimasukkan.
2. **Fakta Teknologi**: Menampilkan fakta menarik tentang teknologi pada tahun yang dimasukkan, menggunakan API Key Groq.

## Fitur
- **Halaman Utama**: Halaman utama aplikasi dengan tautan ke halaman cek umur.
- **Halaman About**: Menyediakan informasi tentang proyek ini.
- **Halaman Hitung Umur**: Pengguna dapat memasukkan tahun lahir untuk menghitung umur mereka dan mendapatkan fakta teknologi yang relevan.

## Screenshot

### 1. **Halaman Utama**
![Halaman Utama](https://github.com/user-attachments/assets/0040abe0-29a2-47a3-b123-f8884d2f20c4)

### 2. **Halaman About**
![Halaman About](https://github.com/user-attachments/assets/1c08bf66-9f81-4ef4-93d7-571d0d2065c2)

### 3. **Halaman Hitung Umur**
![Halaman Hitung Umur](https://github.com/user-attachments/assets/4fc9b672-5ba6-48b1-a4ef-104b2b22dc25)

## Cara Menjalankan Proyek

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/username/project-flask.git
   ```

2. **Install dependencies**:
   Pastikan Anda telah menginstal Python dan pip. Kemudian, install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**:
   Setelah dependensi terpasang, jalankan aplikasi dengan perintah:
   ```bash
   python app.py
   ```

4. Akses aplikasi melalui browser di `http://127.0.0.1:5000/`.

## Struktur Folder
```
/project-flask
│── app.py               # File utama aplikasi Flask
│── templates/           # Folder untuk template HTML
│   ├── index.html
│   ├── about.html
│   ├── cek_usia.html
│── static/              # Folder untuk file CSS
│   ├── style.css
│── requirements.txt     # File dependencies
```

## Teknologi yang Digunakan
- **Flask**: Web framework untuk Python
- **Groq API**: Untuk mendapatkan fakta menarik teknologi berdasarkan tahun
- **HTML/CSS**: Untuk membangun dan mendesain antarmuka pengguna

## Pengaturan API Key
Sebelum menggunakan fitur API untuk mendapatkan fakta teknologi, Anda perlu menambahkan **API Key Groq** di dalam kode:

1. **Buka file `app.py`**.
2. Temukan bagian kode berikut:
   ```python
   AI_KEY = "YOUR_API_KEY_HERE"
   ```
3. Ganti `"YOUR_API_KEY_HERE"` dengan API Key yang Anda dapatkan dari Groq.

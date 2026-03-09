# Validasi Pendaftaran Siswa

Validasi Pendaftaran Siswa adalah aplikasi desktop berbasis Visual Basic .NET yang dirancang untuk menangani proses input data calon siswa secara akurat. Fokus utama proyek ini adalah penerapan sistem validasi formulir untuk mencegah kesalahan input, data kosong, atau format yang tidak sesuai saat proses pendaftaran.

## 🌟 Fitur Utama

- **Validasi Input Real-time:** Memastikan semua kolom wajib (seperti Nama, Alamat, dan NISN) telah diisi sebelum data disimpan.
- **Pengecekan Tipe Data:** Memastikan input angka (seperti nomor telepon atau tahun lahir) tidak diisi dengan karakter huruf.
- **Antarmuka Formulir User-Friendly:** Desain GUI yang bersih untuk mempermudah operator dalam menginput data siswa.
- **Pesan Kesalahan (Error Provider):** Menampilkan notifikasi atau peringatan yang jelas jika ada kolom yang tidak memenuhi kriteria validasi.

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Visual Basic .NET (VB.NET)
- **Framework:** .NET Framework
- **IDE:** Visual Studio

## 📋 Konsep Validasi yang Diimplementasikan

1. **Required Field Validation:** Memastikan tidak ada textbox yang dibiarkan kosong.
2. **Numeric Validation:** Menggunakan logika `IsNumeric` atau penanganan event `KeyPress` untuk memfilter input.
3. **Length Validation:** Membatasi jumlah karakter untuk kolom tertentu (misalnya NISN harus 10 digit).

## 🚀 Cara Menjalankan

1. **Clone Repositori:**
   ```bash
   git clone [https://github.com/asboyy/Validasi-Pendaftaran-Siswa.git](https://github.com/asboyy/Validasi-Pendaftaran-Siswa.git)

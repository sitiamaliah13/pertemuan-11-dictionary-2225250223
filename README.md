# Pertemuan 11 - Dictionary/Map

Nama: Siti Amaliah  
NIM: 2225250223
Kelas: 3E

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data

Program menggunakan dictionary `data_mahasiswa` dengan NIM sebagai key utama. Value berupa dictionary bersarang yang berisi nama, kelas, dan nilai mahasiswa.

NIM digunakan untuk mencari data mahasiswa. Informasi nama, kelas, dan nilai disimpan sebagai value. Program menggunakan metode `get()` untuk pencarian yang aman, `values()` untuk menghitung rata-rata nilai, dan `items()` untuk menampilkan seluruh data mahasiswa.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal pada folder utama proyek:

```bash
python praktik/data_mahasiswa.py
```

Jika perintah tersebut tidak tersedia, gunakan:

```bash
python3 praktik/data_mahasiswa.py
```

## Test Case

| Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan | [Isi setelah diuji] | [Isi setelah diuji] |
| Pencarian tidak tersedia | A999 | Pesan "Data tidak ditemukan" | [Isi setelah diuji] | [Isi setelah diuji] |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 menjadi 82 | Berhasil |
| Penambahan data | A006 | Key A006 tersedia setelah ditambahkan | Data A006 tampil pada rekap | Berhasil |
| Rekap | `items()` | Semua NIM dan data tampil | Enam mahasiswa tampil pada rekap | Berhasil |
| Rata-rata nilai | Menghitung seluruh nilai | Rata-rata dihitung dengan benar | 83.5 | Berhasil |

## Refleksi

Salah satu kesalahan akses key yang perlu dihindari adalah mengakses key yang tidak tersedia menggunakan tanda kurung siku karena dapat menyebabkan `KeyError`.

Kesalahan tersebut dapat dihindari dengan memeriksa keberadaan key menggunakan operator `in` atau menggunakan metode `get()`. Melalui praktikum ini, saya belajar menggunakan dictionary untuk menyimpan data mahasiswa, mengakses data berdasarkan NIM, menambah dan memperbarui data, menelusuri pasangan key-value menggunakan `items()`, serta menghitung rata-rata nilai.

## Sumber dan Bantuan

Sumber utama: Bahan Ajar Pertemuan 11 - Dictionary/Map dan Pasangan Key-Value dalam Python.

Bantuan: ChatGPT digunakan untuk membantu memahami kode, menyesuaikan program dengan test case modul, dan menyusun dokumentasi. 
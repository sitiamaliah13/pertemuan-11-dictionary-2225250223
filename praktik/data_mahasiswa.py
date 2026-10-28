
def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# 1. Mencari mahasiswa yang tersedia
print("=== PENCARIAN MAHASISWA ===")

nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")


# 2. Mencari mahasiswa yang tidak tersedia
print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")

nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")


# 3. Memperbarui nilai A002 menjadi 82
print("\n=== PEMBARUAN NILAI ===")

data_mahasiswa["A002"]["nilai"] = 82
print("Nilai A002 berhasil diubah menjadi 82")


# 4. Menambahkan mahasiswa A006
print("\n=== PENAMBAHAN MAHASISWA ===")

data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Data A006 berhasil ditambahkan")


# 5. Menampilkan semua data dengan items()
print("\n=== REKAP DATA MAHASISWA ===")

for nim, info in data_mahasiswa.items():
    print(nim, info)


# 6. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")

rata_rata = rata_rata_nilai(data_mahasiswa)
print("Rata-rata nilai:", rata_rata)


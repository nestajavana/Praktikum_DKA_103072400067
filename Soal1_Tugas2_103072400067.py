import numpy as np

# jumlah mahasiswa yang akan diinput
n = int(input("Masukkan jumlah mahasiswa: "))

data = []

for i in range(n):
    print(f"\nData mahasiswa ke-{i+1}")

    nama = input("Nama       : ")
    nim = input("NIM        : ")
    nilai = float(input("Nilai      : "))
    tahun = int(input("Tahun Masuk: "))

    data.append([nama, nim, nilai, tahun])

# mengubah list menjadi numpy array
data_array = np.array(data, dtype=object)

print("\n=== Data Mahasiswa ===")
for d in data_array:
    print("Nama:", d[0], "| NIM:", d[1], "| Nilai:", d[2], "| Tahun Masuk:", d[3])

# mengambil kolom nilai
nilai_array = data_array[:,2].astype(float)

print("\nNilai tertinggi :", np.max(nilai_array))
print("Nilai terendah  :", np.min(nilai_array))
print("Nilai rata-rata :", np.mean(nilai_array))

# pencarian mahasiswa
cari = input("\nCari mahasiswa (Nama/NIM): ")

ditemukan = False
for d in data_array:
    if d[0] == cari or d[1] == cari:
        print("\nData ditemukan:")
        print("Nama:", d[0])
        print("NIM :", d[1])
        print("Nilai:", d[2])
        print("Tahun Masuk:", d[3])
        ditemukan = True

if not ditemukan:
    print("Data tidak ditemukan.")
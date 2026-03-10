import numpy as np

n = int(input("Masukkan jumlah barang: "))

data = []

for i in range(n):
    print(f"\nData barang ke-{i+1}")

    nama = input("Nama Barang : ")
    kode = input("Kode Barang : ")
    jumlah = int(input("Jumlah      : "))
    harga = float(input("Harga/unit  : "))

    data.append([nama, kode, jumlah, harga])

data_array = np.array(data, dtype=object)

print("\nData Inventaris")
for d in data_array:
    total = int(d[2]) * float(d[3])
    print("Nama:", d[0],
          "| Kode:", d[1],
          "| Jumlah:", d[2],
          "| Harga:", d[3],
          "| Total Nilai:", total)

# pencarian barang
cari = input("\nCari barang (nama/kode): ")

ditemukan = False
for d in data_array:
    if d[0] == cari or d[1] == cari:
        total = int(d[2]) * float(d[3])
        print("\nData ditemukan:")
        print("Nama Barang :", d[0])
        print("Kode Barang :", d[1])
        print("Jumlah      :", d[2])
        print("Harga/unit  :", d[3])
        print("Total Nilai :", total)
        ditemukan = True

if not ditemukan:
    print("Barang tidak ditemukan.")
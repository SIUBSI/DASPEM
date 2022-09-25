# 7.2 - Pandas pada Python (hal. 83)

# 7.2.2 - Contoh program dengan pengunaan modul Pandas (hal. 92-93)

import pandas as pd

# Variabel yang berulang menggunakan List/Matriks
ListNIM = []
ListNama = []
ListUTS = []
ListUAS = []
ListTotal = []

Ulang = 5
for i in range(Ulang):
    print("Data ke - " +str(i+1))
    ListNIM.append(input("NIM: "))
    ListNama.append(input("Nama: "))
    ListUTS.append(input("Nilai UTS: "))
    ListUAS.append(input("Nilai UAS: "))

# Proses
for i in range(Ulang):
    ListTotal.append((int(ListUAS[i]) + int(ListUTS[i])) / 2)

Tamu = {
    "NIM": ListNIM,
    "Nama Lengkap": ListNama,
    "Nilai UTS": ListUTS,
    "Nilai UAS": ListUAS,
    "Rata-rata": ListTotal
}

DataTamu = pd.DataFrame(Tamu)

# Cetak
print("="*10+" Daftar Nilai "+"="*10)
print(DataTamu)
print("="*55)
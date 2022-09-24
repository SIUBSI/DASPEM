# Latihan Studi Kasus: Pendaftaran Mahasiswa Baru

import locale

locale.setlocale(locale.LC_ALL, '')

Nama = str(input("Masukkan Nama pendaftar: "))
NIS = str(input("Masukkan NIS pendaftar: "))
Jurusan = str(input("Masukkan Jurusan yang diinginkan: "))

if Jurusan == "SI" or Jurusan == "si":
    Jurusan = "Sistem Informasi"
    Biaya = 2400000
elif Jurusan == "SIA" or Jurusan == "sia":
    Jurusan = "Sistem Informasi Akuntansi"
    Biaya = 2000000
else:
    Jurusan = f"Jurusan '{Jurusan}' tidak ditemukan."
    Biaya = 0

print("Nama: ", Nama)
print("NIS:", NIS)
print("Jurusan:", Jurusan)
print("Biaya yang diperlukan:", locale.currency(Biaya, grouping=True))

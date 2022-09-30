# Tugas 2 - Pertemuan 5 (hal. 64)

import locale
locale.setlocale(locale.LC_ALL, '')

print("\t\t-------------------------")
print("\t\t GEROBAK  FRIED  CHICKEN")
print("\t\t-------------------------")
print("\t\t=========================")
print("\t\tKode JenisPotong Harga")
print("\t\t=========================")
print("\t\tD    Dada        Rp. 2500")
print("\t\tP    Paha        Rp. 2000")
print("\t\tS    Sayap       Rp. 1500")
print("\t\t=========================")

BanyakJenis = int(input("Masukkan Banyak Jenis : "))
KodePotong = []
BanyakPotong = []
JenisPotong = []
Harga = []
TotalHarga = []

i = 0
while i < BanyakJenis:
    KodePotong.append(input(f"({i+1}/{BanyakJenis}). Masukkan Kode Potong [D/P/S]: "))
    BanyakPotong.append(int(input("Masukkan Banyak Potong: ")))

    if KodePotong[i] == "D" or KodePotong[i] == "d":
        JenisPotong.append("Dada")
        Harga.append("2500")
        TotalHarga.append(BanyakPotong[i]*int("2500"))
    elif KodePotong[i] == "P" or KodePotong[i] == "p":
        JenisPotong.append("Paha")
        Harga.append("2000")
        TotalHarga.append(BanyakPotong[i]*int("2000"))
    elif KodePotong[i] == "S" or KodePotong[i] == "s":
        JenisPotong.append("Sayap")
        Harga.append("1500")
        TotalHarga.append(BanyakPotong[i]*int("1500"))
    else:
        JenisPotong.append(f"Kode Potong {KodePotong} tidak ditemukan.")
        Harga.append("0")
        TotalHarga.append(BanyakPotong[i]*int("0"))
    i = i + 1

print("\n\t-------------------------")
print("\t GEROBAK  FRIED  CHICKEN")
print("\t-------------------------")
print("===========================================")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Potong    Satuan       Beli      Harga ")
print("===========================================")

a = 0
while a < BanyakJenis:
    print(f"{a+1}    {JenisPotong[a]}       {Harga[a]}        {BanyakPotong[a]}         {TotalHarga[a]}")
    a = a + 1

print("===========================================")
TotalHargaFinal = sum(TotalHarga)

Pajak = TotalHargaFinal * 0.1
TotalBayar = TotalHargaFinal + Pajak
print("Jumlah Bayar:", locale.currency(TotalHargaFinal, grouping=True))
print("Pajak 10%:", locale.currency(Pajak, grouping=True))
print("Total Bayar:", locale.currency(int(TotalBayar), grouping=True))

JumlahBayar = int(input("Masukkan Jumlah bayar Rp"))
if JumlahBayar > int(TotalBayar):
    Kembalian = JumlahBayar - TotalBayar
    print("="*10+" Pembelian berhasil "+"="*10)
    print("Uang kembalian:", locale.currency(int(Kembalian), grouping=True))
else:
    print("Uang anda tidak mencukupi untuk melakukan pembelian.")
    exit()

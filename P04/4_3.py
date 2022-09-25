# 4.3 - Studi kasus: Penjualan Tiket
print("===== 4.3 - Studi kasus: Penjualan Tiket =====")

import locale
locale.setlocale(locale.LC_ALL, '')

# Penginputan
NamaPembeli = str(input("Masukkan Nama Pembeli: "))
NoHP = str(input("Masukkan Nomor HP: "))
Jurusan = str(input("Masukkan Jurusan [SBY/BL/LMP]: "))

# Proses
if Jurusan == "SBY" or Jurusan == "sby":
    NamaJurusan = "Surabaya"
    Harga = 300000
elif Jurusan == "BL" or Jurusan == "bl":
    NamaJurusan = "Bali"
    Harga = 350000
else:
    NamaJurusan = "Lampung"
    Harga = 500000

# Menginput jumlah beli
JumlahBeli = int(input("Masukkan jumlah pembelian: "))

# Proses potongan
if JumlahBeli >= 3:
    Potongan = (JumlahBeli*Harga)*0.1
else:
    Potongan = 0

TotalBayar = (JumlahBeli*Harga)-Potongan

# Mencetak hasil
print("="*30)
print("         PENJUALAN TIKET BUS")
print("                 XYZ")
print("="*30)
print("Nama Pembeli:", str(NamaPembeli))
print("No. Handphone:", str(NoHP))
print("Kode Jurusan:", str(Jurusan.upper()))
print("Nama Kota Tujuan:", str(NamaJurusan))
print("Harga:", locale.currency(Harga, grouping=True))
print("Jumlah Beli:", JumlahBeli)
print("Total Pembayaran:", locale.currency(TotalBayar, grouping=True))

UangBayar = int(input("Masukkan Uang Bayar: "))
UangKembali = UangBayar-TotalBayar
if UangBayar > TotalBayar:
    print("Uang kembali:", locale.currency(UangKembali, grouping=True))
else:
    print("Uang anda tidak mencukupi untuk melakukan pembelian.")
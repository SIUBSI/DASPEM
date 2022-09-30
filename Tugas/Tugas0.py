import locale
locale.setlocale(locale.LC_ALL, '')

print("\t  Toko Kue Barokah")
print("\t"+"-"*20)

NamaPembeli = str(input("Masukkan Nama Pembeli: "))
KodeKue = str(input("Masukkan Kode Kue: "))
HargaKue = int(input("Masukkan Harga Kue: "))
JumlahBeli = int(input("Masukkan Jumlah Beli: "))
Diskon = int(input("Masukkan Diskon: "))

TotalHarga = int(HargaKue*JumlahBeli)
Diskon = int(TotalHarga*Diskon/100)
UangBayar = int(input(
    f"Harga yang harus anda bayar ({locale.currency(Diskon, grouping=True)}) | Masukkan Uang Bayar: "))
UangKembali = UangBayar - Diskon

print("\n"+"="*10+" Hasil Pembelian anda "+"="*10)
print(f"Nama Pembeli: {NamaPembeli}")
print(f"Kode Kue: {KodeKue}")
print(f"Harga Kue: {locale.currency(HargaKue, grouping=True)}")
print(f"Jumlah Beli: {JumlahBeli}")
print(f"Total Harga: {locale.currency(TotalHarga, grouping=True)}")
print(f"Diskon: {locale.currency(int(Diskon), grouping=True)}")
print(f"Uang Bayar: {locale.currency(UangBayar, grouping=True)}")
print(f"Uang Kembali: {locale.currency(int(UangKembali), grouping=True)}")

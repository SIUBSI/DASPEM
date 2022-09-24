import locale
locale.setlocale(locale.LC_ALL, '')


print("         TOKO MAINAN ANAK")
print("       ********************")

NamaPembeli = str(input("Masukkan nama Pembeli: "))
KodeMainan = str(input("Masukkan nama Kode Mainan: "))
Harga = int(input("Masukkan nama Harga: "))
JumlahBeli = int(input("Masukkan nama Jumlah beli: "))

print("="*50)

print("Nama Pembeli:", NamaPembeli)
print("Kode Mainan:", KodeMainan)
print("Harga:", locale.currency(Harga, grouping=True))
print("Jumlah pembelian:", JumlahBeli)
print("Total:", locale.currency(int(Harga*JumlahBeli), grouping=True))

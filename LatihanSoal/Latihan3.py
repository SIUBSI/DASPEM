# Latihan 3 - Pertemuan 3
'''
• Buatlah program seperti gambar dibawah ini (TOKO MAINAN ANAK)
'''

# Untuk menjadikan output currency menjadi format rupiah
import locale
locale.setlocale(locale.LC_ALL, '')


print("\t\t  TOKO MAINAN ANAK")
print("\t\t********************")

NamaPembeli = str(input("Masukkan nama Pembeli: "))
KodeMainan = str(input("Masukkan nama Kode Mainan: "))
Harga = int(input("Masukkan nama Harga: "))
JumlahBeli = int(input("Masukkan nama Jumlah beli: "))

print("="*20+" Hasil Pembelian "+"="*20)

print("Nama Pembeli:", NamaPembeli)
print("Kode Mainan:", KodeMainan)
print("Harga:", locale.currency(Harga, grouping=True))
print("Jumlah pembelian:", JumlahBeli)
print("Total:", locale.currency(int(Harga*JumlahBeli), grouping=True))

# 4.2 - Pernyataan if...elif...else (hal. 50-52)

import locale
locale.setlocale(locale.LC_ALL, '')

print("===== 4.2 - Pernyataan if...elif...else =====")

'''Program menguji apakah sebuah bilangan bersifat positif, nol atau negatif
dan menampilkan pesan ke Monitor.'''

bilangan = 5.5

'''
Coba juga mengganti bilangan jadi
bilangan = 0
bilangan = -5.5
'''

if bilangan > 0:
    print("Bilangan positif")
elif bilangan == 0:
    print("Nol")
else:
    print("Bilangan negatif")

print("> Contoh Program")

KodeBaju = input("Masukkan Kode Baju [SP/AD]: ")
Ukuran = input("Masukkan Ukuran Baju [S/M]: ")

if KodeBaju == "SP" or KodeBaju == "sp":
    merk = "SuperDry"
    if Ukuran == "S" or Ukuran == "s":
        harga = 450000
    elif Ukuran == "M" or Ukuran == "m":
        harga = 500000
    else:
        harga = 0
elif KodeBaju == "AD" or KodeBaju == "ad":
    merk = "Adidas"
    if Ukuran == "S" or Ukuran == "s":
        harga = 650000
    elif Ukuran == "M" or Ukuran == "m":
        harga = 700000
    else:
        harga = 0
else:
    merk = "Anda salah menginput Kode Merk"
    harga = 0

print("-"*20)
print("Merk Baju:", str(merk))
print("Harga Baju: Rp.", locale.currency(harga, grouping=True))

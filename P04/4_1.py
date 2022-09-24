# 4.1 - Pernyataan if (hal. 47-48)

# Bila bilangan positif, tampilkan pesan

Angka = 5
if Angka > 0:
    print(Angka, "adalah bilangan positif.")

Angka = -1
# Yang berikut akan bernilai False sehinggak tidak dieksekusi
if Angka > 0:
    print(Angka, "adalah bilangan negatif.")

# 4.1.1 - Pernyataan if...else (hal. 48-50)
print("="*30)

'''Program menguji apakah sebuah bilangan bersifat positif atau negatif
dan menampilkan pesan ke Monitor.'''

bilangan = 8

'''coba juga merubah bilangan menjadi bilangan = -1
dan perhatikan hasilnya.'''

if bilangan >= 0:
    print("Bilangan Positif atau Nol")
else:
    print("Bilangan negatif")
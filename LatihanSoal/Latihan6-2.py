# Latihan 6-2 - Pertemuan 6

'''
Buatlah input, proses dan output secara berulang dengan memanfaatkan fungsi matriks/list 
seperti pada koding dibawah ini:
'''

# Variable yg berulang menggunakan List/matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []
ulang = 2
for i in range(ulang):
 list_nim.append(input(f"({str(i+1)}/2). Masukkan NIM anda : "))
 list_uts.append(int(input("Masukkan Nilai UTS anda: ")))
 list_uas.append(int(input("Masukkan Nilai UAS: ")))

# Proses
for i in range(ulang):
 list_total.append((list_uas[i] + list_uts[i]) / 2)

# Cetak
print("========================================================")
print("NIM          UTS     UAS     Rata-Rata")
print("========================================================")
for i in range(ulang):
 print(
     f"{list_nim[i]}     {list_uts[i]}      {list_uas[i]}      {list_total[i]}")
print("========================================================")

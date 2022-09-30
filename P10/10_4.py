# 10.4 - Mengimpor semua fungsi modul pada Python (hal. 105-106)
print("# 10.4 - Mengimpor semua fungsi modul pada Python")

"""
Jika pada contoh sebelumnya menggunakan sebagian fungsi dari suatu modul pada python, 
maka contoh kali ini kita dapat menggunakan semua fungsi pada suatu modul, seperti pada 
contoh dibawah ini:
"""

from math import *

# Menggunakan fungsi pow pada modul math
print("> Menggunakan fungsi pow pada modul math")
pangkat_bilangan = pow(3, 3)
print("Hasil dari pemangkatan bilangan adalah: ", pangkat_bilangan)

# Menggunakan fungsi factorial pada modul math
print("\n> Menggunakan fungsi factorial pada modul math")
bil = int(input("Masukkan sebuah bilangan positif: "))
faktorial_bil = factorial(bil)
print("Bilangan faktorial dari bil adalah: ", faktorial_bil)
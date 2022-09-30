# 10.3 - Mengimpor sebagian fungsi modul pada Python (hal. 104)
print("# 10.3 - Mengimpor sebagian fungsi modul pada Python")

"""
Pada python kita juga bisa menggunakan sebagian fungsi dai suatu modul dengan perintah
from... import... seperti pada contoh dibawah ini :
"""

# Contoh modul Math pow
print("\n> Contoh modul Math Pow")

from math import pow

pangkat_bilangan = pow(3, 3)
print("Hasil dari pemangkatan bilangan adalah: ", pangkat_bilangan)

# Angka 3 pertama merupakan angka yang akan dipangkatkan
# Angka 3 berikutnya adalah jumlah pemangkatan

# Contoh modul Math Factorial
print("\n> Contoh modul Math Factorial")

from math import factorial

bil = int(input("Masukkan sebuah bilangan positif: "))
faktorial_bil = factorial(bil)
print("Bilangan faktorial dari bil adalah: ", faktorial_bil)
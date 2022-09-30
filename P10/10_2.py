# 10.2 - Menggunakan perintah alias pada Modul (hal. 103-104)
print("# 10.2 - Menggunakan perintah alias pada Modul")

"""
Untuk memanggil suatu modul pada python, kita juga bisa memanggil modul tersebut dengan 
merubah namanya dengan perintah as, misalkan pada contoh dibawah ini :
"""

import penggunaan_modul as aritmatika

print(aritmatika.penjumlahan(50, 50))

# Cara lain untuk mengimport modul
"""
Ada beberapa sintaks yang bisa digunakan untuk mengimpor modul, yaitu sebagai berikut:
    - Cara import standar, formatnya import nama_modul
    - Cara import dengan rename (alias), formatnya import nama_modul as alias
    - Cara mengimport sebagian, formatnya from...import something
    - Cara mengimport semua isi modul, formatnya import *
"""
# 10.1 - Menggunakan Perintah Import (hal. 102-103)
print("# 10.1 - Menggunakan Perintah Import")

"""
Kita bisa mengimpor modul python ke dalam program yang kita buat. Dengan mengimpor 
modul, maka definisi, variabel, fungsi dan yang lainnya yang ada di dalam modul itu bisa kita 
pergunakan kapan saja jika diperlukan. Kita mengimpor modul dengan menggunakan kata 
kunci import. Misalnya, kita akan mengimpor modul contoh_penggunaan_modul yang 
sudah kita buat di atas, maka kita bisa mengetikkan perintah berikut:

    import contoh_penggunaan_modul

Setelah kita import, maka kita bisa mengakses isi dari modul contoh_penggunaan_modul. 
Kita bisa mengakses fungsi maupun variabel global di dalam modul tersebut dengan 
menggunakan operasi titik (.). Misalnya sebagai berikut:
"""

import penggunaan_modul

print(penggunaan_modul.penjumlahan(10,90))
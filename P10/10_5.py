# 10.5 - Eksepsi (hal. 106-109)
print("# 10.5 - Eksepsi")

"""
Pada saat menulis dan menjalankan program, kita sering dihadapkan pada munculnya 
kesalahan atau error. Seringkali error menyebabkan program berhenti sendiri.

Error dapat terjadi akibat kesalahan struktur (sintaks) program. Hal ini disebut syntax error. 
Contohnya adalah seperti berikut:

>>> if x < 5
  File "<stdin>", line 1
    if x < 5
SyntaxError: invalid syntax

Kita bisa melihat bahwa penyebabnya adalah lupa titik dua pada pernyataan if.

Error juga dapat terjadi pada saat runtime (saat program berjalan). Error seperti ini disebut 
eksepsi. Misalnya, bila kita membuka file yang tidak ada, maka akan muncul pesan kesalahan 
FileNotFoundError. Bila kita membagi bilangan dengan nol akan muncul ZeroDivisionError, 
dan lain sebagainya.

Pada saat terjadi eksepsi, Python akan menampilkan traceback dan detail dimana kesalahan 
terjadi.

>>> 1/0
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""

# 10.5.1 - Menangani Eksepsi Dengan Try, Except, dan Finally (hal. 109-110)
print("\n\n# 10.5.1 - Menangani Eksepsi Dengan Try, Except, dan Finally")

"""
Terjadinya eksepsi pada program dapat menyebabkan program terhenti. Untuk mencegah 
hal tersebut, kita harus mengantisipasi hal tersebut.Python menyediakan metode 
penanganan eksepsi dengan menggunakan pernyataan try dan except.
Di dalam blok try kita meletakkan baris program yang kemungkinan akan terjadi error. Bila 
terjadi error, maka penanganannya diserahkan kepada blok except. Berikut adalah contoh 
penanganan eksepsi pada operasi pembagian bilangan.
"""

import sys

lists = ['a', 0, 4]
for each in lists:
    try:
        print("Masukan:", each)
        r = 1/int(each)
        break
    except:
        print("Oops!", sys.exc_info()[0], " terjadi.")
        print("Masukkan berikutnya.")
        print()
print("Kebalikan dari ", each, " =", r)

"""
Pada program di atas kita mencari kebalikan dari bilangan, misalnya 4, maka kebalikannya 
adalah 1/4 = 0.25.
Pembagian dengan huruf ‘a’, dan juga dengan 0 tidak bisa dilakukan, sehingga muncul 
error. Bila tidak dilakukan penanganan eksepsi, maka program akan langsung terhenti pada 
saat terjadi error.
"""

# 10.5.2 - Menangani Eksepsi tertentu (hal. 110-111)
print("\n\n# 10.5.2 - Menangani Eksepsi tertentu")

"""
Pada contoh di atas kita hanya menangani error secara umum. Tidak dikelompokkan, 
apakah dia adalah TypeError, ValueError, SyntaxError, dan lain sebagainya. Sebuah 
pernyataan try, bisa memiliki sejumlah pernyataan except untuk menangani jenis – jenis 
eksepsi secara lebih spesifik. Kita juga bisa mendefinisikan beberapa error sekaligus 
menggunakan tuple. Contohnya adalah seperti berikut:

    try:
    # lakukan sesuatu
    pass

    except ValueError:
    # tangani eksepsi ValueError
    pass

    except (TypeError, ZeroDivisionError):
    # menangani multi eksepsi
    # TypeError dan ZeroDivisionError
    pass

    except:
    # menangani eksepsi lainnya
    pass

Pernyataan pass adalah pernyataan yang tidak melakukan apa-apa. Istilahnya adalah 
statemen kosong. pass sering digunakan untuk mengisi blok fungsi atau kelas yang masih 
kosong.

"""

# 10.5.3 - Memunculkan Eksepsi (hal. 111)
print("\n\n# 10.5.3 - Memunculkan Eksepsi")

"""
Eksepsi muncul bila terjadi error pada saat runtime atau saat program berjalan. Akan 
tetapi, kita juga bisa memunculkan eksepsi dengan sengaja untuk maksud tertentu dengan 
menggunakan kata kunci raise. Contohnya adalah seperti berikut:

>>> raise KeyboardInterrupt
Treceback (most recent call last):
...
KeyboardInterrupt

>>> try:
        a = int(input("Masukkan sebuah bilangan positif: "))
        if a <= 0:
            raise ValueError("Itu bukan bilangan positif!")
except ValueError as ve:
        print(ve)

Masukkan sebuah bilangan positif: -3
Itu bukan bilangan positif!
"""
# 9.2 - Memanggil Fungsi (hal. 96-101)
from ast import arg


print("9.2 - Memanggil Fungsi")

'''
Bila fungsi sudah didefinisikan, maka ia sudah bisa dipanggil dari tempat lain di dalam 
program. Untuk memanggil fungsi caranya adalah dengan mengetikkan nama fungsi 
berikut paramaternya. Untuk fungsi di atas, kita bisa melakukannya seperti contoh berikut:
>>> sapa('Galih')
Hi, Galih. Apa kabar?
>>> sapa('Ratna')
Hi, Ratna. Apa kabar?
'''

# A. Docstring
"""
Docstring adalah singkatan dari documentation string. Ini berfungsi sebagai dokumentasi 
atau keterangan singkat tentang fungsi yang kita buat. Meskipun bersifat opsional, 
menuliskan docstring adalah kebiasaan yang baik. Untuk contoh di atas kita menuliskan 
docstring. Cara mengaksesnya adalah dengan menggunakan format namafungsi.__doc__

>>> print(sapa.__doc__)
'''Fungsi ini untuk menyapa seseorang sesuai nama yang
dimasukkan sebagai parameter'''
"""

# Pernyataan Return
"""
Pernyataan return digunakan untuk keluar dari fungsi dan kembali ke baris selanjutnya 
dimana fungsi dipanggil

Adapun sintaks dari return adalah
>>> return [expression_list]

return bisa berisi satu atau beberapa ekspresi atau nilai yang dievaluasi dan nilai tersebut 
akan dikembalikan. Bila tidak ada pernyataan return yang dibuat atau ekspresi 
dikosongkan, maka fungsi akan mengembalikan objek None. Perhatikan bila hasil keluaran 
dari fungsi sapa kita simpan dalam variabel

>>> keluaran = sapa('Gani')
>>> print(keluaran) None
"""

# Argumen Fungsi
"""
Kita bisa memanggil fungsi dengan menggunakan salah satu dari empat jenis argumen 
berikut
    - Argumen Wajib (required argument)
      Argumen wajib adalah argumen yang dilewatkan ke dalam fungsi dengan 
      urutan posisi yang benar. Di sini, jumlah argumen pada saat pemanggilan fungsi 
      harus sama persis dengan jumlah argumen pada pendefinisian fungsi. Pada 
      contoh fungsi sapa() di atas, kita perlu melewatkan satu argumen ke dalam 
      fungsi sapa(). Bila tidak, maka akan muncul error.

      >>> sapa('Umar')
      Hi Umar. Apa kabar?
      >>> # akan muncul error
      >>> sapa()

      Traceback (most recent call last):
        File "<pyshell#5>", line 1, in <module>
        sapa()
      TypeError: sapa() missing 1 required positional 
      argument: 'nama'

    - Argumen kata kunci (keyword argument)
      Argumen dengan kata kunci berkaitan dengan cara pemanggilan fungsi. Ketika 
      menggunakan argumen dengan kata kunci, fungsi pemanggil menentukan 
      argumen dari nama parameternya. Hal ini membuat kita bisa mengabaikan 
      argumen atau menempatkannya dengan sembarang urutan. Python dapat 
      menggunakan kata kunci yang disediakan untuk mencocokkan nilai sesuai 
      dengan parameternya. Jelasnya ada pada contoh berikut
"""

# Definisi fungsi print_string
print("\n# Definisi fungsi print_string")
def print_string(str):
    """Menampilkan argumen string str ke layar"""
    print(str)

# Kita memanggil fungsi dengan kata kunci
print("> Kita memanggil fungsi dengan kata kunci")
print_string(str="Hello Python")

# Urutan parameter tidak menjadi masalah. Perhatikan contoh berikut
print("\n# Urutan parameter tidak menjadi masalah. Perhatikan contoh berikut")

# Definisi fungsi
print("> Definisi Fungsi")
def print_info(nama, usia):
    """Fungsi ini menampilkan info yang dimasukkan"""
    print("Nama: ",nama)
    print("Usia: ",usia)

# Memanggil Fungsi
# Output:
# Name: Daffy
# Usia: 20
print_info(usia = 20, nama = "Daffy")


"""
    - Argumen default
      Fungsi dengan argumen default menggunakan nilai default untuk argumen yang 
      tidak diberikan nilainya pada saat pemanggilan fungsi. Pada contoh berikut, 
      fungsi akan menampilkan usia default bila argumen usia tidak diberikan:
"""

# Definisi Fungsi
print("\n\n# Definisi Fungsi")
def print_info(nama, usia = 17):
    """Fungsi ini menampilkan info yang dimasukkan"""
    print("Nama: ", nama)
    print("Usia: ", usia)


# Memanggil fungsi print_info
print("> Memanggil fungsi print_info")
print_info(usia = 20, nama = "Daffy")

# Pemanggilan fungsi tidak menyertakan argumen usia
print("\n> Pemanggilan fungsi tidak menyertakan argumen usia")
print_info(nama = "Daffy")

"""
Pada contoh di atas, pemanggilan fungsi kedua tidak menyediakan nilai untuk 
parameter usia, sehingga yang digunakan adalah nilai default yaitu 17.

    - Argumen dengan panjang sembarang
      Terkadang kita butuh untuk memproses fungsi yang memiliki banyak argumen. 
      Nama – nama argumennya tidak disebutkan saat pendefinisian fungsi, beda 
      halnya dengan fungsi dengan argumen wajib dan argumen default. Sintaksnya 
      fungsi dengan argumen panjang sembarang adalah seperti berikut:

      def function_name([formal_args,] *var_args_tuple): 
          '''function_docstring''' 
          statement(s) 
          return [expression]

        Tanda asterisk (*) ditempatkan sebelum nama variabel yang menyimpan nilai 
        dari semua argumen yang tidak didefinisikan. Tuple ini akan kosong bila tidak 
        ada argumen tambahan pada saat pemanggilan fungsi. Berikut adalah 
        contohnya:
"""

# Definisi Fungsi
def print_info(arg1, *vartuple):
    """Fungsi ini menampilkan nilai argumen sembarang yang dilewatkan"""
    print("Outputnya adalah: ")
    print(arg1)
    for var in vartuple:
        print(var)


# Pemanggilan fungsi
print("\n\n# Pemanggilan fungsi")
# Satu Argumen
print("> Satu Argumen")
print_info(10)

# Empat argumen
print("\n> Empat Argumen")
print_info(10, 30, 50, 70)

# Ruang Lingkup (Scope) Variabel
print("\n\n# Ruang Lingkup (Scope) Variabel")
"""
Di Python, tidak semua variabel bisa diakses dari semua tempat. Ini tergantung dari 
tempat dimana kita mendefinisikan variabel. Ruang lingkup variabel ada dua, yaitu:
    - Global
    - Local

    Variabel yang didefinisikan di dalam fungsi memiliki scope lokal, sedangkan 
    variabel yang didefinisikan di luar fungsi memiliki scope global. Ini berarti, variabel 
    lokal hanya bisa diakses dari dalam fungsi di mana ia di definisikan, sedangkan variabel 
    global bisa diakses dari seluruh tempat dimanapun di dalam program. Berikut adalah contohnya:
"""

# Variabel Global
print("# Variabel Global")
# Definisi Fungsi
def sum(arg1, arg2):
    """Menambahkan variabel dan mengembalikan hasilnya"""
    total = arg1 + arg2;
    # Total di sini adalah variabel lokal
    print("Di dalam fungsi nilai total: ", total)
    return total

# Pemanggilan fungsi sum
print("> Pemanggilan fungsi sum")
print("Di luar fungsi, nilai total: ", sum(10, 20))
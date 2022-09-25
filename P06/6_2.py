# 6.2 - Tuple (hal. 71)

# 6.2.1 - Membuat Tuple (hal. 72)
print("="*10+" 6.2.1 - Membuat Tuple "+"="*10)

print("Membuat Tuple Kosong")
MyTuple = ()
print(MyTuple)

print("\nTuple dengan 1 Elemen")
# Output: (1, )
MyTuple = (1,)
print(MyTuple)

print("\nTuple dengan berisi integer")
# Output: = (1, 2, 3)
MyTuple = (1, 2, 3)
print(MyTuple)

print("\nTuple Bersarang")
# Output: ("hello", [1, 2, 3], (4, 5, 6))
MyTuple = ("hello", [1, 2, 3], (4, 5, 6))
print(MyTuple)

print("\nTuple bisa tidak menggunakan tanda ()")
# Output: (1, 2, 3)
MyTuple = 1, 2, 3
print(MyTuple)

print("\nMemasukkan anggota Tuple ke variabel yang bersesuaian")
# A akan berisi 1, B berisi 2 dan C berisi 3
# Output: 1 2 3
A, B, C = MyTuple
print(A, B, C)

# 6.2.2 - Mengakses anggota Tuple (hal. 72-73)
print("\n"+"="*10+" 6.2.2 - Mengakses anggota Tuple "+"="*10)

MyTuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')

print("Akses dari indeks 0 s/d 2")
# Output: ('p', 'r', 'o')
print(MyTuple[:3])

print("\nAkses dari indeks 2 s/d 5")
# Output: ('r', 'o', 'g', 'r')
print(MyTuple[2:6])

print("\nAkses dari indeks 3 sampai akhir")
# Output: ('r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')
print(MyTuple[3:])

# 6.2.3 - Mengubah anggota Tuple (hal. 73-74)
print("\n"+"="*10+" 6.2.3 - Mengubah anggota Tuple "+"="*10)

MyTuple = (2, 3, 4, [5, 6])
# Kita bisa mengubah anggota tuple
# Bila kita hilangkan tanda komentar # pada baris ke 6
# Akan muncul error: # TypeError: 'tuple' object does not support item assignment

# MyTuple[1] = 8

print("Tapi list di dalam tuple bisa diubah")
# Output: (2, 3, 4, [7, 6])
MyTuple[3][0] = 7
print(MyTuple)

print("\nTuple bisa diganti secara keseluruhan dengan penugasan kembali")
# Output: ('p', 'y', 't', 'h', 'o', 'n')
MyTuple = ('p', 'y', 't', 'h', 'o', 'n')
print(MyTuple)

print("\nAnggota tuple juga tidak bisa dihapus menggunakan del")
# Perintah berikut akan menghasilkan error TypeError
# Kalau Anda menghilangkan tanda komentar #

# del MyTuple[0]

print("Kita bisa menghapus tuple keseluruhan dengan perintah del MyTuple")
del MyTuple

print("\n(1). Menguji Keanggotaan Tuple")
MyTuple = (1, 2, 3, 'a', 'b', 'c')

print("Menggunakan in")
# Output: False
print('3' in MyTuple)

# Output: False
print('e' in MyTuple)

print("Menggunakan not in")
# Output: True
print('k' not in MyTuple)


print("\n(2). Iterasi pada Tuple")
# Output:
# Hi Galih
# Hi Ratna
Nama = ('Galih', 'Ratna')
for Name in Nama:
    print('Hi', Name)

# 6.2.4 - Metode dan Fungsi Bawaan Tuple (hal. 75-76)
print("\n"+"="*10+" 6.2.4 - Metode dan Fungsi Bawaan Tuple "+"="*10)

MyTuple = ('p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o')
print("Count")
# Output: 2
print(MyTuple.count('n'))

print("Index")
# Output: 5
print(MyTuple.index('n'))
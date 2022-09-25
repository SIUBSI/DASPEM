# 6.1 - List (hal. 66)

'''
Anggota list bisa berisi satu tipe data, atau campuran
'''
# list kosong 
my_list = []
# list berisi integer my_list = [1,2,3,4,5]
# list berisi tipe campuran my_list = [1, 3.5, "Hello"]

'''
List juga bisa berisi list lain. Ini disebut list bersarang
'''
# list bersarang 
my_list = ["hello", [2,4,6], ['a','b']]

# 6.1.1 - Mengakses Anggota List (hal. 66)

MyList = ["I", "love", "python", "programming", 2017]
# Output: I
MyList[0]

# Output: python
MyList[2]

# List dalam list
YourList = ["hello", [1, 2, 3], "python"]

print("="*5+" 6.1.1 - Mengakses Anggota List "+"="*5)
# Output: 1
print(YourList[1][0])

# Output: 3
print(YourList[1][2])

# Output: IndexError
# MyList[6]

# 6.1.2 - List dengan Indeks Negatif (hal. 67)
print("="*5+" 6.1.2 - List dengan Indeks Negatif "+"="*5)

MyList = ['p', 'y', 't', 'h', 'o', 'n']
# Output: n
print(MyList[-1])

# Output: h
print(MyList[-3])

# 6.1.3 - Memotong (Slicing) List (hal. 67)

print("="*5+" 6.1.3 - Memotong (Slicing) List "+"="*5)
MyList = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']

# Anggota list dari 3 s/d 5 (dari h s/d n)
print(MyList[3:6])

# Anggota list dari 4 s/d yang terakhir
print(MyList[4:])

# Anggota list dari 0 s/d 4
print(MyList[:5])

# Indeks dari belakang dari -1 s/d -4
print(MyList[-1:-5])

###### A. Metode List ######
'''
A. List memiliki banyak metode untuk operasi seperti menambahkan anggota, 
menghapus, menyisipkan, menyortir, dan lain sebagainya. Mereka bisa diakses 
menggunakan format list.metode().
'''

###### B. Menambahkan anggota List ######
'''
Fungsi append() berguna untuk menambahkan anggota ke dalam list. Selain itu, ada 
metode extend() untuk menambahkan anggota list ke dalam list.
'''

print("\nB. Menambahkan anggota List")
Ganjil = [1,3,5,7]
Ganjil.append(9)
print(Ganjil)
Ganjil.extend([11,13,15])
print(Ganjil)

'''
Kita juga bisa menggunakan operator + untuk menggabungkan dua list, dan operator
* untuk melipatgandakan list.
'''
print("\nB. Menambahkan anggota List (2)")
Genap = [2, 4, 6]
print(Genap + [8, 10, 12])
print(['p', 'y'] * 2)

###### C. Menyisipkan anggota List ######
'''
Fungsi insert() berfungsi untuk menyisipkan anggota list pada indeks tertentu.
'''

print("\nC. Menyisipkan anggota List")
Ganjil = [5,7,11,13,15]
# Kita akan menyisipkan 9 setelah angka 7

Ganjil.insert(2,9)
print(Ganjil)

###### D. Menghapus anggota List ######

print("\nD. Menghapus anggota List")
MyList = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
MyList.remove('p')

# Output: ['y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
print(MyList)

MyList.remove('n')
# Remove hanya menghapus elemen pertama yang dijumpai
# Output: ['p', 'y', 't', 'h', 'o', 'i', 'n', 'd', 'o']

# Output: 'p'
print(MyList.pop(0))

del MyList[2]
print(MyList)

MyList.clear()
# Output []
print(MyList)

###### E. Mengurutkan anggota List ######

print("\nE. Mengurutkan anggota List")
Alfabet = ['a', 'b', 'd', 'f', 'e', 'c', 'h', 'g', 'j', 'i']
Alfabet.sort()
print(Alfabet)
Alfabet.sort(reverse=True)
print(Alfabet)

###### F. Membalikkan anggota List ######

print("\nF. Membalikkan urutan List")
Alfabet = ['a', 'c', 'd', 'e', 'b']
print(Alfabet)
Alfabet.reverse()
print(Alfabet)
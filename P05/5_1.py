# 5.1 - Perulangan dengan Menggunakan For (hal. 57-58)

# Program untuk menemukan jumlah bilangan dalam satu list
print("===== 5.1 - Program untuk menemukan jumlah bilangan dalam satu list =====")

# List Number
numbers = [7, 5, 9, 8, 9, 0, 8, 4, 0]

# Variabel untuk menyimpan jumlah

sum = 0

# iterasi
for each in numbers:
    sum = sum + each

# Output: jumlah semuanya: 46
print("Jumlah semuanya:", sum)

# 5.1.1 - Fungsi range (hal. 58-59)
print("="*10+" 5.1.1 - Fungsi range "+"="*10)

# Output: range(0,10)
print(range(10))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))
# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2,8)))
# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))

# Program untuk iterasi list menggunakan pengindeksan
print("===== (5.1.1) Program untuk iterasi list menggunakan pengindeksan =====")

Mapel = ['Matematika', 'Fisika', 'Kimia']

# iterasi list menggunakan indeks
for i in range(len(Mapel)):
    print("Saya suka", Mapel[i])

# 5.1.2 - Perulangan menggunakan While
print("="*10+" 5.1.2 - Perulangan menggunakan While "+"="*10)

Count = 0
while (Count < 5):
    print("The count is:", Count)
    Count = Count + 1
print("Good Bye!")

# 5.1.3 - Infinite Loop
print("="*10+" 5.1.3 - Infinite Loop "+"="*10)

# Count = 0
# while (Count < 5):
#     print("The count is", Count)
#     Count = Count
# print("Good Bye!")

# 5.1.4 - Kendali Looping
print("="*10+" 5.1.4 - Kendali Looping "+"="*10)

# Contoh penggunaan statement break
print("|With break|")
for letter in "PythonProgramming":
    if letter == "g":
        break
    print("Huruf sekarang:", letter)
print("Good Bye!")

# ketika break diubah menjadi continue
print("\n|With continue|")
for letter in "PythonProgramming":
    if letter == "g":
        continue
    print("Huruf sekarang:", letter)
print("Good Bye!")
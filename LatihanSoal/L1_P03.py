# Latihan 1 - Pertemuan 3
'''
• Buatlah 1 Contoh Operator Penugasan 
• Buatlah 1 Contoh Operator Logika
• Buatlah 1 Contoh Operator Bitwise 
• Buatlah 1 Contoh Operator Identitas 
• Buatlah 1 Contoh Operator Keanggotaan
'''

# =========== Contoh Operator Penugasan ===========
print("="*10+" Operator Penugasan "+"="*10)

# Mengambil value dari variabel Nilai
Nilai = 10
print("Value dari variabel Nilai adalah =", Nilai)

# Jika Value dari Variabel Nilai ditambahkan menggunakan +=
Nilai += 5
print("Value dari variabel Nilai ditambah 5 menjadi =", Nilai)

# Jika Value dari Variabel Nilai dikurangi menggunakan -=
Nilai -= 5
print("Value dari variabel Nilai dikurang 5 menjadi =", Nilai)

# Jika Value dari Variabel Nilai dikalikan menggunakan *=
Nilai *= 2
print("Value dari variabel Nilai dikali 2 menjadi =", Nilai)

# Jika Value dari Variabel Nilai dikalikan menggunakan *=
Nilai /= 2
print("Value dari variabel Nilai dibagi 2 menjadi =", Nilai)

# Jika Value dari Variabel Nilai dikalikan menggunakan *=
Nilai **= 2
print("Value dari variabel Nilai dipangkat 2 menjadi =", Nilai)

# Jika Value dari Variabel Nilai dikalikan menggunakan *=
Nilai //= 2
print("Value dari variabel Nilai dibagi ke bilangan nilai bulat bernilai 2 menjadi =", Nilai)

# Jika Value dari Variabel Nilai dikalikan menggunakan *=
Nilai %= 5
print("Hasil bagi dari Value pada variabel Nilai dan 5 adalah =", Nilai)


# =========== Contoh Operator Logika ===========
print("="*10+" Operator Logika "+"="*10)

Nilai1 = True
Nilai2 = False

# Logika AND
Nilai3 = Nilai1 and Nilai2
print("True and False =", Nilai3)

# Logika OR
Nilai3 = Nilai1 or Nilai2
print("True or False =", Nilai3)

# Logika Not
Nilai3 = not Nilai1
print("not True =", Nilai3)

# =========== Contoh Operator Bitwise ===========
print("="*10+" Operator Bitwise "+"="*10)

a = 5
b = 30

print('a =', a, '=', format(a, '08b'))
print('b =', b, '=', format(b, '08b'), '\n')

print('[AND]')
print('a & b =', a & b)
print(format(a, '08b'), '&', format(b, '08b'), '=', format(a & b, '08b'), '\n')

print('[OR]')
print('a | b =', a | b)
print(format(a, '08b'), '|', format(b, '08b'), '=', format(a | b, '08b'), '\n')

print('[XOR]')
print('a ^ b =', a ^ b)
print(format(a, '08b'), '^', format(b, '08b'), '=', format(a ^ b, '08b'), '\n')

print('[NOT]')
print('~a ~b =', ~a, ~b)
print('~' + format(a, '08b'), '~' + format(b, '08b'), '=', format(~a, '08b'), format(~b, '08b'), '\n')

print('[SHIFT RIGHT]')
print('a >> b =', a >> b)
print(format(a, '08b'), '>>', format(b, '08b'), '=', format(a >> b, '08b'), '\n')

print('[SHIFT LEFT]')
print('b << a =', b << a)
print(format(b, '08b'), '<<', format(a, '08b'), '=', format(b << a, '08b'), '\n')

# =========== Contoh Operator Identitas ===========
print("="*10+" Operator Identitas "+"="*10)

nama_1 = 'Daffy'
nama_2 = 'Daffy'
list_a = [1, 2, 3]
list_b = [1, 2, 3]
b = 10
a = 10

print('nama_1 is nama_2 =', nama_1 is nama_2)
print('nama_1 is not nama_2 =', nama_1 is not nama_2)
print('list_a is list_b =', list_a is list_b)
print('list_a == list_b =', list_a == list_b)
print('a is b =', a is b)
print('a is not b =', a is not b)

# =========== Contoh Operator Keanggotaan ===========
print("\n"+"="*10+" Operator Keanggotaan "+"="*10)

Kota = ['Depok', 'Bogor']

print("Pada variabel Kota terdapat kota Depok?", 'Depok' in Kota)
print("Pada variabel Kota tidak terdapat kota Jakarta?", 'Jakarta' not in Kota)
# 3.5 - Mengatur format String (hal. 33)

# 3.5.1 - Metode Format (hal. 33-35)
print("===== 3.5.1 - Metode Format =====")

print("> Menggunakan posisi default")
default_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(default_order)

print("> Menggunakan argumen posisi")
positional_order = "{1}, {0} dan {2}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)

print("> Format Integer")
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))

print("> Format Float")
print("Format eksponsial: {0:e}".format(1566.345))

print("> Pembulatan")
print("Sepertiga sama dengan: {0:.3f}".format(1/3))

print("> Meratakan string")
print("|{:<10}|{:^10}|{:>10}".format('beras', 'gula', 'garam'))

print("> Format cara lama menggunakan operator %")
x = 12.3456789
print('Nilai x = %3.2f' %x)
print('Nilai x = %3.4f' %x)

# 3.5.2 - Metode / Fungsi bawaan String (hal. 35)
print("\n===== 3.5.1 - 3.5.2 - Metode / Fungsi bawaan String =====")

print("Universitas Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika".upper())
print("I love programming in Python".split())
print("Saya belajar Python".endswith("on"))
print(' - '.join(['I', 'love', 'you']))
print("Belajar Java di BSI".replace('Java', 'python'))
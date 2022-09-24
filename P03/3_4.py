# 3.4 - Mengetahui panjang String (hal. 31)
string = 'I Love Python'
print(len(string))

# 3.4.1 - Karakter Escape (hal. 31-33)

# Contoh Error
# print("He said, "What's there?"")

# Menggunakan kutip tiga
print('''He said, "What's there?''')

# Menggunakan karakter escape untuk tanda kutip tunggal
print('He said, "What\'s there?')

# Menggunakan karakter escape untuk tanda kutip ganda
print("He said \"What's there?\"")

# Contoh lain
print("Ini adalah baris pertama\nDan ini baris kedua")
print("Ini adalah \x48\x45\x58")

# 3.4.2 - Raw String untuk Mengabaikan Karakter Escape (hal. 33)
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")
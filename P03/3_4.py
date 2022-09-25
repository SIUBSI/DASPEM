# 3.4 - Mengetahui panjang String (hal. 31)

print("===== 3.4 - Mengetahui panjang String =====")
string = 'I Love Python'
print(len(string))

# 3.4.1 - Karakter Escape (hal. 31-33)
print("\n===== 3.4.1 - Karakter Escape =====")

# Contoh Error
# print("He said, "What's there?"")

print("> Menggunakan kutip tiga")
print('''He said, "What's there?''')

print("> Menggunakan karakter escape untuk tanda kutip tunggal")
print('He said, "What\'s there?')

print("> Menggunakan karakter escape untuk tanda kutip ganda")
print("He said \"What's there?\"")

print("> Contoh lain")
print("Ini adalah baris pertama\nDan ini baris kedua")
print("Ini adalah \x48\x45\x58")

# 3.4.2 - Raw String untuk Mengabaikan Karakter Escape (hal. 33)
print("\n===== 3.4.2 - Raw String untuk Mengabaikan Karakter Escape =====")

print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")
# Latihan 6 - Pertemuan 6

'''
3.1 - Studi Kasus:
    Buatlah sebuah list (array) 2 dimensi dimana terdapat baris dan kolom dengan nilai sebagai berikut:
    1   2   3
    4   5   6
    7   8   9
    0

Tampilkanlah:
- Baris Pertama, Kolom Pertama
- Baris Pertama, Kolom Kedua
- Baris Pertama, Kolom Ketiga
- Baris Ketiga, Kolom Ketiga
- Baris Keempat, Kolom Pertama
'''

MyList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(f"Baris Pertama, Kolom Pertama adalah: {MyList[0][0]}")
print(f"Baris Pertama, Kolom Kedua adalah: {MyList[0][1]}")
print(f"Baris Pertama, Kolom Ketiga adalah: {MyList[0][2]}")
print(f"Baris Kedua, Kolom Pertama adalah: {MyList[1][0]}")
print(f"Baris Kedua, Kolom Kedua adalah: {MyList[1][1]}")
print(f"Baris Kedua, Kolom Ketiga adalah: {MyList[1][2]}")
print(f"Baris Ketiga, Kolom Pertama adalah: {MyList[2][0]}")
print(f"Baris Ketiga, Kolom Kedua adalah: {MyList[2][1]}")
print(f"Baris Ketiga, Kolom Ketiga adalah: {MyList[2][2]}")
print(f"Baris keempat, Kolom Pertama adalah: {MyList[3][0]}")

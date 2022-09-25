# 7.1 - Matrix (hal. 80)

# 7.1.1 - Membuat Matrix di Python (hal. 80)
print("===== 7.1.1 - Membuat Matrix di Python =====")

print("> Matriks dengan ukuran 2x2")
MatriksA = [[1, 0], [0,1]]
print(MatriksA)

print("> Matriks dengan ukuran 3x3")
MatriksB = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(MatriksB)

print("> Matriks dengan ukuran 4x4")
MatriksC = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
print(MatriksC)

# Contoh 2
Matrix = [
    [5, 0],
    [2, 6]
]

Matrix1 = [
    [5, 0, 8],
    [2, 6, 7],
    [1, 3, 4]
]

Matrix2 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# 7.1.2 - Melakukan Penjumlahan Matrix (hal. 81)
print("\n7.1.2 - Melakukan Penjumlahan Matrix")

Mat1 = [
    [9, 0],
    [3, 6]
]

Mat2 = [
    [6, 0],
    [7, 2]
]

for x in range(0, len(Mat1)):
    for y in range(0, len(Mat1[0])):
        print(Mat1[x][y] + Mat2[x][y], end=' '),
    print

# 7.1.3 - Melakukan Pengurangan Matrix (hal. 81-82)
print("\n7.1.3 - Melakukan Pengurangan Matrix")

Mat1 = [
    [9, 0],
    [3, 6]
]

Mat2 = [
    [6, 0],
    [7, 2]
]

for x in range(0, len(Mat1)):
    for y in range(0, len(Mat1[0])):
        print(Mat1[x][y] - Mat2[x][y], end=' '),
    print

# 7.1.4 - Melakukan Perkalian Matrix (hal. 82-83)
print("\n7.1.4 - Melakukan Perkalian Matrix")

Mat1 = [
    [9, 0],
    [3, 6]
]

Mat2 = [
    [6, 0],
    [7, 2]
]

Mat3 = []

for x in range(0, len(Mat1)):
    row = []
    for y in range(0, len(Mat1[0])):
        total = 0
        for z in range(0, len(Mat1)):
            total = total + (Mat1[x][z] * Mat2[z][y])
        row.append(total)
    Mat3.append(row)

for x in range(0, len(Mat3)):
    for y in range(0, len(Mat3[0])):
        print(Mat3[x][y], end=' ')
    print()
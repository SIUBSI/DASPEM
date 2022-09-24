# 3.7.2 - Operator Perbandingan (hal. 41-42)

'''
> | Lebih besar dari – Hasilnya True jika nilai sebelah kiri 
lebih besar dari nilai sebelah kanan | a > b
< | Lebih kecil dari – Hasilnya True jika nilai sebelah kiri lebih 
kecil dari nilai sebelah kanan | a < b
== | Sama dengan – Hasilnya True jika nilai sebelah kiri sama 
dengan nilai sebelah kanan | a == b
!= | Tidak sama dengan – Hasilnya True jika nilai sebelah kiri 
tidak sama dengan nilai sebelah kanan | a != b
>= | Lebih besar atau sama dengan – Hasilnya True jika nilai 
sebelah kiri lebih besar atau sama dengan nilai sebelah 
kanan | a >= b
<= | Lebih kecil atau sama dengan – Hasilnya True jika nilai 
sebelah kiri lebih kecil atau sama dengan nilai sebelah 
kanan | a <= b
'''

nilai1 = int(input("Masukkan Nilai Pertama: "))
nilai2 = int(input("Masukkan Nilai Kedua: "))

operator_lebih_besar = nilai1 > nilai2
print(nilai1, ">", nilai2, "adalah", operator_lebih_besar)

operator_lebih_kecil = nilai1 < nilai2
print(nilai1, "<", nilai2, "adalah", operator_lebih_kecil)

operator_sama_dengan = nilai1 == nilai2
print(nilai1, "==", nilai2, "adalah", operator_sama_dengan)

operator_tidak_sama_dengan = nilai1 != nilai2
print(nilai1, "!=", nilai2, "adalah", operator_tidak_sama_dengan)


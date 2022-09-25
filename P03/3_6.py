# 3.6 - Bilangan (Number)  (hal. 36)

# 3.6.1 - Konversi Jenis Bilangan (hal. 36)
print("===== 3.6.1 - Konversi Jenis Bilangan =====")

print(int(2.5))
print(int(3.8))
print(float(5))

# 3.6.2 - Python Decimal (hal. 36-37)
print("\n===== 3.6.2 - Python Decimal =====")

print((1.1 + 2.2) == 3.3)
print(1.1 + 2.2)

import decimal

print(0.1)
print(decimal.Decimal(0.1))

# 3.6.3 - Bilangan pecahan (hal. 38)
print("\n===== 3.6.2 - 3.6.3 - Bilangan pecahan =====")

import fractions
#output: 3/2
print(fractions.Fraction(1.5))
#output: 1/3
print(fractions.Fraction(1,3))

from fractions import Fraction as F
#output: 2/3
print(F(1,3) + F(1,3))
#output: 6/5
print(1 / F(5,6))
#output True
print(F(-3,10) < 0)
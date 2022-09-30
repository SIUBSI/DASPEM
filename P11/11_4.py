# 11.4 - Constructor (hal. 114)

"""
Pada contoh awal tentang penjelasan class, terdapat sebuah method bernama 
__init__(). Method itulah yang disebut dengan constructor. Suatu constructor berbeda 
dengan method lainnya, karena constructor akan otomatis dieksekusi ketika membuat object 
dari class itu sendiri.
"""


class Car:
   color = 'black'
   transmission = 'manual'

def __init__(self, transmission):
   self.transmission = transmission
   print('Engine is ready!')
...

honda = Car('automatic')
# >>> 'Engine is ready!'

"""
Ketika object honda dibuat dari class Car, constructor langsung dieksekusi. Hal ini berguna 
jika anda membutuhkan proses inisialisasi ketika suatu object dibuat. Suatu constructor juga 
bisa memiliki satu atau beberapa parameter, sama seperti method pada umumnya namun 
constructor tidak bisa mengembalikan value.
"""
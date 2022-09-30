# 11.5 - Object (hal. 115)

"""
Object merupakan produk hasil dari suatu class. Jika class merupakan blueprint dari 
suatu rancangan bangunan, maka object adalah bangunan itu sendiri. Begitulah contoh analogi 
yang bisa saya gambarkan mengenai relasi antara class dan object. Berikut contoh 
implementasi dalam bentuk code program.
"""

class Car:
    color = 'black'
    transmission = 'manual'
    gear_position = 'N'

def __init__(self, transmission):
    self.transmission = transmission
    print('Engine is ready!')

def drive(self):
    self.gear_position = 'D'
    print('Drive')

def reverse(self):
    self.gear_position = 'N'
    print('Reverse. Please check your behind.')

def change_gear(self, gear='N'):
    self.gear_position = gear
    print('Gear position on: ' + self.gear_position)

def get_gear_position(self):
    return self.gear_position

car1 = Car('manual')
car1.change_gear('D-1')

car2 = Car('automatic')
gear_position = car2.get_gear_position()
print(gear_position)
# >>> 'N'

"""
Dari contoh di atas, terdapat 2 buah object car1 dan car2 yang dibuat dari class yang sama. 
Masing-masing dari object tersebut berdiri sendiri, artinya jika terjadi perubahan attribute dari 
object car1 tidak akan mempengaruhi object car2 meskipun dari class yang sama.
"""
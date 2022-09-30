# 11.9 - Polymorphism (hal. 116-117)

"""
polimorfisme yang memungkinkan anda untuk membuat banyak bentuk dari satu object. 
Berikut contoh implementasinya:
"""


class Car:
    def fuel(self):
        return 'gas'

class Honda(Car):
    pass

class Tesla(Car):
    def fuel(self):
        return 'electricity'

def get_fuel(car):
    print(car.fuel())

get_fuel(Tesla())
get_fuel(Honda())
# >>> 'electricity'
# >>> 'gas'

"""
    - Polimorfisme merupakan kemampuan objek objek yang berbeda kelas namun terkait 
      dalam pewarisan untuk merespon secara berbeda terhadap suatu pesan yang sama
    - Polimorfisme juga dapat dikatakan kemampuan sebuah objek untuk memutuskan 
      method mana yang akan diterapkan padanya, tergantung letak objek tersebut pada jenjang pewarisan
"""
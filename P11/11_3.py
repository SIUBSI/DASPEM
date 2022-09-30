# 11.3 - Function / Method (hal. 113-114)

"""
Fungsi method dalam konsep OOP adalah untuk merepresentasikan suatu behaviour. 
Dalam contoh di atas suatu object 'mobil' memiliki behaviour antara lain adalah bergerak dan 
mundur. Suatu method bisa juga memiliki satu atau beberapa parameter, sebagai contoh:
"""

gear_position = 'N'

def change_gear(self, gear):
    self.gear_position = gear
    print('Gear positiion on: ' + self.gear_position)

"""
Pada method change_gear() terdapat 1 parameter yaitu gear. Ketika method tersebut 
dipanggil dan anda tidak memberikan value pada parameter tersebut, maka program akan 
melempar error. Bagaimanapun juga parameter yang sudah didefinisikan pada suatu method 
harus memiliki value meskipun value tersebut None. Cara lainnya adalah dengan 
mendefinisikan default value pada parameter tersebut sejak awal method tersebut dibuat:
"""

gear_position = 'N'

def change_gear(self, gear='N'):
    self.gear_position = gear
    print('Gear positiion on: ' + self.gear_position)

    self.change_gear()
    # >>> 'Gear position on: N'
    self.change_gear('R')
    # >>> 'Gear position on: R

"""
Jika diperhatikan, terdapat keyword self pada salah satu parameter method di atas. 
Keyword self mengacu pada Class Instance untuk mengakses attribute atau method dari class 
itu sendiri. Dalam bahasa pemrograman Java, terdapat keyword this yang memiliki fungsi 
yang mirip dengan keyword self pada Python. Pemberian keyword self pada parameter awal 
suatu method menjadi wajib jika anda mendefinisikan method tersebut di dalam block suatu 
class.

Suatu method juga bisa mengembalikan suatu value ketika method tersebut dipanggil. 
Berikut contoh implementasinya:
"""


def get_gear_position(self):
    return self.gear_position

    gear_position = self.get_gear_position()

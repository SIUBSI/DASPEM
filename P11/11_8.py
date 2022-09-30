# 11.8 - Private Attribute/Function (hal. 116)

"""
Tidak semua attribute maupun method bisa diturunkan pada class child. Anda bisa 
menentukan mana attribute atau method yang ingin diproteksi agar tidak bisa digunakan pada 
class turunannya. Berikut caranya:
"""

__factory_number = '0123456789'

def __get_factory_number(self):
    return self.__factory_number
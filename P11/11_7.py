# 11.7 - Overriding (hal. 116)

"""
Ada suatu kondisi dimana suatu method yang berasal dari parent ingin anda modifikasi 
atau ditambahkan beberapa fitur sesuai kebutuhan pada class child, disinilah peran dari 
'overriding method'. Dengan menggunakan fungsi super(), anda bisa memanggil instance dari 
class parent di dalam suatu method untuk memanggil fungsi dari parent tersebut. Perhatikan 
contoh di bawah ini.
"""

"""
class Tesla(Car):

    def drive(self):
        super().drive()
        print('LOL Gas')
"""
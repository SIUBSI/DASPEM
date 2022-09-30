# 11.6 - Inheritance (hal. 115-116)

"""
Salah satu keuntungan dari konsep OOP ialah reusable codes yang bisa mengoptimalkan 
penggunaan code program agar lebih efisien dan meminimalisir redudansi.

    - Kita dapat mendefinisikan suatu kelas baru dengan mewarisi sifat dari kelas lain yang sudah ada
    - Penurunan sifat ini bisa dilakukan secara bertingkat tingkat, sehingga semakin ke 
      bawah kelas tersebut menjadi semakin spesifik
    - Sub kelas memungkinkan kita untuk melakukan spesifikasi detail dan perilaku khusus dari kelas supernya
    - Dengan konsep pewarisan, seorang programmer dapat menggunakan kode yang 
      telah ditulisnya pada kelas super berulang kali pada kelas-kelas turunannya tanpa harus menulis ulang semua kodekode itu

Semua itu berkat adanya fitur inheritance yang memungkinkan suatu class (parent) 
menurunkan semua attribute dan behaviour nya ke class (child) lain. Berikut contoh 
penerapannya:
"""

"""
class Tesla(Car):
    pass  # use 'pass' keyword to define class only

    tesla = Tesla()
    tesla.drive()
    # >>> 'Drive'
"""

"""
Pada potongan code di atas, class Tesla merupakan turunan dari class Car. Jika diperhatikan 
pada class Tesla tidak didefinisikan method drive() namun class tersebut bisa memanggil 
method drive(). Method tersebut berasal dari class parentnya yaitu class Car, sehingga tidak 
perlu lagi didefinisikan ulang pada class childnya. Dengan cara seperti ini anda bisa melakukan 
reusable codes sehingga source code menjadi lebih clean.
"""
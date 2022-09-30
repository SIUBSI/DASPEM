# Latihan 1 - Pertemuan 5
'''
• Lakukan pengulangan input data sebanyak 2 kali dengan data dibawah ini:
Data Ke- <berulang>
Masukkan NIM anda : <Input Data Ke 1>
Masukkan Nilai UTS : <Input Data Ke 1>
Masukkan Nilai UAS : <Input Data Ke 1>
Nim anda adalah <outputnim1> nilai UTS anda <outpututs1> nilai UTS anda <outputuas1>
'''

ulang=2
for i in range(ulang):
 NIM = input(f"({str(i+1)}/2). Masukkan NIM anda : ")
 UTS = int(input("Masukkan Nilai UTS anda: "))
 UAS = int(input("Masukkan Nilai UAS: "))
 print("NIM anda adalah %s nilai UTS anda %i nilai UTS anda %i" % (NIM,UTS,UAS))
 print("="*30+"\n")
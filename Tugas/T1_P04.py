# Tugas 1 - Pertemuan 4 (hal. 55)

Nama = str(input("Masukkan Nama: "))
GolonganJabatan = str(input("Pilih Golongan Jabatan [1/2/3]: "))
JumlahJamKerja = int(input("Masukkan Jam Kerja: "))
Pendidikan = str(input("Masukkan Pendidikan [SMA/D1/D3/S1]: "))
Gaji = 300000

# Perhitungan Tunjangan Jabatan
if GolonganJabatan == "1":
    TunjanganJabatan = 0.05*Gaji
elif GolonganJabatan == "2":
    TunjanganJabatan = 0.10*Gaji
elif GolonganJabatan == "3":
    TunjanganJabatan = 0.15*Gaji
else:
    print("\nGolongan jabatan", GolonganJabatan+" tidak ditemukan.")
    exit()

# Perhitungan Tunjangan Pendidikan
if Pendidikan == "SMA" or Pendidikan == "sma":
    TunjanganPendidikan = 0.025*Gaji
elif Pendidikan == "D1" or Pendidikan == "d1":
    TunjanganPendidikan = 0.05*Gaji
elif Pendidikan == "D3" or Pendidikan == "d3":
    TunjanganPendidikan = 0.20*Gaji
elif Pendidikan == "S1" or Pendidikan == "s1":
    TunjanganPendidikan = 0.30*Gaji
else:
    print("\nPendidikan", Pendidikan+" tidak ditemukan.")
    exit()

# Perhitungan Final
if JumlahJamKerja > 8:
    Lembur = JumlahJamKerja - 8
    JumlahLembur = Lembur * 3500
else:
    Lembur = 0
    JumlahLembur = 0

TotalGaji = TunjanganJabatan + TunjanganPendidikan + Gaji + JumlahLembur

print("="*20+" Hasil "+"="*20)
print("Data Karyawan dengan nama: ", Nama)
print(" Golongan Jabatan:", GolonganJabatan)
print(" Jumlah Jam Kerja:", JumlahJamKerja)
print(" Pendidikan:", Pendidikan.upper())
print("\nHonor yang diterima")
print(" Gaji Pokok: Rp", Gaji)
print(" Tunjangan Jabatan: Rp", int(TunjanganJabatan))
print(" Tunjangan Pendidikan: Rp", int(TunjanganPendidikan))
print(" Honor Lembur: Rp", str(JumlahLembur) + " (Total waktu Lembur: ", str(Lembur)+" jam)")
print(" Total Gaji: Rp", int(TotalGaji))
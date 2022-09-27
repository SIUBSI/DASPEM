# Layanan Aqiqah “Amanah Subscriber Aqiqah”

import locale
from colorama import Fore, Style, init
init(autoreset=True)

locale.setlocale(locale.LC_ALL, '')

print("\t\t"+"="*41)
print(f"\t\tLayanan Aqiqah “Amanah Subscriber Aqiqah”")
print("\t\t"+"="*41+"\n")

NamaPembeli = str(input(f"{Fore.BLUE}Masukkan Nama pembeli{Style.RESET_ALL}: "))
TelpPembeli = str(input(f"{Fore.BLUE}Masukkan Nomor HP Pembeli{Style.RESET_ALL}: "))

print("\t\t"+"="*20)
print("\t\tPAKET YANG TERSEDIA")
print("\t\t"+"="*20)
print("Keterangan:\nBerikut daftar Paket yang tersedia (pilih paket dengan menginputkan nomor yang sudah ditentukan)")
print(f" {Fore.YELLOW}1. Paket Syar'i{Style.RESET_ALL}")
print(f" {Fore.YELLOW}2. Paket Afdhal{Style.RESET_ALL}\n")
Paket = input("Pilih Paket [1/2]: ")
if Paket == "1":
    NamaPaket = "Paket Syar'i"
    print("============= Paket Syar'i ===============")
    print(f"{Fore.YELLOW}1. Tipe A - Rp. 1.350.000 (200 tusuk + 50 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2. Tipe B - Rp. 1.450.000 (250 tusuk + 60 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}3. Tipe C - Rp. 1.550.000 (300 tusuk + 80 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}4. Tipe D - Rp. 1.750.000 (400 tusuk + 100 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}5. Tipe Super - Rp. 2.000.000 (500 tusuk + 120 porsi){Style.RESET_ALL}")
    print("==========================================")
    Tipe = input("Pilih Tipe [1/2/3/4/5]: ")
    if Tipe == "1":
        NamaTipe = "Tipe A"
        Harga = 1350000
    elif Tipe == "2":
        NamaTipe = "Tipe B"
        Harga = 1450000
    elif Tipe == "3":
        NamaTipe = "Tipe C"
        Harga = 1550000
    elif Tipe == "4":
        NamaTipe = "Tipe D"
        Harga = 1750000
    elif Tipe == "5":
        NamaTipe = "Tipe Super"
        Harga = 2000000
    else:
        NamaTipe = "Tidak diketahui"

    JumlahBeli = int(input("Masukkan Jumlah Beli: "))
    TotalPembayaran = Harga*JumlahBeli
    DP = int(input(f"Masukkan DP (DP yang diperlukan adalah melebihi 50% dari harga pembelian, jadi DP yang diperlukan dalam pembelian anda adalah minimum {Fore.BLUE}{locale.currency(int(TotalPembayaran-0.50*TotalPembayaran), grouping=True)}{Style.RESET_ALL} dan maximum {Fore.BLUE}{locale.currency(int(TotalPembayaran*0.80), grouping=True)}{Style.RESET_ALL}): "))
    
    print("\n===== KETERANGAN PEMBELIAN =====")
    print(f"{Fore.BLUE}Item yang dibeli{Style.RESET_ALL}: {NamaPaket} ({NamaTipe})")
    print(f"{Fore.BLUE}Total yang harus dibayar dalam pembelian{Style.RESET_ALL}: {locale.currency(TotalPembayaran, grouping=True)}")
    print(f"{Fore.BLUE}DP yang diperlukan dalam pembayaran{Style.RESET_ALL}: {locale.currency(int(TotalPembayaran*0.50), grouping=True)} (Minimum) & {locale.currency(int(TotalPembayaran*0.80), grouping=True)} (Maximum)")
    print(f"{Fore.BLUE}DP yang dibayar{Style.RESET_ALL}: {locale.currency(DP, grouping=True)}")
    print("\n===== KONFIRMASI PEMBELIAN =====")
    print("1. Lanjut & Bayar\n2. Batalkan Pembelian")
    KonfirmasiPembelian = input("Konfirmasi pembelian [1/2]: ")
    if KonfirmasiPembelian == "1":
        if DP >= int(TotalPembayaran*0.50) and DP <= int(TotalPembayaran*0.80):
            print("\n\t\t"+"="*44)
            print(f"\t\t{Fore.WHITE}Terimakasih telah menggunakan layanan Aqiqah\n\t\t\t“Amanah Subscriber Aqiqah”{Style.RESET_ALL}")
            print("\t\t"+"="*44)
            print(f"\n\t\t      {Fore.GREEN}Pembelian atas nama {NamaPembeli.capitalize()} berhasil{Style.RESET_ALL}.\nSelanjutnya kami akan mengirim keterangan/ketentuan pengiriman melalui\nNomor Hp yang sudah anda berikan ke kami yaitu {TelpPembeli}, silahkan dicek dalam beberapa saat.")
        else:
            print("\n\t\t"+"="*44)
            print("\t\tTerimakasih telah menggunakan layanan Aqiqah\n\t\t\t“Amanah Subscriber Aqiqah”")
            print("\t\t"+"="*44)
            print(f"\n\t\t  {Fore.RED}Pembelian atas nama {NamaPembeli} tidak berhasil{Style.RESET_ALL}.\ndikarenakan DP tidak sesuai dengan ketentuan yaitu DP minimum 50% dan maximum 80% dari harga pembelian.")
            exit()
    elif KonfirmasiPembelian == "2":
        print("Pembelian dibatalkan.")
    else:
        print(f"Pilihan {KonfirmasiPembelian} tidak diketahui.")
        exit()

    
elif Paket == "2":
    NamaPaket = "Paket Afdhal"
    print("============= Paket Afdhal ===============")
    print(f"{Fore.YELLOW}1. Tipe A - Rp. 1.600.000 (200 tusuk + 50 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2. Tipe B - Rp. 1.850.000 (250 tusuk + 60 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}3. Tipe C - Rp. 2.150.000 (300 tusuk + 80 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}4. Tipe D - Rp. 2.500.000 (400 tusuk + 100 porsi){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}5. Tipe Super - Rp. 3.000.000 (500 tusuk + 120 porsi){Style.RESET_ALL}")
    print("==========================================")
    Tipe = input("Pilih Tipe [1/2/3/4/5]: ")
    if Tipe == "1":
        NamaTipe = "Tipe A"
        Harga = 1600000
    elif Tipe == "2":
        NamaTipe = "Tipe B"
        Harga = 1850000
    elif Tipe == "3":
        NamaTipe = "Tipe C"
        Harga = 2150000
    elif Tipe == "4":
        NamaTipe = "Tipe D"
        Harga = 2500000
    elif Tipe == "5":
        NamaTipe = "Tipe Super"
        Harga = 3000000
    else:
        NamaTipe = "Tidak diketahui"

    JumlahBeli = int(input("Masukkan Jumlah Beli: "))
    TotalPembayaran = Harga*JumlahBeli
    DP = int(input(f"Masukkan DP (DP yang diperlukan adalah melebihi 50% dari harga pembelian, jadi DP yang diperlukan dalam pembelian anda adalah minimum {Fore.BLUE}{locale.currency(int(TotalPembayaran-0.50*TotalPembayaran), grouping=True)}{Style.RESET_ALL} dan maximum {Fore.BLUE}{locale.currency(int(TotalPembayaran*0.80), grouping=True)}{Style.RESET_ALL}): "))

    print("\n===== KETERANGAN PEMBELIAN =====")
    print(f"{Fore.BLUE}Item yang dibeli{Style.RESET_ALL}: {NamaPaket} ({NamaTipe})")
    print(f"{Fore.BLUE}Total yang harus dibayar dalam pembelian{Style.RESET_ALL}: {locale.currency(TotalPembayaran, grouping=True)}")
    print(f"{Fore.BLUE}DP yang diperlukan dalam pembayaran{Style.RESET_ALL}: {locale.currency(int(TotalPembayaran*0.50), grouping=True)} (Minimum) & {locale.currency(int(TotalPembayaran*0.80), grouping=True)} (Maximum)")
    print(f"{Fore.BLUE}DP yang dibayar{Style.RESET_ALL}: {locale.currency(DP, grouping=True)}")
    print("\n===== KONFIRMASI PEMBELIAN =====")
    print("1. Lanjut & Bayar\n2. Batalkan Pembelian")
    KonfirmasiPembelian = input("Konfirmasi pembelian [1/2]: ")
    if KonfirmasiPembelian == "1":
        if DP >= int(TotalPembayaran*0.50) and DP <= int(TotalPembayaran*0.80):
            print("\n\t\t"+"="*44)
            print(
                f"\t\t{Fore.WHITE}Terimakasih telah menggunakan layanan Aqiqah\n\t\t\t“Amanah Subscriber Aqiqah”{Style.RESET_ALL}")
            print("\t\t"+"="*44)
            print(f"\n\t\t      {Fore.GREEN}Pembelian atas nama {NamaPembeli.capitalize()} berhasil{Style.RESET_ALL}.\nSelanjutnya kami akan mengirim keterangan/ketentuan pengiriman melalui\nNomor Hp yang sudah anda berikan ke kami yaitu {TelpPembeli}, silahkan dicek dalam beberapa saat.")
        else:
            print("\n\t\t"+"="*44)
            print(
                "\t\tTerimakasih telah menggunakan layanan Aqiqah\n\t\t\t“Amanah Subscriber Aqiqah”")
            print("\t\t"+"="*44)
            print(f"\n\t\t  {Fore.RED}Pembelian atas nama {NamaPembeli} tidak berhasil{Style.RESET_ALL}.\ndikarenakan DP tidak sesuai dengan ketentuan yaitu DP minimum 50% dan maximum 80% dari harga pembelian.")
            exit()
    elif KonfirmasiPembelian == "2":
        print("Pembelian dibatalkan.")
    else:
        print(f"Pilihan {KonfirmasiPembelian} tidak diketahui.")
        exit()

else:
    print(f"Paket {Paket} tidak ditemukan.")
    exit()
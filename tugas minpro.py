def login():
    print("=== Selamat Datang di pengambilan gaji karyawan perusahaan ===")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    print(f"Halo {nama}, Selamat Datang Di Perusahaan Kami!\n")

def hitung_total_gaji():

    try:
        jam_kerja = float(input("Masukkan total jam kerja:"))
        tarif_kerja = int(input("Masukkan tarif kerja: "))
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")
        return None

    
    total_gaji = jam_kerja * tarif_kerja

    
    if jam_kerja > 160:
        bonus = 0.10
        total_gaji_setelah_mendapatkan_bonus = total_gaji - (total_gaji * 0.10)
        print(f"Total gaji sebelum mendapatkan bonus: Rp {total_gaji:.2f}")
        print(f"Anda mendapatkan bonus 10%!")
        print(f"Total gaji setelah mendapatkan bonus: Rp {total_gaji_setelah_mendapatkan_bonus:.2f}")
    else:
        print(f"Total_gaji: Rp {total_gaji:.2f}")
        print(f"maaf sekali Anda tidak mendapatkan bonus,tetap semangat kawan")

def main():
    login()
    while True:
        hitung_total_gaji()
        
        pilihan = input("Apakah Anda ingin menghitung total gaji lagi? (ya/tidak): ")
        if pilihan != 'ya':
            print("Terima kasih telah mengambil gaji bulanan karyawan !")
            break


main()
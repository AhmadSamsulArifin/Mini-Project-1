while True:
    print(" Selamat datang di tempat pengambilan gaji bulanan perusahaan Merah putih  ")
    Nama = (input("Masukkan Nama:"))
    Nim = (input("Masukkan Nim:"))
    print(f"Hai {Nama}, silahkan masuk ke ruangan!\n")
    # Input jam kerja dan tarif kerja
    jam_kerja = float(input("Masukkan jam kerja karyawan: "))
    tarif_kerja = float(input("Masukkan tarif per jam: "))

    # Menghitung total gaji
    total_gaji = jam_kerja * tarif_kerja

    # Menentukan apakah ada bonus
    if jam_kerja > 160:
        bonus = total_gaji * 0.10
        total_gaji += bonus
        print("Selamat anda mendapatkan bonus 10%.")
    else:
        print("Maaf anda tidak mendapatkan bonus tetap semangat untuk kedepannya.")

    # Menampilkan total gaji
    print(f"Total gaji karyawan adalah: Rp {total_gaji:.2f}")

    # Pilihan untuk menghitung gaji lagi atau keluar
    pilihan = input("Apakah Anda ingin menghitung gaji lagi? (ya/tidak): ").lower()
    if pilihan != 'ya':
        print("Terima kasih silahkan keluar dari ruangan.")
        break

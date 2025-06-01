def tampilkan_daftar_film():
    print("Selamat datang di Netflix Lite KW 10!")
    print("Berikut adalah daftar film yang tersedia:")
    print("1. The Substance (18+)")
    print("2. Mean Girls (13+)")
    print("3. Trolls(Semua umur)")
    print("4. Saw(21+)")
    print("5. Ready Player One(13+)")
    print("6. Inside out 2(Semua Umur)")
    print()

def cek_kelayakan(umur, batas_umur):
    if umur >= batas_umur:
        return "Kamu bisa menonton film ini! 🎉"
    else:
        return "Maaf, kamu belum memenuhi syarat untuk menonton film ini. "

def pilih_film():
    tampilkan_daftar_film()
    pilihan = int(input("Silakan pilih nomor film (1-6): "))
    umur = int(input("Masukkan umur kamu: "))
    
    if pilihan == 1:
        print(cek_kelayakan(umur, 18))
    elif pilihan == 2:
        print(cek_kelayakan(umur, 13))
    elif pilihan == 3:
        print(cek_kelayakan(umur, 0))
    elif pilihan == 4:
        print(cek_kelayakan(umur, 21))
    elif pilihan == 5:
        print(cek_kelayakan(umur, 13))
    elif pilihan == 6:
        print(cek_kelayakan(umur, 0))
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


pilih_film()
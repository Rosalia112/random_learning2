def hitung_harga_tiket(umur):
    harga_tiket_anak = 10.000
    harga_tiket_remaja = 15.000
    harga_tiket_dewasa = 25.000
    harga_tiket_lansia = 0

    if umur <= 12:
        return f"Harga tiket untukmu = {harga_tiket_anak:.3f}"
    elif umur <= 17:
        return f"Harga tiket untukmu = {harga_tiket_remaja:.3f}"
    elif umur <= 59:
        return f"Harga tiket untukmu = {harga_tiket_dewasa:.3f}"
    else:
        return print("harga tiket untukmu = " , harga_tiket_lansia , "Yap betul, untuk lansia GRATIS!!")

def main():
    while True:
        try:
            umur = int(input("Berapa umur kamu? "))
            print(hitung_harga_tiket(umur))
        except ValueError:
            print("Harap masukkan angka yang valid!")

        lagi = input("Apakah kamu ingin menambah tiket? (y/n): ").lower()
        if lagi != 'y':
            print("Terima kasih atas pesananmu!")
            break


main()
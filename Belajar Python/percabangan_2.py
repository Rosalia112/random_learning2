umur = int(input("Berapa umur kamu?"))

if umur<=12 : 
    print("kamu adalah anak-anak")
elif umur<=17 :
    print("Kamu adalah remaja")
elif umur<=59 :
    print("Kamu adalah dewasa")
else :
    print("Kamu adalah lansia")

def hitung_harga_tiket(umur):
harga_tiket_anak = 10.000
harga_tiket_remaja = 15.000
harga_tiket_dewasa = 25.000
harga_tiket_lansia = 0

if umur<=12 : 
    return f"harga tiket untukmu = {harga_tiket_anak:.3f}"
elif umur<=17 :
   return f"harga tiket untukmu = {harga_tiket_remaja:.3f}"
elif umur<=59 :
   return f"harga tiket untukmu = {harga_tiket_dewasa:.3f}"
else :
   return print("harga tiket untukmu = " , harga_tiket_lansia , "Yap betul, untuk lansia GRATIS!!")

def mnegulang():
    while True :
        try :
         int(input("Berapa umur kamu?  : "))
         print(hitung_harga_tiket(umur))
    except ValueError :
        print("Haraf masukan angka yang valid!!!")
    lagi = input("Apakah kamu ingin mengecek lagi? (y/n): ").lower()
        if lagi != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break



    


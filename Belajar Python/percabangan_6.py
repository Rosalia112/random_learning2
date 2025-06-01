total_belanja = float(input("Total brlanja kamu?"))
diskon1 = 20/100
diskon2 = 10/100

Jumlah_diskon1 = total_belanja * diskon1
Jumlah_diskon2 = total_belanja * diskon2

if total_belanja >= 5000000 :
    print("Kamu dapat diskon sebesar : " , Jumlah_diskon1)
elif total_belanja >= 250000 :
    print("Kamu apat diskon sebesar : " , Jumlah_diskon2)
else :
    "Kamu belum dapat dssikon :) "

if total_belanja >= 5000000 :
    print("Jadi total belanjaan kamu setelah dapat diskon adalah  : " , total_belanja - Jumlah_diskon1)
elif total_belanja >= 250000 :
    print("Jadi total belanjaan kamu setelah diskon adalah : " , total_belanja - Jumlah_diskon2)
else :
    "Silahkan dibayar :) "

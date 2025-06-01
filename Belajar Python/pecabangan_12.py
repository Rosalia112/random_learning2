jarak_tempuh = float(input("Berapa jarak tempuh : "))
print("Jarak tempuh : " , jarak_tempuh , "km")

def hitung_tarif_jarak_tempuh(jarak_tempuh):
    if jarak_tempuh >= 5 :
        return 5000
    elif jarak_tempuh >= 10 :
        return 4000
    elif jarak_tempuh >10 :
        return 3000
    else :
        print("Input anda tidak valid")
        return 0

tarif = hitung_tarif_jarak_tempuh(jarak_tempuh)
print("Tarif yang kamu dapatkan : " , tarif , "per jam")
print("Tarif yang harus di bayar : " , tarif * jarak_tempuh)
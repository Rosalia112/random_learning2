def menu_dan_harga():
    print("Selamat datang di Kedai Mie Ayam Kami!! ini dia daftar harganya : ")
    print("1. Mie ayam biasa : 10000")
    print("2. Mie ayam bakso : 18000")
    print("3. Mie ayam extra daging : 15000 ")
    print("4. Es teh : 5000")
    print("5. Es Jeruk : 5000")

menu_dan_harga()


umur_pelanggan = int(input("Berapa umur kamu? "))

if umur_pelanggan <= 13 :
    print("Kamu memenuhi syarat!!! Selamat Kamu dapat diskon sebesar 50%!!! " , )
elif umur_pelanggan >= 60 :
    print("Kamu memenuhi syarat!!! Selamat Kamu dapat diskon 30% ")
else :
    print("Kamu belum memenugi syarat, Kamu tidak dapat diskon ya huhu")

mie_ayam_biasa = 10000
mie_ayam_bakso = 18000
mie_ayam_ekstra = 15000
es_teh = 5000
es_jeruk = 5000

mie_ayam_biasa_yang_dipesan = float(input("Berapa jumlah mie ayam biasa yang anda pesan? ")) 
mie_ayam_bakso_yang_dipesan = float(input("Berapa jumlah mie ayam bakso yang anda pesan? ")) 
mie_ayam_ekstra_yang_dipesan = float(input("Berapa jumlah mie ayam ekstra yang anda pesan? "))
es_teh_yang_dipesan = float(input("Berapa jumlah es teh yang anda pesan? "))
es_jeruk_yang_dipesan = float(input("Berapa jumlah es jeruk yang anda pesan? "))

total_harga_mie_ayam_biasa_yang_dipesan = mie_ayam_biasa_yang_dipesan * mie_ayam_biasa
total_harga_mie_ayam_bakso_yang_dipesan = mie_ayam_bakso_yang_dipesan * mie_ayam_bakso
total_harga_mie_ayam_ekstra_yang_dipesan = mie_ayam_ekstra_yang_dipesan * mie_ayam_ekstra
total_harga_es_teh_dipesan = es_teh_yang_dipesan * es_teh
total_harga_es_jeruk_dipesan = es_jeruk_yang_dipesan * es_jeruk

def hitung_diskon(umur, total_belanja):
    if umur <= 13 :
        diskon = 0.50
    elif umur >= 60:
        diskon = 0.30 
    else:
        diskon = 0  

    total_diskon = total_belanja * diskon
    total_setelah_diskon = total_belanja - total_diskon

    return total_setelah_diskon

total_belanjaan = total_harga_mie_ayam_biasa_yang_dipesan + total_harga_mie_ayam_bakso_yang_dipesan + total_harga_mie_ayam_ekstra_yang_dipesan + total_harga_es_teh_dipesan + total_harga_es_jeruk_dipesan
print("Total belanjaan sebelum diskon : " , total_belanjaan)

hasil = hitung_diskon(umur_pelanggan, total_belanjaan)
print(f"Total belanja setelah diskon (Jika kamu dapat diskon): {hasil:.2f}")








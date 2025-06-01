#Percobaan operasi bilangan 01
jumlah_player_server01 = 142
jumlah_player_server02 = 358

total_player = jumlah_player_server01 + jumlah_player_server02

print("Total Player : " , total_player)

#Percobaan operasi bilangan 02
panjang = 34.6
lebar = 18.2

luas = panjang * lebar

print("Luas map:", luas , "m3")

#Percobaan operasi bilangan 03
average_online_players_01 = 3 #hours per day
average_online_players_02 = 2 
average_online_players_03 = 6

average_of_online_players = (average_online_players_01 + average_online_players_02 + average_online_players_03) / 3
print("Rata-rata waktu online player" , average_of_online_players , "Jam")

#Percobaan Operasi Bilangan 04
angka1 = float(input("Isikan bilangan :"))
angka2 = float(input("Isikan bilangan kedua :"))

if angka2 != 0:
    hasil = angka1/angka2
    print("Hasil pembagian : " , hasil)
    print("Hasil dari pembagian tadi : " , hasil , "Tipe datanya : " , type(angka1)  )
else:
    print("Pembagian tidal bisa jika penyebut bernilai Nol.")
    
        
#Percobaan Operasi Bilangan 05
jumlah_player_0001 = int(input("Masukan Jumlah Player Terbaru : "))
jumlah_player_0002 =int(input("Masukan Jumlah Player terbaru : "))
jumlah_player_0003 =int(input("Masukan Jumlah Player terbaru : "))

rata_rata_jumlah_player = jumlah_player_0001 + jumlah_player_0002 + jumlah_player_0003 / 3

print("Rata-rata jumlah player di semua server : " , rata_rata_jumlah_player)

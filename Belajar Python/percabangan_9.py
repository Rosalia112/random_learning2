def cari_posisi(no_punggung_pemain):
    if no_punggung_pemain % 2 == 0 :
        print("Posisi Attacker")
        if no_punggung_pemain >= 50 and no_punggung_pemain <= 100 :
          print("Dan kamu berhak dipilih menjadi kapten team ")
    elif no_punggung_pemain % 2 != 0 :
        print("Posisi Defender")
        if no_punggung_pemain >= 90 :
             print("Dan Playmaker")
    elif no_punggung_pemain % 2 != 0 and no_punggung_pemain % 3 == 0 and no_punggung_pemain % 5 == 0 :
        print("Kamu Keeper")

cari_posisi(int(input("Masukan nomor punggung anda agar bisa mengetahui posisis anda apa : ")))
cari_posisi(int(input("Masukan nomor punggung anda agar bisa mengetahui posisis anda apa : ")))
cari_posisi(int(input("Masukan nomor punggung anda agar bisa mengetahui posisis anda apa : ")))
cari_posisi(int(input("Masukan nomor punggung anda agar bisa mengetahui posisis anda apa : ")))
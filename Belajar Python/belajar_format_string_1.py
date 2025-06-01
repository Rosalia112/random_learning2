peringkat = 1
juara = "pemenang"
teks1 = "Rosa adalah %s dan %d" % (juara, peringkat)
print(teks1)

name = input("Masukan nama anda : ")
age = int(input("Berapa umur Anda : "))
hobby = input("Apa hobi anda : ")
origin = input("Darimana asal anda : ")
print("Halo Selamat Datang!! \nNama kamu : {} \nhobi kamu : {} \nberumur : {} \ndan berasal dari : {}\n" .format(name, hobby, age, origin))

my_campus = "UNIVERSITAS NUSA PUTRA"
print("Kampus saya adalah : {} " .format(my_campus))
soal_a = my_campus.split(" ")
print("Soal bagian a : " , my_campus[2])



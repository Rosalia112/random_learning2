#Contoh abs(), mengubah nilai negatif(-) menjadi nilai positif
def nilai_absolut(nilai) : 
    return abs(nilai) 

print(nilai_absolut(-10))
print(nilai_absolut(-900))

#abs() untuk menghitung selisih dua angka
def hasil_absolut(angka1,angka2) : 
    return abs(angka1 - angka2)

print(hasil_absolut(10,7))
print(hasil_absolut(2,9))
print("Selisih dari 4 dan 10 adalah : " , hasil_absolut(4,10))


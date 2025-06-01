jenisKendaraan = input("Masukan motor/mobil: ")
jamMasuk = int(input("Jam Masuk: "))
jamKeluar = int(input("Jam Keluar: "))

tarifPerjam = 0
if jenisKendaraan == "motor":
    tarifPerjam = 2000
elif jenisKendaraan == "mobil":
    tarifPerjam = 5000
else:
    print("Tidak menerima selain mobil atau motor")

if jamMasuk >= jamKeluar:
    print("Input Jam Masuk/Jam Keluar Salah!")
else:
    totalTarif = (jamKeluar - jamMasuk)*tarifPerjam

print(f"Tarif {jenisKendaraan}: {tarifPerjam}")
print(f"Lama Parkir: {jamKeluar-jamMasuk} jam")
print(f"Total Tarif Parkir: {totalTarif}")
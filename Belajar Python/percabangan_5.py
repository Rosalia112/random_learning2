nilai_rapor = float(input("Masukan nilai rapot : "))
penghasilan_ortu = float(input("Masukan banyaknya penghasilan ortu : "))

if nilai_rapor >= 90 and penghasilan_ortu <= 5000000 :
    print("Siswa ini layak dapat beasiswa penuh!!") 
elif nilai_rapor >= 80 and penghasilan_ortu <= 8000000 :
    print("Siswa ini layak , mendapatkan beasiswa 50%")
else :
    "Siswa ini tidak layak mendapatkan beasiswa"
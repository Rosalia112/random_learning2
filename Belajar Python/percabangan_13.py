nilai_coding = float(input("Masukan nilai coding peserta : "))

if nilai_coding >= 80 :
    print("Peserta LOLOS tes coding")
elif nilai_coding >= 60 :
    print("Hasil tes akan dipertimbangkan")
elif nilai_coding <60 :
    print("Peserta GAGAL tes coding")
else :
    print("Invalid input")


penilaian_interview = input("Masukan nilai peserta (A/B) : ")

if penilaian_interview == "A" :
    print("Peserta LOLOS tes interview")
elif penilaian_interview == "B" :
    print("Peserta GAGAL test interview")
else :
    print("Input invalid")

if nilai_coding >=80 and penilaian_interview == "A" :
    print("Selamat kamu berhasil jadi calon programmer")
elif nilai_coding >60 and penilaian_interview == "B" :
        print("Selamat kamu berhasil jadi calon programmer")
else :
     print("Peserta belum cocok jadi programmer")
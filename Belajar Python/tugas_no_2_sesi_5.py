my_campus = "UNIVERSITAS NUSA PUTRA SUKABUMI"
print("Kampus saya adalah : {} " .format(my_campus))

#soal bagian a
soal_a = my_campus.split(" ")
print(soal_a)
print("Soal bagian a : " , soal_a[2] .lower() , soal_a[1] .lower())

#soal bagian b
soal_b = my_campus.replace("U", "")
print("Soal bagian b : " , soal_b)

#Soal bagian c
soal_c = my_campus.split(" ")[::-1]
print("Soal bagian c : " , " ".join(soal_c))

#Soal bagian d
soal_d = "".join([word[0] for word in my_campus.split()])
print("Soal bagian d : " , soal_d)

#Soal bagian e 
soal_e = my_campus.split()
universitas = soal_e[0][-3:]
nusa_putra = soal_e[1][-2:] + soal_e[2][:2]
sukabumi = soal_e[3][-4:]
soal_bagian_e = f"{universitas} {nusa_putra} {sukabumi}"
print("Soal bagian e : " , soal_bagian_e)
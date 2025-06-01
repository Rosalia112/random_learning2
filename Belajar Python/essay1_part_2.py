def sandi_kalimat(kalimat):
    hasil = ""
    for huruf in kalimat:
        if huruf == 'A' or huruf == 'a':
            hasil += '4'
        elif huruf == 'E' or huruf == 'e':
            hasil += '3'
        elif huruf == 'I' or huruf == 'i':
            hasil += '7'
        elif huruf == 'S' or huruf == 's':
            hasil += '5'
        else:
            hasil += huruf
    return hasil

# Contoh penggunaan
kalimat_input = input("Masukkan kalimat: ")
output = sandi_kalimat(kalimat_input)
print("Hasil enkripsi:", output)

def sandi_kalimat(kalimat):
    ganti = {'A': '4', 'a': '4', 'E': '3', 'e': '3', 'I': '7', 'i': '7', 'S': '5', 's': '5'}
    return ''.join(ganti.get(huruf, huruf) for huruf in kalimat)

# Contoh penggunaan
kalimat_input = input("Masukkan kalimat: ")
enkripsi = sandi_kalimat(kalimat_input)
print("Hasil enkripsi:", enkripsi)
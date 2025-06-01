#Function tanpa pengembalian nilai
def party(name):
    print("Welcome to the Guild" , name)
    print("Let's be the strongest together")
    print("Together we aare Strong!!!")

party(input("What is your name new member? : "))
party(input("What is your name new member? : "))

def penjumlahan(x, y):
    hasil_penjumlahan = x + y
    return hasil_penjumlahan

hasil_pertambahan = penjumlahan(2, 4)
print("Hasil penjumlahan : " , hasil_pertambahan)

#function return perkalian dan pertambahan
def jumlah_ayam(ayam, kandang , terjual):
    ayam_terjual = ayam * kandang + terjual
    return ayam_terjual

ayam_terjual_wonosobo = jumlah_ayam(1000 , 6 , 10 )
print(ayam_terjual_wonosobo)
print("Ayam terjual di Wonosobo : " , jumlah_ayam(3400 , 9 , 90))

def creat_name(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = creat_name(input("enter your first name : "), input("enter your last name : ")) 
print(full_name)
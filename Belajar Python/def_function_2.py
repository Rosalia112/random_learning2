def server(*asia):
    print("Server terdapat di : " + asia[1] )

server("South Asia" , "East Asia" , "West Asia")

#Arbitary Arguments (*args)
def team_no(*numbers) : 
    for number_team in numbers :
        print(number_team)

team_no(1000 , 1001 , 1011, 1111)

#Keyword Arguments
def uid1(id1 , id2 , id3 , id4) : 
    print("The oldest player : " + id2)
    print("The newest player : " + id1)

uid1("8000001" , '8000002' , "80000004" , '8000005')

#(**kwargs)
def data_mahasiswa(**students) :
    for k, v in students.items() :
        print(f"{k} : {v}")

data_mahasiswa(nama="Rosa" , jururusan="TI" , angkatan="2024" )

#


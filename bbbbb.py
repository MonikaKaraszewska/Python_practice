import datetime

f = open("passwords.txt", 'r')


for i in f:
    i = i.strip()
    if i[0] == '1':
        lista = i.split(' ')
        print(lista)
        print("...",lista[1])
        print("&", lista[2][0])


urodziny = datetime.date(1999,2,1)
print(urodziny.month)


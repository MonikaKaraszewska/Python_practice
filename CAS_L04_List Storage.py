try:
    number = int(input("wprowadz pozytywnaliczbe: "))
    lista = []
    counter = 0
    while number>0:
        if number>0:
            lista.append(number)
            counter+=1
            number = int(input("Enter a number: "))
except:
    print("invalid number")
print("Cala Lista: ", lista)
print("Average: ", sum(lista) / counter)
print(sum(lista))
suma = 0
for i in lista:
    suma+=i
print(suma)
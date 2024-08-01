import random
lista =[]
step = 0

for i in range(30):
    p = random.randint(0, 3)
    lista.append(p)

while step<100:
    line = ''
    for z in lista:
        line += str(z)

    lista_sum = []
    new_value = []
    for i in range(len(lista)):
        n1 = 0
        n2 = 0
        n3 = 0
        if i == 0:
            n2 = lista[i]
            n3 = lista[i + 1]

        elif i>len(lista)-2:
            n1 = lista[i - 1]
            n2 = lista[i]

        else:
            n1 = lista[i - 1]
            n2 = lista[i]
            n3 = lista[i + 1]
        suma = n1 + n2 + n3
        lista_sum.append(suma)
        if suma > 3:
            nv = 0
        else:
            nv = suma
        new_value.append(nv)
        step+=1

    print("Line",line)
    print("Lista_sum",lista_sum)
    print("new_value",new_value)
    lista = new_value
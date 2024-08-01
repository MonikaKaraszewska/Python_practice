lista = [1,1]

suma = 0
for i in range(0,20):
    suma = lista[i] + lista[i+1]
    lista.append(suma)
print(lista)

aktualna = 1
poprzednia = 0
for i in range(0,20):
    suma = aktualna + poprzednia
    print(suma)
    poprzednia = aktualna
    aktualna = suma


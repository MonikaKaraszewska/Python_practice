given = [10, 20, 33, 46, 55]

print("...............................................lambda....")
wynik3 = filter(lambda x: x % 5 == 0, given)
given5 = list(wynik3)
print(given5)
print("podzielne na 5: ")
for l in given5:
    print(l)

print("...............................................sposob nr 2....")

def podzielne(lista):
    for x in lista:
        if x % 5 == 0:
            yield x
podzielneList = list(podzielne(given))
print(podzielneList)

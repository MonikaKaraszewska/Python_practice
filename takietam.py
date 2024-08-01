a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = set(a)
b = set(b)
c = a.intersection(b)
print(c)


c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lista = []
for i in c:
    if i in d:
        if i not in lista:
            lista.append(i)
print(lista)
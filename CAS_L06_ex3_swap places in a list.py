lis = [1, 2, 3, 4, 5, 6, 7]

# jakofunkcja:

def swaop_palces(lista):
    indx = -1
    dlugosc_listy = len(lista)
    zakres = dlugosc_listy // 2

    for i in range(dlugosc_listy):
        if i < zakres:
            lista[i], lista[indx] = lista[indx], lista[i]
            indx -=1
    return lista

print(swaop_palces([1, 2, 3, 4, 5, 6, 7]))
print(swaop_palces([4, 5, 6, 7, 8]))


print("..........................odpowiedz")
# -*- coding: utf-8 -*-
"""
@author: stme
"""


def reorder_list(l):
    # laufe bis zur Hälfte der Liste
    for i in range(int(len(l) / 2)):
        # wähle den erste, zweite, dritte, ... Index
        first_index = i  # 0, 1, 2,...

        # wähle den "gegenüberliegenden" Index: letzter, vorletzter,...
        second_index = - 1 * (i + 1)  # -1, -2

        # lese beide Werte und tausche sie aus
        val1 = l[first_index]
        val2 = l[second_index]
        l[first_index] = val2
        l[second_index] = val1

    # nach der Schleife sollte die Liste zurückgeliefert werden
    return l


print(reorder_list([5, 6, 7, 8]))
print(reorder_list([4, 5, 6, 7, 8]))
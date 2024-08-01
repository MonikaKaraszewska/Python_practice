'''https://www.w3resource.com/python-exercises/dictionary/'''

print("1. Write a Python script to sort (ascending and descending) a dictionary by value. ")

slownik = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
import operator

print(sorted(slownik.values()))
sorted_d = sorted(slownik.items(), key=operator.itemgetter(1))
print(sorted_d)

slownik[8] = 'mama'
print(slownik)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {**dic1,**dic2,**dic3}
print(dic4)
print('')
print("4. Write a Python script to check whether a given key already exists in a dictionary. ")
dick4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
klucz = 10

if klucz in dick4:
    print("true")
else:
    print("false")
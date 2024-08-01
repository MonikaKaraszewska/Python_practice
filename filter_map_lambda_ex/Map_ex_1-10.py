'''https://www.w3resource.com/python-exercises/map/index.php'''

print("1. Write a Python program to triple all numbers in a given list of integers. Use Python map. ")

liczny = [1,5,3,9,45,33,17,19]
nums = (1, 2, 3, 4, 5, 6, 7)

result = map(lambda x: x*3,liczny)
print(list(result))
result2 = map(lambda x: x*3,nums)
print(list(result2))

print('')
print("2. Write a Python program to add three given lists using Python map and lambda. ")
liczny = [1,5,3,9,45,33,17,19]
nums = [1, 2, 3, 4, 5, 6, 7]
licz  = [55,33,66,22,88]

wynik = map(lambda x,y,z:x+y+z,licz,liczny,nums)
print(list(wynik))

print('')
print("3. Write a Python program to listify the list of given strings individually using Python map.")
string3 = ['black', 'blue', 'white', 'rot', 'schwarz']

string33 = map(list,string3)
print(list(string33))
print('')
print("4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map")
lista4 = [1,2,3,4,5,6,7,8,9]
for i in lista4:
    indx = lista4.index(i)
    if indx % 2 != 0:
        z = i * 2
        print(z)
print('jednak o cos innego chodzilo')
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

wynik4 = map(lambda x,y:x**y,bases_num,index)
print(list(wynik4))
wynik45 = list(map(pow,bases_num,index))
print(list(wynik45))
print('')
print("5. Write a Python program to square the elements of a list using the map() function. ")

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wynik5 = map(lambda x:x*2,lista5)
print(list(wynik5))

print(pow(3,4))

print("6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.")

zbior = {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

# def krotka(litera):
krotkazb = []
litera = "E"
if litera.isupper:
    krotkazb.append(litera)
    litera2 = litera.lower()
    krotkazb.append(litera2)
    krotkazb = set(krotkazb)
    print(krotkazb)

print('')
def krotka(litera):
    krotkazb = []
    if litera.isupper:
        krotkazb.append(litera)
        litera2 = litera.lower()
        krotkazb.append(litera2)
    if litera.islower:
        litera3 = litera.upper()
        krotkazb.append(litera3)
        krotkazb.append(litera)
        krotkazb = set(krotkazb)
    return (krotkazb)

print(krotka('p'))


zbior = {'f', 'b', 'U', 'i', 'o', 'E', 'a'}

print(list(map(krotka,zbior)))

print('.................................odp')
def change_cases(s):
  return str(s).upper(), str(s).lower()

print(change_cases("t"))

k = 'p'

print(k.upper(),',', k.lower())

print('')
print("7. Write a Python program to add two given lists and find the difference between them. Use the map() function")

lista6 = [6, 5, 3, 9]
lista7 = [0, 1, 7, 7]

lista8 = list(map(lambda x,y:x+y,lista6,lista7))
lista9 = str(lista6)
print(lista9.replace(',',''))

print("7. Write a Python program to add two given lists and find the difference between them. Use the map() function")
print('')
print("8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings. ")
'''Original list and tuple:
[1, 2, 3, 4]
(0, 1, 2, 3)

List of strings:
['1', '2', '3', '4']

Tuple of strings:
('0', '1', '2', '3')'''

lst = [1, 2, 3, 4]
tpl = (0, 1, 2, 3)

lst=tuple(lst)
print(lst)

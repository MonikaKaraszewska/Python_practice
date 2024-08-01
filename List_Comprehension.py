# Find all of the numbers from 1-1000 that are divisible by 7

wynik = [i for i in range(1,100) if i%7 ==0]

print("wynik: ", wynik)


wynik1 = [i for i in range(1,100) if '3' in str(i)]
print("wynik1: ", wynik1)


string22 = "i liczymy ile jest spacji w stringu,hm ? no ile? "

spaces = [i for i in string22 if i==' ']
print("spaces: ", len(spaces))

spaces2 = [i for i in string22].count(' ')
print("spaces2: ",spaces2)

yellow = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
consonants = [i for i in yellow if i not in 'aeiou '] # spacje dodalam bo bez spacji ma wydrukowac
print(*consonants)

sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

result = [letter for letter in sentence if letter not in 'a,e,i,o,u, " "']
print("result ", *result)

items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
print(items.index('hi'))

krotka = [i for i in enumerate(items)]
print(krotka)

print(list(enumerate(items)))
#The enumerate() function adds a counter as the key of the enumerate object.
print(list(enumerate(wynik)))


# Find the common numbers in two lists (without using a tuple or set)
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common = [a for a in list_a if a in list_b]
print(common)

zdanie = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

liczby = [i for i in zdanie if i.isdigit()]

print(liczby)

result = ['even' if n%2 == 0 else 'odd' for n in range(20)]
print(result)



lambada = [(lambda x: "even" if x % 2 == 0 else "odd")(i) for i in range(20)]
print(lambada)

# Produce a list of tuples consisting of only the matching numbers in these lists
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]
# Result would look like (4,4), (12,12)

result33 = [(a, b) for a in list_a for b in list_b if a == b]
print("result33: ",result33)

result77 = [(i,i) for i in list_a if i in list_b]
print("result77: ", result77)


wypelniacz = 'On a summer day somner smith went simming in the sun and his red skin stung'
wypelniczlista = wypelniacz.split()
print(wypelniczlista)
efekt = [i for i in wypelniczlista if len(i)<4]
print(efekt)


# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
divisible = [number for number in range(1,100) if True in [True for x in range(2,10) if number % x == 0]]
print(divisible)

matrix = [[j for j in range(2)] for i in range(4)]

print("matrix: ", matrix)

s = '10 20 30 40 50'
s1 = s.split()
suma = sum([int(i) for i in s1])
print(suma)

# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

print(twoDMatrix[1])

# Generate transpose
trans = [[lista[item] for lista in twoDMatrix] for item in range(len(twoDMatrix[0]))]

print(trans)

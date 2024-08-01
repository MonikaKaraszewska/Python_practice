'''Find all of the numbers from 1-1000 that are divisible by 7'''

lista = range(1,101)
print(lista)
print([number for number in lista if '3' in str(number)])

string1 = "Count the number of spaces in a string"
c=0
for i in string1:
    if i==' ':
        c+=1
print(c)

d = [i for i in string1 if i ==" "]
print(len(d))

'''Create a list of all the consonants in the string '''

string2 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

cons = [i for i in string2 if i not in('aeiou ')]
print(cons)

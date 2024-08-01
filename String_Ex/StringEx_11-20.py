print('11. Write a Python program to remove characters that have odd index values in a given string. ')

string = "Python program to remove characters that have odd index values in a given string"

print(string[::2])

print('')
print('12. Write a Python program to count the occurrences of each word in a given sentence.')

string12 = "word Write a Python wordprogram to count the occurrences count Python of each word in a givenPython sentence word"
string122 = string12.split()
print(string122)
slownik ={}
for i in string122:
    r = string122.count(i)
    slownik[i]= r
print(slownik)
print('')
print('13. Write a Python script that takes input from the user and displays that input back in upper and lower cases. ')

userinput = "wpisz"
userinputPrint = userinput[::-1]
print(userinputPrint)
print(userinputPrint.upper())
print(userinputPrint.lower())

print("")
print("14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically). ")
'''Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red'''

slowa = "red, white, black, red, green, black"
slowa = slowa.replace(',','')
slowa2 = slowa.split()
slowa3 = []
for i in slowa2:
    if i not in slowa3:
        slowa3.append(i)
print(sorted(slowa3))

print('')
print("15. Write a Python function to create an HTML string with tags around the word(s). ")

'''add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'''

tag = 'i'
string15 = "Python"

print(f"<{tag}> {string15} </{tag}>")

def htchange(tag,string):
    return f"<{tag}> {string} </{tag}>"

print(htchange('b','python welcome'))

print('')
print('16. Write a Python function to insert a string in the middle of a string.')

'''Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}'''

znaki = '<<>>'
string16 = "PHP"
l = len(znaki)
d = l//2
odp16 = znaki[:2]+ string16 +znaki [2:]
print(odp16)

print("17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). ")
'''Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses'''

string17 = 'python'
c = string17[-2:]
print(c*4)

print('')
print("18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.")
'''Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt'''

string18 = 'ipy'
string188 = 'python'

e = len(string188)
def truncating(string):
    if e <= 3:
        print(string)
    else:
        print(string[:3])

truncating(string18)
truncating(string188)
truncating('characters')

print('')
print('19. Write a Python program to get the last part of a string before a specified character. ')
adres1 = 'https://www.w3resource.com/python-exercises/string'
adres2 = 'https://www.w3resource.com/python'

import re
print(re.findall('(?<=.com/).+$',adres2))

c = re.split('/',adres1)
d = len(c)
print(c[d-1:])

print('')
print("20. Write a Python function to reverse a string if its length is a multiple of 4")

string20 = "abcd"
p = len(string20)
print(p)
if p%4==0:
    print(string20[::-1])
else:
    print(string20)


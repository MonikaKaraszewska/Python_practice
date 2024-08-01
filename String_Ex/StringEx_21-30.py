print("21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. ")
'''Python')  # Output: 'Python' (Not all uppercase)
('PyThon')  # Output: 'PYTHON' (All uppercase) '''

str1 = 'Python'
str2 = "PyThon"
def ex21(string):
    c = 0
    for i in string[:4]:
        if i.isupper():
            c += 1
    if c >= 2:
        print(string.upper())
    else:
        print(string, "not all upper")

ex21(str1)
ex21(str2)
print('')
print("22.Write a Python program to sort a string lexicographically. ")

str3 = 'quickbrown'
str4 = 'w3resource'

print(sorted(str3.lower()))

print('')
print("23. Write a Python program to remove a newline in Python. ")

str5 = "python\npython"
print(str5)
print(str5.replace('\n',' '))
str55 = "\npython"
print(str55.lstrip())

print('')
print("25. Write a Python program to create a Caesar encryption. ")

import string

alfabet = string.ascii_uppercase
print(alfabet)
zdanie ='Kot'

# zdanie = zdanie.upper()
# print(zdanie)
# listazaszyfrowane = []
# indexLiteryAlfabet = alfabet.index(zdanie)
# zaszfrowane = alfabet[indexLiteryAlfabet-3]
# listazaszyfrowane.append(zaszfrowane)
# print(listazaszyfrowane)
zdanie = zdanie.upper()
listazaszyfrowane = []
for i in zdanie:
    if i.isalpha():
        alfabet = string.ascii_uppercase
        indexLiteryAlfabet = alfabet.index(i)
        zaszfrowane = alfabet[indexLiteryAlfabet - 3]
        listazaszyfrowane.append(zaszfrowane)
    else:
        listazaszyfrowane.append(i)
print(listazaszyfrowane)

szyfr =''.join(listazaszyfrowane)
print(szyfr)

print("..................kurdenooooo.................")
def zamianiaLiter(zdanie):
    alfabet = string.ascii_uppercase
    zdanie = zdanie.upper()
    listazaszyfrowane = []
    for i in zdanie:
        if i.isalpha():
            alfabet = string.ascii_uppercase
            indexLiteryAlfabet = alfabet.index(i)
            zaszfrowane = alfabet[indexLiteryAlfabet - 3]
            listazaszyfrowane.append(zaszfrowane)
        else:
            listazaszyfrowane.append(i)
    szyfr = ''.join(listazaszyfrowane)
    print(szyfr)

zamianiaLiter('Write a Python program to create a Caesar encryption')

print('')
print('26. Write a Python program to display formatted text (width=50) as output. ')
x = 3.1415926
print('+%.2f' % x)
print('{:=+8.2f}'.format(x))
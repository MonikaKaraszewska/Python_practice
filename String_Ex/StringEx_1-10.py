'''https://www.w3resource.com/python-exercises/string/'''

print("1. Write a Python program to calculate the length of a string. ")

string = "Write a Python program to calculate the length of a string."
print(len(string))
count = 0
for s in string:
    count+=1
print(count)

print('')
print('2. Write a Python program to count the number of characters (character frequency) in a string. ')
diki ={}
for i in string:
    if i in 'abcdefghijklmnopqrstuvxyz':
        c = string.count(i)
        if i not in diki:
            diki[i] = c
print(diki)
print("...........................")
diki2 ={}
for i in 'abcdefghijklmnopqrstuvxyz':
    # if i in string:
        c = string.count(i)
        if i not in diki2:
            diki2[i] = c
print(diki2)

print('')
print("3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. \n If the string length is less than 2, return the empty string instead. ")

'''Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''

string = 'w3resource'
SampleString = 'w3'
sampleString2 = 'w'


def towFirst2Last(string):
    if len(string)>=2:
        print(string[0:2] + string[-2:])
    else:
        print("empty string")

towFirst2Last(string)
towFirst2Last(SampleString)
towFirst2Last(sampleString2)

print('')
print('4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to \\$, except the first char itself')
string4 = 'trestart'
def string44(string4):
    p = string4[0]
    string99 = string4.replace(p,'$') # zamieniłam wszytskie r
    string99 = p + string99[1:] #dodalam pierwsze r i reszte stringa od indeksu1.
    return string99

print(string44(string4))

print('')
print('5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. ')
string5 = 'abc', 'xyz'
print(string5[0])

print(string5[0][0:2],string5[1][0:2],string5[1][0:2],string5[0][0:2])
string55 = string5[1][0:2] +string5[0][2:]
string66 = string5[0][0:2] +string5[1][2:]

print(string55)
print(string66)
string5566 = (string55," " + string66)
print(string5566)

print('')
print("6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). "
      "\nIf the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged")
'''Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'''

string6 = 'abc'
string61 = 'string'
string63 = 'sb'
def ing(string6):
    ln = len(string6)
    if ln <3:
        return "za krótki"
    if ln >=3 and string6.endswith('ing'):
        string6+="ly"
        return string6
    if ln>=3:
        string6+='ing'
        return string6

print(ing(string6))
print(ing(string61))
print(ing(string63))

print(' ')
print("7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. \nIf 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.")
'''Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'''
import re
string7 = 'The lyrics is not that poor!'
string71 = 'The lyrics is poor!'

print(re.findall(r'not .+ poor',string7))
print((re.sub(r'not .+ poor','good',string71)))
# print(re.sub(r"(?:'is')'poor'",'poor',string71))

def poor(string):
    if re.findall(r'not .+ poor',string):
        return re.sub(r'not .+ poor', 'good', string)
    else:
        return string

print('def poor: ',poor(string7))
print('def poor: ',poor(string71))

print(' ')
print("8. Write a Python function that takes a list of words and return the longest word and the length of the longest one")
'''Sample Output:
Longest word: Exercises
Length of the longest word: 9'''

stringWords = "Write a Python function that takes a list of words and return the longest word and the length of the longest one"
words = stringWords.split(' ')
odp = ["PHP", "Exercises", "Backend"]
print(words)
wynik = {}
# def longest(words):
for i in words:
    l = len(i)
    wynik[i]= l
for k, w in wynik.items():
    if w is max(wynik.values()):
        print(k, w)
print('')
print("9. Write a Python program to remove the nth index character from a nonempty string. ")

string9 = 'character from a nonempty string'
index = 2
strin98 = string9[0:2]
print(strin98)
efekt = strin98+string9[3:]
print(efekt)

def usun(string,index):
    string0 = string[:index]
    string90 = string0+string[index+1:]
    return (string90)

print(usun(string9,2))

print('')
print("10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.")
string10 = 'character'
x=len(string10)
print(x)
char1= string10[0]
print(char1)
char2 = string10[x-1]
print(char2)
string77 = char2 +string10[1:x-1]+char1
print(string77)
odp10 =string10[-1:] + string10[1:-1] + string10[:1]
print('odp:',odp10)
print(string10[:1])

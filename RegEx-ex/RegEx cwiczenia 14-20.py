import re

print("14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores. ")
string = " jsjuwyAWkmmA172_928JJnsks  jsjuwyAWk_mmA1 jsj&%uwyAWkmmA1"

stringW = re.findall(r"((\w)+)", string)
print(stringW)

print(" ")
print("15. Write a Python program that starts each string with a specific number. ")

ciagliczb = '6278512'

spr = re.match('5',ciagliczb)
print(spr)

if spr:
    print("Match")
else:
    print("no maych")
print("mmmmmmmmmmmmmmmmmmmmmmmmmmm")
def spr(ciagliczb):
    wzor = re.compile(r'5')
    if wzor.match(ciagliczb):
        print("jest Match")
    else:
        print("NO")

spr(ciagliczb)

print('......16. Write a Python program to remove leading zeros from an IP address. ......................')
adres = '000.192.1508.1.308'

wzorBez0 = re.search(r"([1-9]+\.\d+\.\d+\.\d+)", adres).group()

print(wzorBez0)

zwor2 = re.sub('0','',adres,)
print(zwor2)
print(' ')

print("............17. Write a Python program to check for a number at the end of a string. ..............")
adres = '000.192.1508.1.30889'
h = re.search(r'8$',adres)
print(bool(h))
# czy string konczy sie na liczbe czy nie

zawor = "and4n djdie6 djd"
f = re.search("[0-9]$",zawor)
print("f: ", bool(f))
print('  ')

print(".....18. Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string...............")

givenString = "Exercises number 1, 12, 13, and 3456 are important"
gS = re.findall('(\s+[0-9]{1,3},?)', givenString)
print(gS)

givenString2 = "Exercises number 1, 12, 13, and 3456 are important"
gS2 = re.finditer('(\s+[0-9]{1,3},?)', givenString2)
for i in gS2:
    print("Finditer: ", i.group())


import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 3455 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))
print('')

print("............19. Write a Python program to search for literal strings within a string.......")

Sampletext ='The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'")
sampleodp = re.findall('fox|dog|horse',Sampletext)
print(sampleodp)

words = ['fox', 'dog', 'horse']
def wordSearch(words,sampletext):
    for i in words:
        if re.search(i,Sampletext):
            print("ok",i)
        else:
            print('NO', i)

print("... to z mojej funkcji...")
wordSearch(words,Sampletext)

print(' ')
print('20. Write a Python program to search for a literal string in a string and also find the location within\nthe original string where the pattern occurs. ')

samplezdanie = 'The quick brown fox  jumps over the lazy dog.'
wyraz = 'fox'

def findwyraz(wyraz,samplezdanie):
    x = re.search(wyraz,samplezdanie)
    d = x.start()
    e=x.end()
    if x:
        print(wyraz, d,e)
    else:
        print("NO matxh")

findwyraz(wyraz,samplezdanie)




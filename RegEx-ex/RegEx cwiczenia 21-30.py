import  re
print("21. Write a Python program to find the substrings within a string. ")

sampleText = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

for x in re.findall(pattern,sampleText):
    print(x)

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)

print('')
print("22. Write a Python program to find the occurrence and position of substrings within a string. ")

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

dom = re.finditer((pattern),text)
for i in dom:
    print(i.group(),i.span())

print(' ')
print("23. Write a Python program to replace whitespaces with an underscore and vice versa. ")

zdanie = "Write a Py_thon pro_gram to replace white_spaces w3455ith an under_scor 344 and vice versa"

zdanieRepl = re.sub(r'(\w{3}) (\d{3})','\\2-\\1',zdanie)
print("jestUdalosie: ", zdanieRepl)

zdanierepl2 = zdanie.replace('_', '*')
print(zdanierepl2)
zdanie3 = zdanierepl2.replace('*','')
print(zdanie3)
print(' ')

print("24. Write a Python program to extract year, month and date from an URL.  ")
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

datesearch= re.findall(r'((\d\d\d\d)/(\d\d)/(\d\d))', url1)
print(datesearch)
odp = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url1)
print('odp: ',odp)

print(' ')
print("25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format. ")
dt = '2013-12-17'
odp25 = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
print(odp25)
print(' ')
print("26. Write a Python program to match if two words from a list of words start with the letter 'P'. ")

listOfWords = ['mama','papa', 'kota', 'rok', 'pies', "Pawel", 'plot', 'okop']
listOfWordsString = str(listOfWords)
kurdenoooo = 'mama, kota,rok, pies, , okop, tok, pot '
pWords = re.findall(r"[Pp]\w+", kurdenoooo)
print("pWords: ",pWords)
f = len(pWords)
if f ==2:
    print("match")
if f>2:
    print("jest wiecej ")
if f<2:
    print("jest mnije")

words = ["Python PHP", "Java JavaScript", "c c++"]

print("27. Write a Python program to separate and print the numbers in a given string. ")
text = "Ten 10, Twenty 20, Thirty 30"
text55 = re.findall(r'\d+',text )
print(text55)

text = "Ten 10, Twenty 20, Thirty 30"
result = re.split(r"\D+", text)
# Print results.
for element in result:
    print(element)
print("  ")
print("28. Write a Python program to find all words starting with 'a' or 'e' in a given string ")

text4 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
text44 = re.findall(r"\W[aeAE]\w* ",text4)
print(text44)

text45 = re.findall(r"[aeAE]\w*",text4)
print(text45)

print("  ")
print("29. Write a Python program to separate and print the numbers and their position in a given string. ")
text6 = "Ten 10, Twenty 20, Thirty 30"
for m in re.finditer(r"((\d)+)",text6):
    print(m, m.span())
print("  ")
print("30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string. ")
text7 = "Write a Python program to abbreviate Road in a given string"
text77 = text7.replace("Road","Rd")
print(text77)
text78 = re.sub('Road',"RD",text7)
print(text78)


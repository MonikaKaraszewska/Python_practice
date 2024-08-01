import re
print("51. Write a Python program to insert spaces between words starting with capital letters. ")

text = "words starting with capital letters"
text2 = text.title()
text3 = text2.replace(' ','')
print(text3)

text4 = re.findall('([A-Z][a-z]+)',text3)
text5 = ' '.join(text4)
print(text5)

print('.....................odp51..................')
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

print('')
print("52. Write a Python program that reads a given expression and evaluates it. ")

print('')
print("53. Write a Python program to remove lowercase substrings from a given string")
string = "WordsStartingWithCapitalLetters"
print(re.sub('[^A-Z][a-z]+','',string))
print(re.sub('[a-z]','',string))

print('')
print("54. Write a Python program to concatenate the consecutive numbers in a given string")

string54 = "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1  6. Please have your identification ready."
print(re.findall(r'(\d+\s+\d+)',string54))
print(re.findall(r'([A-Za-z\s]+)(\d+\s+\d+)([.\s]*)([A-Za-z\s]+)',string54))
print(re.sub(r'(\d+)(\s+)(\d+)','\\1''\\3', string54))

print(".........................odp...")
txt = "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready."
print("Original string:")
print(txt)
new_txt = re.sub(r"(?<=\d)\s(?=\d)", '', txt)
print('\nAfter concatenating the consecutive numbers in the said string:')
print(new_txt)
print('')
print("55. Write a Python program to convert a given string to snake case. ")
string55 = "Write a Python program to convert a given string to snake case."
print("1:", re.sub(r'\s',"_",string55))
string555 = "Write a PythonProgram to convert a givenString to snake case."
string5556 = re.split(r'([A-Z]?[a-z]+[\s]?) ',string555)
print("2:",string5556)

string5567 = '_'.join(string5556)
print("3:",string5567.lstrip())
print("4:",re.sub("(?<=_)_",'',string5567))

print('')
str556 = [i for i in re.split(r'([A-Z]?[a-z]+[\s]?) ',string555) if i !='']
print("5:",str556)
str5567 = '_'.join(str556)
print("6:",str5567)

print('')
print("56. Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.")

obj1 = ('Red', 'Green', 'Black', 'Orange')
obj2 = ([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5])
obj3 = ([1, 2, 3], 'Java')
obj4 = ({10, 100}, 'Python')

obj1len = [len(i) for i in obj1]
print(max(obj1len))

lista=[]
for i in obj3:
  c = len(i)
  lista.append(c)
print(max(lista),i)

print("def")
def objekt(object):
  lista2 = []
  for i in object:
    c = len(i)
    lista2.append(c)
  return (max(lista2), i)

print(objekt(obj4))
print(objekt(obj3))
print(objekt(obj2))
print(objekt(obj1))

print("")
print("57. Write a Python program that checks whether a word starts and ends with a vowel in a given string. Return true if a word matches the condition; otherwise, return false.")
'''
Sample Data:
("Red Orange White") -> True
("Red White Black") -> False
("abcd dkise eosksu") -> True'''

slowo1 = "Red Orango White"
slowo2 = "Red White Black"
slowo3 = "abcd dkise eosksu"

print(bool(re.findall(r'\s?[aeiou][A-Z|a-z]+\w+[aeiou]\s?',slowo1,flags=re.IGNORECASE)))



def test(text):
	return bool(re.findall(r'[/^[aeiou]$|^([aeiou]).*\1$/', text))

print(test(slowo3))
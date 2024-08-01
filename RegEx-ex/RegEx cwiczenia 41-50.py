import re

print("42. Write a Python program to find URLs in a string. ")
textUrl = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
print(re.findall(r'\bhttp[s]?.+com',textUrl))

chunks = re.split(r'(http[s]?\W{,3}\w+\.com)',textUrl)
print([i for i in chunks if i.startswith('https') or i.startswith('http')])

# chunks2 =
# print([i for i in chunks2 if i.startswith('https') or i.startswith('http')])
textOdp = 'https://www.w3resource.com/python-exercises/re/python-re-exercise-42.phphttps://www.geeksforgeeks.org/python-list-comprehension/'

print(re.findall(r'(http[s]?\W*\w*\W*\w*(?:.com|.org))',textOdp))

print('')
print("43. Write a Python program to split a string into uppercase letters. ")

string43 = "Write a Python program to split a string into uppercase letters"
print(string43.title())
print(string43.upper())
text43 = "PythonTutorialAndExercises"

chunk1 = re.split('([A-Z]{,1}[a-z]+)',text43)
print('moje43: ',[i for i in chunk1 if i !=''])

text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))

print('')
print('44. Write a Python program to do case-insensitive string replacement. ')


print(re.escape('https://www.finxter.com/'))
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))
print(' ')
string44 =  "Write PHP a Python php program to split a string pHP into Php uppercase letters"
print('odp44: ',re.sub('php','php',string44,flags=re.IGNORECASE))

print('')
print('46. Write a Python program to find all adverbs and their positions in a given sentence')

sample_text = "Clearly, he has no excuse for such behavior sadly."

sample = re.finditer(r'(\w+ly)',sample_text)
for i in sample:
    print(i)

print('')
print("47. Write a Python program to split a string with multiple delimiters. ")
sample_text47 = "Clearly, he has no ex;cuse for 'such' behavior sadly."
print(re.split(",|;|[']", sample_text47))

print('')
print("48. Write a Python program to check a decimal with a precision of 2. ")
x=7
y=9
f =7/9
print(round(f,2))

print('')
print("49. Write a Python program to remove words from a string of length between 1 and a given number. ")

string49 = "Write a Python program to remove words from a string of length between 1 and a given number"
print(re.sub(r'\b\w{1,4}\b','',string49))

import re
text = "The quick brown fox jumps over the lazy dog."
# remove words between 1 and 3
shortword = re.compile(r'\W*\b\w{1,3}\b')
print(shortword.sub('', text))

print(re.sub(r'\b\w{1,3}\b','',text))

print('')
print("50. Write a Python program to remove the parenthesis area in a string. ")
sampleDataList = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
sampleData = "example (.com)"

odp50 =  re.split('[^\b\w+\b]\(\.com\)',sampleData)
print(odp50)

print([i for i in re.split('[^\b\w+\b]\(\.com\)',sampleData) if i !=''])

print('.............')

for i in sampleDataList:
    for x in re.split('[^\w+]\(\.com\)',i):
        if i != '':
            print(x,end=' ',)

print([z for z in re.sub('[^\w+]\(\.com\)','',sampleData)])

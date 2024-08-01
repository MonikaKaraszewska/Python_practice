import re
print("31. Write a Python program to replace all occurrences of a space, comma, or dot with a colon. ")

text = 'Python Exercises, PHP exercises.'
text1 = re.sub(r'\s|,|\.',':',text)
print(text1)
text11 = re.finditer(r'([\bEe]\w+[ises\b])',text)
print(text11)
for i in text11:
    print(i)
txt2 = re.sub("[ ,.]", ":", text)
print(txt2)

print(' ')
print(" 32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon. ")
txt3 = re.sub("[ ,.]", ":", text,2)
print(txt3)
print(' ')

print('33.34.35. Write a Python program to find all five-character words in a string.  ')
text3 = 'The quick brown fox jumps over the lazy dog.'
text33 = re.findall(r"\w{3,5} ",text3)
print(text33)
print(re.findall(r"\b\w{5}\b", text3))
print(re.findall(r"\b\w{4,}\b", text3))
print(' ')
print(' 36.37 Write a Python program to convert a camel-case string to a snake-case string.  ')

kamel = "CamelCaseStringConvertToSnakeCase"


def camel_to_snake(text):
    import re
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    print(str1) # dlaczego od razu nie wstawił wszystkich _
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()


print(camel_to_snake(kamel))

print('..38. Write a Python program to extract values between quotation marks of a string. ......')

text6 = '"Python", "PHP", "Java"'
print(re.findall(r'"(.*?)"',text6)) # w pierszej kolejnosci wyswietla to co jest w grupie!!!!
print(text1.replace('"',''))

print('')
print("39. Write a Python program to remove multiple spaces from a string. ....")
text9 = "Pyth  on Exerci  ses, PHP exerci  ses"
print(re.sub('\s{2}','',text9))

print('')
print("40. Write a Python program to remove all whitespaces from a string. ")
text10 = "Pyth  on Exerci  ses, PHP exerci  ses"
print(re.sub(r'(\s+)','',text10))

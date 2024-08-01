'''https://www.kaggle.com/code/albeffe/regex-exercises-solutions'''

import re

print("1) Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).")

string1 = "a string contains only a certain set of characters177 388 832"
string2 = " characters (in this case a-z, A-Z and 0-9)"
string3 = "characters177"

print(not bool(re.findall('[^A-Za-z0-9. ]',string2)))

print("odp")
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))
print(is_allowed_specific_char(string2))

print('')
print("2) Write a Python program that matches a string that has an a followed by zero or more b's")

string4 = 'abababa'
string5 = 'a'
string6='abbbbbab'
print(re.findall('ab*?',string4))


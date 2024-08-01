# Exercise 15: Remove special symbols / punctuation from a string
import re
str1 = "/*Jon is @developer & musician"
# print(str1.split())
# symbols =[]
#
# for i in str1:
#     if i.isalpha() or i == '&' or i ==' ':
#         i = True
#     else:
#         symbols.append(i)
#         for z in symbols:
#             if z in str1:
#                 str1 = str1.replace(z,'')
# print(str1)
#

#Exercise 18: Replace each special symbol with # in the following string

str1 = '/*Jon is @developer & musician!!'

symbols = []
for i in str1:
    if i.isalpha() or i ==' ':
        i = True
    else:
        symbols.append(i)
        for z in symbols:
            if z in str1:
                str1 = str1.replace(z,'#')
print(str1)



str1 = 'I am 25 years and 10 months old'
str1 = str1.lower()
resStr1 = re.sub(r'[a-z]', '', str1)
resStr1 = re.sub(r' ', '', resStr1)
print(resStr1)

str11 = 'I am 55 years and 5 months old'

res = "".join([item for item in str11 if item.isdigit()])
print(res)

zum = ''
str33 = 'I am 34 years and 9 months old'
for i in str33:
    if i.isdigit():
        zum = zum.join(i)
        print(zum,end='')

print ("........................................")
str5 = "/*Jon is @developer & musician since 1999"

str555 = ''.join([i for i in str5 if i.isdigit()])
print(str555)
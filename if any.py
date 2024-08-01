#EExercise 17: Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"
str2 = str1.split()
print(str2)

print(".......moje..........")
zz=[]
for i in str2:
    for z in i:
        if z.isdigit():
            if i not in zz:
                zz.append(i)
print(zz)

print("..........odp.......................odp")
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)


res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(d.isalpha() for d in item) and any(d.isdigit() for d in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
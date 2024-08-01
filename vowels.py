string = input("zdanie:")
vowels= "aeiou"
vowels = list(vowels)
for i in vowels:
    v = string.count(i)
    print('\n',"{} - {}".format(i,v))


# total = []
# tot = 0
# string = input("zdanie: ")
# vowels = "aeiou"
# vowels = list(vowels)
# for i in vowels:
#     v = int(string.count(i))
#     total.append(v)
#     print(v)
#     tot += v
#     print("serio?",tot)
# print(total)

# total = 0
# string = input("zdanie: ")
# string = string.lower()
# vowels = "aeiou"
# vowels = list(vowels)
# for i in vowels:
#     v = int(string.count(i))
#     total += v
# print("\n", "wszystkich samoglosek jest: ", total)


# sentence = input("Input: ")
# sentence = sentence.lower()
# countA = sentence.count('a')
# countE = sentence.count('e')
# countI = sentence.count('i')
# countO = sentence.count("o")
# countU = sentence.count('u')
# total = countA +countU + countO + countI + countE
# print("\nTotal = ", total)
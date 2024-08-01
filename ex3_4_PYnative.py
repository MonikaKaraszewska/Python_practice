#ex3
str = "pynative"
str1 = (input("Napisz cos: "))
print(str1[::2])

print ('...................................................1..')
size = len(str1)
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", str1[i])

print("pynative".lstrip("pyna"))

print ('...................................................2..')

native = "pynative"
print(native[:4])
native = native.removeprefix("pyna")
print(native)

native = "pynative"
native = native[4:]
print("a teraz: ", native)
native = native[:1] + native[2:]
print("??: ", native)
native = native.replace('n', " ")
print(native)

print ('......................................zad4.............3')

cut = input("wpisz: ")
print(cut)
cut = cut[4:]
print(cut)



print ('...................................................odpowiedz. zad4.')

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
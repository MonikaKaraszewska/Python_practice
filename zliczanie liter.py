zdanie = "Ala ma kota"
zdanie = zdanie.lower()
zdanie1 = zdanie.replace(" ", '')
print("wszystkich liter jest: ", len(zdanie1))
zdanie2 = zdanie.split()
print(zdanie2)
print("Wyrazow jest: ", len(zdanie2))
print(zdanie.count("a"))

for x in "abcdefghijklmnopqrstuwxyz":
    y = zdanie.count(x)
    if y > 0:
        print(x,":",y)



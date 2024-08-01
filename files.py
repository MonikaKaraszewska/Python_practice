f = open('names.txt', 'r')
f.close()

f = open('names.txt', 'r')
counter = 0
for name in f:
    counter+=1
print(counter)
    # print(name[:-1]) # bez [:-1] wydrukuje linie przery pomiedzy imionami
f.close()

print("................")
f = open('names.txt', 'r')
lea = 0
luke = 0
darth = 0
for name in f:
    if name[:-1] == "Lea":
        lea+=1
    if name[:-1] == 'Luke':
        luke +=1
    if name == "Darth":
        darth +=1
    if name[:-1] == "Darth":
        darth += 1
#     else:
#         print(name)
print(f"Lea = {lea}\nLuke = {luke}\nDarth = {darth}")
f.close()


print("....")
lea1 = 0
luk1 = 0
darth1 = 0
f = open('names.txt', 'r')
for name in f:
    name = name.strip()
    if name == "Lea":
        lea1 += 1
    if name == 'Luke':
        luk1 += 1
    if name == "Darth":
        darth1 += 1
#     else:
#         print(name)
print(f"Lea = {lea1}\nLuke = {luk1}\nDarth = {darth1}")
f.close()


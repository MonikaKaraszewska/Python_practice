#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

for i in l1:
    idx = l1.index(i)
    if idx % 2 == 1:
        l3.append(l1[idx])
for z in l2:
    idz = l2.index(z)
    if idz % 2 == 0:
        l3.append(l2[idz])
print(l3)


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)
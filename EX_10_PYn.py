list1 = [10, 20, 25, 30, 35] #odd
list2 = [40, 45, 60, 75, 90] #even


list3 = []
for i in list1:
    if i % 2  != 0:
        list3.append(i)
for z in list2:
    if z % 2 == 0:
        list3.append(z)
print(list3)

print("........................................drugi moj")


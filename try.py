my_list = list([6, 4, 6, 6, 8, 12])

for item in my_list:
    my_list.remove(6)

print(my_list)


my_list = list([2, 4, 6, 8, 10, 12])

# remove range of items
# remove item from index 2 to 5
del my_list[2:5]
print(my_list)
# Output [2, 4, 12]

# remove all items starting from index 3
my_list = list([2, 4, 6, 8, 10, 12])
del my_list[3:]
print(my_list)
# Output [2, 4, 6]
print("......")
l1 = [10, 20, 30, 40, 50]
print(l1.index(10, 0, 5))
l2 = [60, 70, 80, 60]

l2 = l1.copy()
print(l2)

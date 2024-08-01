print ("......................Exercise 6: Count the total number of digits in a number...")
# Write a program to count the total number of digits in a number using a while loop.

number =5009890765

counter = 0
while number > 0:
    counter += 1
    number = number//10
print(counter)


liczba = 67890
liczba = str(liczba)
print(len(liczba))
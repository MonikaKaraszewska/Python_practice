'''Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop'''


'''numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(1000):
    if i % 5 == 0:
        if i == 150:
            continue
        if i > 500:
            break
        print(i)'''



numbers = [12, 75, 150, 180, 145, 524, 50]
for i in numbers:
    if i % 5 == 0:
        if i > 500:
            break
        if i > 150:
            continue

        print(i)

print("..................................................")
numbers = [12, 75, 150, 180, 145, 524, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)

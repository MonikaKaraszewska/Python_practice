
print('................................Exercise 4: Write a program to print multiplication table of a given number.......')
n = 2
# n = int(n)

for i in range(0,11):
    if i > 0:
        suma = i * n
        print(suma)

print('..................................Exercise 3: Calculate the sum of all numbers from 1 to a given number...........')
suma = 0
for i in range(0,31):
        suma = suma +i
print(suma)

## odp
s = 0
n = 465
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)


print('..................................Exercise 2: Print the following pattern...........')
for i in range(1,7):
    for j in range(i):
        print(j, end=' ')
    print('\r')

print('..................................Exercise 1: Print First 10 natural numbers using while loop')
z=1
while z <10:
    print(z)
    z+=1
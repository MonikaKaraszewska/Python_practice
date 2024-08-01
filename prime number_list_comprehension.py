a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = 128

divisors_list = []

for i in range(1,b+1):
    if b % i == 0:
        divisors_list.append(i)
if len(divisors_list) ==2:
    print(f"{b} is a prime number")
else:
    print(f"{b} is not a prime number because it has more than two divisors {divisors_list}" )

print('.................')
new_lista = [i for i in range(1,b+1) if b %i == 0]
if len(new_lista) == 2:
    print(f"{b} is a prime number")
else:
    print(f"{b} is not a prime number because it has more than two divisors  {divisors_list}" )






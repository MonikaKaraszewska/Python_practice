import random

secret_number = random.randint(1,10)

print(secret_number)

user=0

while user!=secret_number:
    user = int(input("I have picked the number from 1 to 10. Guess the number"))
    if user < secret_number:
        print('Too low')
    elif user > secret_number:
        print('Too high')
    else:
        print(f"YES!! the number is {secret_number}")

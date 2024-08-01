import random

computer_player_second_throw = random.randint(1,6)
computer_player_first_throw = random.randint(1,6)
user_first_throw = int(input("Throw a dice and write the number: "))
user_second_throw = int(input("Throw a dice again and write the second number: "))

user_sum = user_second_throw + user_first_throw
computer_sum = computer_player_first_throw + computer_player_second_throw

if user_sum > computer_sum:
    print(f"You are the winner. Your points {user_sum}, computer's points {computer_sum}")
elif user_sum == computer_sum:
    print(f"It's a draw. No winners")
else:
    print(f"Computer is the winner. Your points {user_sum}, computer's points {computer_sum}")



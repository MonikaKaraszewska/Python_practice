import random

lista = ['rock', 'paper', 'scissors']
computer_choice = random.choices(lista)
user_choice = 'paper'
print(computer_choice)
print(computer_choice[0] == user_choice)

if computer_choice[0] == 'rock' and user_choice == 'scissors':
    print(f"Computer is the winner!!!. {computer_choice[0]} beats {user_choice}")

if computer_choice[0] == 'scissors' and user_choice == 'rock':
    print(f"YOU are the winner!!!. {user_choice} beats {computer_choice[0]}")

if computer_choice[0] == user_choice:
    print(f"It's a draw, because your choice is  {user_choice} and computer's choice is {computer_choice[0]}")

if computer_choice[0] == 'scissors' and user_choice == 'paper':
    print(f"Computer is the winner!!!. {computer_choice[0]} beats {user_choice}")

if computer_choice[0] == 'paper' and user_choice == 'scissors':
    print(f"YOU are the winner!!!. {user_choice} beats {computer_choice[0]}")

if computer_choice[0] == 'paper' and user_choice == 'rock':
    print(f"Computer is the winner!!!. {computer_choice[0]} beats {user_choice}")

if computer_choice[0] == 'rock' and user_choice == 'paper':
    print(f"YOU are the winner!!!. {user_choice} beats {computer_choice[0]}")
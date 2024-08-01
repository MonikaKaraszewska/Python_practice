import random

start_game = (input("chcesz zagrac w gre? y/n? "))

# user_input = '2356'

comp_guess = []

cow = 0
bull = 0
for i in range(0,4):
    cg = random.randint(0, 9)
    comp_guess.append(cg)

def user_input_list(string):
    user_guess = []
    for k in user_input:
        user_guess.append(int(k))
    return user_guess

# print("comp Guess: ",comp_guess)
idx = 0
while start_game != 'y' and start_game != 'n':
    print("write 'y' for yes / 'n' for no")
    start_game = (input("chcesz zagrac w gre? y/n? "))

if start_game == 'y':
    print('guess a 4-digit number. For every digit you guessed correctly in the correct place, you have a “cow”. For every digit you guessed correctly in the wrong place is a “bull.” ')
    gramy = input("Gotowy? y/n? ")
    while gramy != 'y' and gramy != 'n':
        print("if gotowy - write 'y' for yes / 'n' for no")
        gramy = input("Gotowy? y/n? ")
    if gramy == 'y':
        user_input = input("Write 4-digit number: ")

        while user_input.isdigit() == False:
            print("not a number")
            user_input = input("Write 4-digit number: ")
        else:
            user_guess = user_input_list(user_input)
            print("computer guess: ", comp_guess)

            while len(user_guess) < 4 or len(user_guess) > 4:
                user_input = input("4-digit number no more no less. Try again: ")
                user_input_digit = int(user_input)
                user_guess = user_input_list(user_input)
            for e in user_guess:
                if e == comp_guess[idx]:
                    cow += 1

                    comp_guess[idx] = '*'
                idx += 1

                if e in comp_guess:
                    count_bulls = comp_guess.count(e)
                    bull += count_bulls
            print("cows: ", cow)
            print("bulls: ", bull)


    else:
        print("hmmmm??")
else:
    print("szkoda, moze nastpnym razem")




print("user_guess: ", list(user_input))
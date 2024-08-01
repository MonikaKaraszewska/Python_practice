import random
lista=[]

for i in range(30):
        p = random.randint(0,3)
        lista.append(p)


user_poz = 0
comp_poz = 0

while user_poz <30 and comp_poz <30:
    pos_U = " " * user_poz *2
    pos_U += "U"
    print(pos_U)

    pos_C = " " * comp_poz * 2
    pos_C += "C"
    print(pos_C)

    line=''
    for e in lista:
        line += str(e) + '|'
    print(line)

    answer = input("1 or 2: ")

    if answer == '1':
        user_score = random.randint(1,2)
    else:
        user_score = lista[user_poz]
    comp_score = random.randint(1,2)

    user_poz += user_score
    comp_poz += comp_score

if user_poz > comp_poz:
    print("You are the winner")
elif user_poz < comp_poz:
    print("Computer is the winner")
else:
    print("Draw")
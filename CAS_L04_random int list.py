import random

lista_user_input=[]

for i in range(1,4):
    user_input = input(f"podaj liczbe {i}: ")
    lista_user_input.append(int(user_input))
print(lista_user_input)
maks = max(lista_user_input)
minim = min(lista_user_input)
print("ilosc znaków: ",len(lista_user_input))
for k in random.randint(minim, maks):
    print(k)
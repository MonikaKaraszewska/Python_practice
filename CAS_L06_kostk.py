import random

print("\u2680 \u2681 \u2682 \u2683 \u2684 \u2685")
kostka = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
print(kostka)

kosta1_lista = []
kosta2_lista = []

number_of_ones = 0
number_of_pairs = 0
number_of_following_The_same_pairs = 0
following_pairs = False
numbers_of_following_pairs = 0
counter = 0
suma = 0
while counter < 15:
    counter += 1
    kostka1 = random.randint(1, 6)
    kostka2 = random.randint(1, 6)
    print(f"runda {counter}: {kostka[kostka1-1]} ({kostka1}) and {kostka[kostka2-1]}({kostka2})")
    if kostka1 == 1:
        number_of_ones +=1
    if kostka2 == 1:
        number_of_ones += 1

    if kostka1 == kostka2:
        following_pairs = True
        number_of_pairs += 1
        kosta2_lista.append(kostka1)
        kosta2_lista.append(kostka2)

        if following_pairs == True:
            numbers_of_following_pairs +=1


        if kosta1_lista == kosta2_lista:
            number_of_following_The_same_pairs +=1
            kosta1_lista = kosta2_lista
    else:
        following_pairs = False

        kosta2_lista.clear()

    suma += kostka2
    suma += kostka1
average_number = suma / counter *2



print(f"The number of ones: {number_of_ones}")
print(f"The number of following the same pairs: {number_of_following_The_same_pairs}")
print(f"The average number: {average_number}")
print(f"The number of following pairs: {numbers_of_following_pairs}")
print(f'number of all pairs {number_of_pairs}')




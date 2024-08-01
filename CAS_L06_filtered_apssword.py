import os
file_passwords = open('passwords.txt', 'r')

# counter = 0
#
# for i in file_passwords:
#     n1 = int(i[0])
#     n2 = int(i[2])
#     litera = i[4]
#     password = i[6::]
#     number_of_letters = password.count(litera)
#     if number_of_letters >= n1 and number_of_letters <= n2:
#         counter+=1
# print(counter)

filtered_passwords = open('filtered_passwords.txt', 'r')

counter1 = 0
niepoprawne = 0
wszytskie = 0
for i in filtered_passwords:
    white_space_split = i.split(' ')
    split_mysl = white_space_split[0].split('-')
    n1 = int(split_mysl[0])
    n2 = int(split_mysl[1])
    letter = white_space_split[1]
    haslo = white_space_split[2]
    number_of_letters = haslo.count(letter[:-1])

    if number_of_letters >= n1 and number_of_letters <= n2:
        counter1 += 1
        wszytskie+=1
    else:
        niepoprawne+=1
        wszytskie+=1

print(f"Poprwane hasla: {counter1}\nNiepoprawne hasla: {niepoprawne}\nWszytskie hasla: {wszytskie}")

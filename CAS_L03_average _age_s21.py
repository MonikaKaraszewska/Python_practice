numbers_of_people = int(input("Howmany person are the in teh group? "))

ages_of_people = input("Write ages of those persons, separated only by space: ")

ages_int = ages_of_people.split(' ')

ages_int1 = list((int(i) for i in ages_int))
max_age = max(ages_int)
min_age = min(ages_int1)
ages_sum = sum(ages_int1)

average_age = ages_sum // numbers_of_people
print(f"Maximum age {max_age}.\nMinimum age {min_age}.\nAverage age {average_age}")

print("........................................................................................................")

number_of_people = 3
suma = 0
min_age = 100
max_age=0
for i in range(1,number_of_people+1):
    age = int(input(f"podaj wiek nr {i}: "))
    suma+=age
    if age <min_age:
        min_age = age
    else:
        max_age = age
print("sredni wiek to: ", suma/number_of_people)
print('max: ', max_age)
print("min: ", min_age)
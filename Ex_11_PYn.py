#If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

numb = 7536
print("Given number", numb)
numb = str(numb)
numb = numb[::-1]

for i in numb:
    print(i, end=" ")


print("\n"'..............................................odpowiedz')
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
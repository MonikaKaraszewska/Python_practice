# number1 = 80
# number2 = 30
# sum = number1 + number2
# multi = number1 * number2
#
# if multi <= 1000:
#     print(multi)
# else:
#     print(sum)

def ex1 (num1, num2):
    multi = num1 * num2
    if multi <= 1000:
        return multi
    else:
        sum = num1 + num2
        return sum

print(ex1(20,30))
print(ex1(40,30))








ODP
#
# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2
#
# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)
#
# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)
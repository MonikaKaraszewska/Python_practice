numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# xp = numbers_x[0]
# xk = numbers_x[-1]
# yp = numbers_y[0]
# yk = numbers_y[-1]
#
# print(xp)
# print(xk)
# print(yp)
# print(yk)


def trufalse (lista):
    if lista[0] == lista[-1]:
        print("Given list: ",lista,"\n","The result is: ", True)
    else:
        print("Given list: ",lista,"\n","The result is: ", False)

trufalse(numbers_x)
trufalse(numbers_y)
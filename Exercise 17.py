# '''Exercise 17: Find the sum of the series upto n terms'''
#
# n= 5
#
# suma = 0
#
# for i in range(1,n+1):
#     s = str(2)
#     num = s*i
#     num = int(num)
#     suma+=num
# print(suma)


def series(nb, n):
    razem = 0

    for i in range(1, n + 1):
        s = str(nb)
        num = s * i
        num = int(num)
        razem += num
    return razem

print(series(3,5))
# print('.......')
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for i in my_list:
#     if my_list.index(i)%2 !=0:
#         print(i)
#
# for i in my_list[1::3]:
#     print(i, end=" ")
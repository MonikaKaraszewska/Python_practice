liczby = {0,1,2,3,4,5,6,7,8,9,10}
for i in liczby:
    i2 = i-1
    if i2<0:
        i2 = 0
    i3 = i2 + i
    print("Current Number:",i, " ", "Previous Number:", i2, "  ", "Sum", i3)



liczby2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def exercise(x):
    x1=x-1
    if x1>=0:
        return x1+x
    return 0

wynik = list(map(exercise, liczby2))
print(wynik)



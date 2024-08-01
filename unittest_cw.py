

# numbers_x = [10, 20, 30, 40, 10]
numbers_y = ["jk", 65, 35, 75, 60]

# print(len(numbers_y))
# print(numbers_x[-1])

def czy_sa_rowne_original(numbers_y):

    if isinstance(numbers_y[0],str):
        if numbers_y[0].isalpha():
            print(f'{numbers_y[0]} , - to nie jest LIczba')

        if isinstance(numbers_y[-1],str):
            if numbers_y[-1].isalpha():
                print(f'{numbers_y[-1]} , - to nie jest LIczba')

    if isinstance(numbers_y[0],(int)) and isinstance(numbers_y[-1],(int)) :
        if numbers_y[0] == numbers_y[-1]:
            print(f'{numbers_y[0]} , {numbers_y[-1]} - sa rowne')
            # return True
        else:
            print(f'{numbers_y[0]} , {numbers_y[-1]} - NIE sa rowne')
            return False
    else:
        a = int(numbers_y[0])
        b = int(numbers_y[-1])
        if a == b:
            print(f'{a} , {b} - sa rowne')
            return True
        else:
            print(f'{a} , {b} - NIE sa rowne')
            return False




print ("......................................1111111111111111.................")

print('')
print('')
print('')
print('------------------------------------------------')
for i in range(0,11):
    for n in range (0,11):
        if n == 0 and i == 0:
            print("     ", end=' ')
            continue
        else:
            if i == 0:
                suma = n
            elif n == 0:
                suma = i
            else:
                suma = i * n

        if suma <10:
            if n == 0:
                print('| ', suma, end='')
            else:
                print('  ', suma, end='')
        elif suma > 99:
            print('', suma, end='')
        else:
            if n == 0:
                print('| ' + str(suma), end='')
            else:
                print(' ', suma, end='')
        if i == 0 and n == 10:
            print('\n------------------------------------------------',end='')
        if i > 0 and (n == 0 or n == 10):
            print(' |', end='')
    print('')
print('------------------------------------------------')
print('')
print('')
print('')
print ("............................................22222222222222222...........")

for i in range(0,11):
        if i >0:
            for n in range (1,11):
                if i > 0:
                    suma = i * n

                if suma <10:
                    print(suma, end='   ')
                else:
                    print(suma, end='  ')
        print('\r')

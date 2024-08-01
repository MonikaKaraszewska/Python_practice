question = input("Please think of a number from 1 to 10. Ready?")
if question == 'yes':
    question = input("Is the number greater than 5? ")
    if question == 'yes':
        question = input("Is the number greater than 7? ")
        if question == 'yes':
            question = input("Is the number greater than 9? ")
            if question == 'yes':
                print("The chosen number is 10")
            elif question == 'no':
                question = input("Is the number equal to 8? ")
                if question == 'yes':
                    print("The chosen number is 8")

        elif question == 'no':
            question = input("Is the number equal to 5? ")
            if question == 'yes':
                print("The chosen number is 5")
            elif question == 'no':
                question = input("Is the number equal to 6? ")
                if question == 'yes':
                    print("The chosen number is 6")

    elif question == 'no':
        question = input("Is the number greater than 3? ")
        if question == 'yes':
            print("The chosen number is 4")
        else:
            question = input("Is the number equal to 3 ? ")
            if question == 'yes':
                print("The chosen number is 3")
            else:
                question = input("Is the number greater than 1? ")
                if question == 'yes':
                    print("The chosen number is 2")
                else:
                    print("The chosen number is 1")










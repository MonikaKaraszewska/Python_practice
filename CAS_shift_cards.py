string = "hallo world of python xyz"

def shift_cards(string,shift_number):
    line = ''
    for i in string:
        if i.isalpha():
            kodenumber = ord(i)
            new_letter_code = kodenumber + shift_number
            if new_letter_code <= 122:
                new_letter = chr(new_letter_code)
                line += new_letter
            else:
                k = kodenumber + shift_number
                new_shift_number = k-122
                new_letter = chr(64 + new_shift_number)
                line += new_letter
        else:
            line += i

    return line

print(shift_cards(string,15))
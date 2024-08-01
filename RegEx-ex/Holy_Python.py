'''https://holypython.com/advanced-python-exercises/project-regular-expressions-regex/'''
import re

print("{}, {}, {}".format(1,2,3))

str="One year has {} months, {} weeks and {} days.".format(12,56,365)
print(str)

letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}

print('%(h)s %(e)s %(l)s %(p)s' % letter_to_morse)
import string

print('.............................count characters 1..............')

lista2 = ["abc", "de", "fgh"]

def count_char(list):
    letters = 0
    for i in list:
        lenght_einzeln = len(i)
        letters += lenght_einzeln
    print(letters)


count_char(lista2)


print(".....................")
string2 = "Hello Weltttttt"
def count_char1(list):
    letters = 0
    for i in list:
        length_einzeln = len(i)
        letters += length_einzeln

    if isinstance(list,str):
        letters = len(list)
    print(letters)


count_char1(lista2)
count_char(string2)

print("...........................................lobal / local variables")

a, b = 'one','two'
print("outer a,b=", a, b)
def function():
    # a, b = 1, 2
    a = 1
    print ("inner a,b=", a, b)

function()
print("outer a,b=", a, b)

print("...........................................count words Folie 15")
zdanie = "Write a function that receives a text and counts the words"
text = "Guido van Rossum began working on. Python in the late 1980s as a successor to the ABC programming language and first released it in 1991"

def count_words(string):
    words = string.split(' ')
    words_number = len(words)
    print(words_number)

def count_sentences(string):
    words_list = string.split('.')
    number_sentences = len(words_list)
    print(number_sentences)

count_words(zdanie)
count_sentences(text)

print("..........................................................shif cards Folie 17")


string17 = "Hallo"

def shift_cards(string,shift_number):
    line = ''
    for i in string:
        kod_numbr = ord(i)
        new_letter = chr(kod_numbr + shift_number)
        line += new_letter
    return line

print("new word: ",shift_cards(string17,2))


print("''''''''''''''''''''counting letters folie 19")

text19 = "hallo world of python"

def counting_letters(text):
    text = text.upper()
    alfabet = string.ascii_uppercase
    for i in alfabet:
        ilosc = text.count(i)
        print(f"{i} : {ilosc}")

print("..........counting_letters2................................")
def counting_letters2(text):
    text = text.upper()
    alfabet = string.ascii_uppercase
    for i in alfabet:
        ilosc = 0
        for t in text:
            if t == i:
                ilosc+=1
        print(f"{i} : {ilosc}")

counting_letters2(zdanie)





print("................german r english")
text = "Write a function that receives a text and counts the words"
text_German = "Python unterstützt mehrere Programmierparadigmen, z. B. die objektorientierte, die aspektorientierte und die funktionale Programmierung."


def language(text):
    text = text.upper()
    text = text.replace(' ', '')
    len_text = len(text)
    alfabet = string.ascii_uppercase
    for i in alfabet:
        ilosc = text.count(i)
        procent = (ilosc / len_text) *100
        # print(f"{i} : {procent}")

        if i == 'E':
            if procent >= 12.702:
                print(f"german {i} = {procent}")
            else:
                print(f"english {i} = {procent}")
        if i == 'O':
            if procent <= 7.507:
                print(f"german {i} = {procent}")
            else:
                print(f"english {i} = {procent}")

        if i == 'T':
            if procent <= 6.15:
                print(f"german {i} = {procent}")
            else:
                print(f"english {i} = {procent}")

language(text_German)
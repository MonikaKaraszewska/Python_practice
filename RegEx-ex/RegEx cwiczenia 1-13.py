import re
print("1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).")
string1 = "Asia lat 15, Madzia lat 13, i Pawcio lat 8 maja 3koty"
string1match = re.findall('[A-Za-z0-9]+', string1)
print(string1match,'\n')

print("2. Write a Python program that matches a string that has an a followed by zero or more b's.")
string2 = "a acb ab aab abbb"
string22 = re.findall('ab*', string2)
print(string22,'\n')

print("3. Write a Python program that matches a string that has an a followed by one or more b's. ")
string33 = re.findall('ab+', string2)
print(string33,'\n')

print("4. Write a Python program that matches a string that has an a followed by zero or one 'b'.  ")
string44 = re.findall('ab?', string2)
print(string44,'\n')

print("5. Write a Python program that matches a string that has an a followed by three 'b'. ")
string5 = "a acb ab aab abbb aabbbb"
string55 = re.findall('ab{3}', string5)
print(string55,'\n')

print("6. Write a Python program that matches a string that has an a followed by two to three 'b'. ")
string6 = "abb a acb ab aab abbb aabbbb aabbb"
string66 = re.findall('ab{2,3}', string6)
print(string66,'\n')

print("7. Write a Python program to find sequences of lowercase letters joined by an underscore. ")
string7 = "asia_joanna lat 15, madzia_madzik lat 13, i pawcio_pawel lat 8 maja 3koty"
string77 = re.findall("[a-z]+_[a-z]+", string7)
print(string77,'\n')

print("8. Write a Python program to find the sequences of one upper case letter followed by lower case letters. ")
string8 = "Asia_joanna lat 15, Madzia_madzik lat 13, i Pawcio_pawel lat 8 maja 3koty"
string88 = re.findall("[A-Z]+[a-z]+", string8)
print(string88,'\n')

print("9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'. ")
string9 = "Asiab arab krach akra4b krab amb akreb strat ab a%&b Awa*&b raf magda"
string99 = re.findall(r"[A|a][\w]+b", string9)
print(string99,'\n')

print('nierozumiem .............................dlaczego coznaczy *? razem????')
# '?' = 0 or 1
# '*' = 0 or more
#id laczego nie moge wstawic znakupoczatkiu i konca "^a.*b$"
string099 = re.findall("a.*b", string9)
print(string099,'\n')
string1099 = re.findall("a.*?b", string9)
print(string1099,'\n')

print("11. Write a Python program that matches a word at the end of a string, with optional punctuation.")

string11 = "Asia woz ma 15 lat, madzia ma 13 lat, i Pawcio ma 8 lat. koza kasza wazon wasza zadek"
string111 = re.findall(r"\d\slat\S*", string11)
print(string111,'\n')

print("12. Write a Python program that matches a word containing 'z'. ")
#dlaczego jak usune pierwszy znak zapytania to nie wyszukujemislow wasza i kasza
string122 = re.findall(r"[\s]?[a-z]*[z]+[a-z]*[\s]?", string11)
print(string122,'\n')

# dlaczwego wyszukal woz ma????
print("odpowiedz pyt.12")
string123 = re.findall(r'\w*z.\w*',string11)
print(string123,'\n')

print("13. Write a Python program that matches a word containing 'z', not the start or end of the word. ")

string13 = "Asia woz ma 15 lat, madzia ma maz 13 lat zanim, i Pawcio ma 8 lat. koza kaszaz wazon wasza zadzekz"
string133 = re.findall(r"[\w]+[z]+[\w]+", string13)
print('string133: ',string133,'\n')

string334 = re.findall(r"\Bz[a-z]+z?[a-z]+\Bz?", string13)
print('string134: ',string334,'\n')

string135 = re.findall(r"\Bz[\w]+[z]+[\w]+z\B", string13)
print('string135: ',string135)


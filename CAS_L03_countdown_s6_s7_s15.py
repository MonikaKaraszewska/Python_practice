

user_input = int(input("Write a number: "))
x= user_input +1
while x >0:
    x-=1
    print(x)


for i in range(user_input,-1,-1):
     print(i)


print("COUNT LETTERS s15")

sentence = "Python is an interpreted,high-level and general-purpose programming language."
#
# print(sentence.count('e'))
# counter = 0
# for i in sentence:
#     if i == 'e':
#         counter+=1
# print(counter)

indx =0
count =0
while len(sentence)>indx:

    letter = sentence[indx]
    if  letter == 'e':
        count+=1
    indx += 1
print(count)

print('....')


lista_e = [i for i in sentence if i =='e']
print(len(lista_e))


print("............")

print(list(range(6)))
print(list(range(1, 6)))
print(list(range(1, 6, 2)))
print(list(range(5, 0, -1)))
print(list(range(5, -1, -1)))

sentence = "Python is an interpreted, high-level and general-purpose programming language."

count=0
for i in sentence:
    if i =='e':
        count+=1
print(count)


lista_e = [i for i in sentence if i =='e']
print(len(lista_e))


# user_input = 10
#
# while user_input >=0:
#     print(user_input)
#     user_input-=1

# Syntax: list(range(<start_value>[, <end_value>][, <step>]))
# returns a list (sequence) of integers including the start_value
# and excluding the end_value incrementing by step
# by default, step = +1 and start_value = 0
# list(range(<end_value>)) # returns a list of integers
# from 0 to end_value-1
print(list(range(5))) # returns [0, 1, 2, 3, 4]
list(range(1, 5)) # returns [1, 2, 3, 4]
#Creating ranges with steps
list(range(0, 10, 2)) # returns [0, 2, 4, 6, 8]
list(range(10, 0, -2)) # returns [10, 8, 6, 4, 2]
print(list(range(0, -10, -1))) # ret. [0, -1, ..., -7, -8, -9]
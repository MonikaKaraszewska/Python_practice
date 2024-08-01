
'''Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]'''

print("............................swap .........approach 1...........")
lista11 = [23, 65, 19, 90]


lista11[0], lista11[2] = lista11[2], lista11[0]

print("lista11",lista11)

lista44 = [1, 2, 3, 4, 5]

lista44[1], lista44[4] = lista44[4], lista44[1]

print("lista44:", lista44)

print('.......................................swap .........approach 2.........................')
def swapPositions(list, pos1, pos2):
        # popping both the elements from list
        first_ele = list.pop(pos1)
        second_ele = list.pop(pos2 - 1)

        # inserting in each others positions
        list.insert(pos1, second_ele)
        list.insert(pos2, first_ele)

        return list
# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))

print('.......................................swap .........approach 3.........................')

def swapPositions(list, pos1, pos2):
        # Storing the two elements
        # as a pair in a tuple variable get
        get = list[pos1], list[pos2]

        # unpacking those elements
        list[pos2], list[pos1] = get

        return list


# Driver Code
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))

print('....................................listek get.......................')

listek = [23, 24, 65, 57, 19, 90, 66]
blabla = listek[0], listek [5]
print(blabla)
listek[5],listek[0] = blabla
print(listek)
a, b = 'one', 'two'
c = 4
print("outer a,b=", a, b)
def function():
    # a, b = 1, 2
    c = a
    a = c
    print ("inner a,b=", a, b)

function()
print("outer a,b=", a, b)

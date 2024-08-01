
"""a = "This is a secrete message"
print(a)
a= a[::-1]
print(a)
a=a.replace(" ", "0b")
print(a)
a= "101" + a +'3456'
print(a)

print("\n", "Decrypting")

a=a.lstrip("101")
print(a)
a=a.rstrip(("3456"))
print(a)
a= a.replace("0b", " ")
print(a)
a = a[::-1]
print(a)"""

secrete = "tramsgferagfuoy"
secrete = secrete.replace("gf", " ")
print(secrete)
secrete = secrete[::-1]
print(secrete)
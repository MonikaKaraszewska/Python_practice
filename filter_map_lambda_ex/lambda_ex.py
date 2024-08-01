'''https://www.geeksforgeeks.org/python-lambda-function-to-check-if-value-is-in-a-list/?ref=lbp'''

print("write a Python program to check if the value exists in the list or not using the lambda function.")

arr = [1, 2, 3, 4]
v = 8
x = lambda arr, v: True if v in arr else False

if (x(arr, v)):
    print("Element is Present in the list")
else:
    print("Element is Not Present in the list")

p = "kskks"
print(p.upper())
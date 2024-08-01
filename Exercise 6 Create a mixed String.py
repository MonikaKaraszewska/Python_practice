# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the
# first char of s1, then the
# last char of s2, Next,
# the second char of s1 and
# second last char of s2, and so on. Any leftover chars go at the
# end of the result.

s1 = "Abc"
s2 = "Xyz"

k1 = len(s1)-1
k2 = len(s2)
str4 =""
i= 0

# for i in range(0,k1-1):
    # if i <= k1:
for e in range(0,k2+1):
    e = -e
    if e<0:
        str3= s1[i] + s2[e]
        str4+=str3
        # e += 1
        i += 1
print(str4)


print('     ............defini........................')




def mixString(s1,s2):
    k1 = len(s1)-1
    k2 = len(s2)
    str4 =""
    i= 0

    for e in range(0,k2+1):
        e = -e
        if e<0:
            str3= s1[i] + s2[e]
            str4+=str3
            # e += 1
            i += 1
    print(str4)


s1 = "Abc"
s2 = "Xyz"
mixString(s1,s2)
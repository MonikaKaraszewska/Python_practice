sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89, 99,77,88,55, 4, 6 ,90, 45, 78, 67, 52, 41]

d = len(sample_list)
c = d // 3
c1 = c
e =0
for i in sample_list:
    list44 = sample_list[e:c]
    print(list44[::-1])
    if c>d:
        break
    e+=c1
    c+=c

print('........................meza')
d = len(sample_list)
c = d // 3
e =0
for i in range(3):
    list44 = sample_list[e:e+c]
    print(list44[::-1])

    e+=c

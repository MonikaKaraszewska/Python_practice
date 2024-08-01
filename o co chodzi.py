str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str_list22 = []

for i in str_list:
    if i is None:
        continue
    if i == '':
        continue
    str_list22.append(i)

print(str_list22)

print('.....................odp')
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)
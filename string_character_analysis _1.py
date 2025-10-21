str = 'Hello World'
str = str.lower().replace(' ','')
str_list = {}

for i in str:
    if i not in str_list:
        str_list[i] = 1
    else:
        str_list[i] +=1
print(str_list)

str_input = input().split(' ')
new_list = []

for i in str_input:
    current_num = abs(float(i))
    new_list.append(current_num)
print(new_list)

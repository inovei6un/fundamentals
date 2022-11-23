single_string = input().split(" ")
new_list = []

for num in single_string:
    if int(num) > 0:
        new_list.append(-int(num))
    else:
        new_list.append(abs(int(num)))
print(new_list)

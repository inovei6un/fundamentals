input_string = input().split(" ")
rounded_list = []

for i in input_string:
    current_num = round(float(i))
    rounded_list.append(current_num)

print(rounded_list)

string_one = [i for i in input().split(", ")]
string_two = [j for j in input().split(", ")]
substring_list= list()

for element1 in string_one:
    for element2 in string_two:
        if element1 in element2:
            if element1 not in substring_list:
                substring_list.append(element1)
print(substring_list)

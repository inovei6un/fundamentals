multiple = int(input())
counts = int(input())

new_list = []

for i in range(1, counts + 1):
    new_list.append(i * multiple)
print(new_list)

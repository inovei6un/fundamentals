some_list = [i for i in input().split(' ')]
even_list = list()

for num in some_list:
    if len(num) % 2 == 0:
        print(num)

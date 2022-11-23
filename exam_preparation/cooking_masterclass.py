import math

budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_egg = float(input())
price_for_apron = float(input())
free_package_flour = 0
flour_counter = 0

for counter in range(1, students + 1):
    flour_counter += 1
    if flour_counter % 5 == 0:
        free_package_flour += 1

sum_apron = price_for_apron * math.ceil((students + 20 / 100 * students))
sum_eggs = price_for_egg * 10 * students
sum_flour = price_for_flour * (students - free_package_flour)
check_sum = sum_flour + sum_eggs + sum_apron

if check_sum > budget:
    print(f"{check_sum - budget:.2f}$ more needed.")
else:
    print(f"Items purchased for {check_sum:.2f}$.")

list_of_nums = list(map(int, [i for i in input().split(', ')]))
positive = list()
negative = list()
even = list()
odd = list()

for num in list_of_nums:
    if num >= 0:
        positive.append(num)
        if num % 2 == 0:
            even.append(num)
        elif num % 2 != 0:
            odd.append(num)
    elif num < 0:
        negative.append(num)
        if num % 2 == 0:
            even.append(num)
        elif num % 2 != 0:
            odd.append(num)

positive = ", ".join(list(map(str, positive)))
negative = ", ".join(list(map(str, negative)))
even = ", ".join(list(map(str, even)))
odd = ", ".join(list(map(str, odd)))

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")

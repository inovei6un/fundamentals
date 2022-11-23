from math import floor


def calculator(n, m, operator):
    result = 0
    if operator == "+":
        result = n + m
    if operator == "-":
        result = n - m
    if operator == "*":
        result = n * m
    if operator == "/":
        result = f'{floor(n / m)}'
    if operator == "%":
        result = n % m
    return result


num_one = int(input())
operate = input()
num_two = int(input())

print(calculator(num_one, num_two, operate))

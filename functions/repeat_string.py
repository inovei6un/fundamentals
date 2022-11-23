string = input()
counter = int(input())

repeater_string = lambda a, b: a * b

result = repeater_string(string, counter)
print(result)
lines = int(input())
even_list = list()
odd_list = list()
negative_list = list()
positive_list = list()

for i in range(lines):
    number = int(input())
    if number % 2 == 0 or number == 0:
        even_list.append(number)
    if number % 2 != 0:
        odd_list.append(number)
    if number < 0:
        negative_list.append(number)
    if number > 0 or number == 0:
        positive_list.append(number)

command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)

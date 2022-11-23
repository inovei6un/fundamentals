elements = input().strip()
elements = list(map(str, elements.split(' ')))
command = input().strip()

number_of_moves = 0

while command != "end":
    expand_command = command.split(' ')
    number_of_moves += 1
    index1 = int(expand_command[0])
    index2 = int(expand_command[1])
    if index1 == index2 or index1 < 0 or index1 >= len(elements) or index2 < 0 or index2 >= len(elements):
        mid = len(elements) / 2
        elements.insert(int(mid), f"-{number_of_moves}a")
        elements.insert(int(mid), f"-{number_of_moves}a")
        print(f"Invalid input! Adding additional elements to the board")
    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        if index1 > index2:
            elements.pop(index1)
            elements.pop(index2)
        else:
            elements.pop(index2)
            elements.pop(index1)
    elif elements[index1] != elements[index2]:
        print(f"Try again!")
    if len(elements) == 0:
        break

    command = input().strip()

if command != "end":
    print(f"You have won in {number_of_moves} turns!")
else:
    print(f"Sorry you lose :(")
    print(' '.join(elements))

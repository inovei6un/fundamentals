cards_list = list(input().split(', '))
command_number = int(input())
index2 = 0
for i in range(1, command_number + 1):
    command = input()
    expand = command.split(", ")
    current_command = expand[0]
    card_name = expand[1]
    if current_command == "Add":
        if card_name in cards_list:
            print("Card is already in the deck")
        else:
            cards_list.append(card_name)
            print("Card successfully added")
    elif current_command == "Remove":
        if card_name not in cards_list:
            print(f"Card not found")
        else:
            cards_list.remove(card_name)
            print(f"Card successfully removed")
    elif current_command == "Insert":
        index2 = int(card_name)
        card_name = expand[2]
        if index2 not in range(len(cards_list)):
            print(f"Index out of range")
        elif card_name in cards_list:
            print(f"Card is already added")
        else:
            cards_list.insert(index2, card_name)
            print(f"Card successfully added")
    elif current_command == "Remove At":
        index2 = int(card_name)
        if index2 not in range(len(cards_list)):
            print(f"Index out of range")
        else:
            cards_list.pop(index2)
            print(f"Card successfully removed")

print(', '.join(cards_list))

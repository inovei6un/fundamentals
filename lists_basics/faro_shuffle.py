deck = input().split(' ')
num_of_shuffles = int(input())
first_half = []
second_half = []
shuffled_deck = []

for i in range(1, num_of_shuffles + 1):
    for card in range(len(deck)):
        current_card = deck[card]
        if card % 2 == 0:
            first_half.append(current_card)
        elif card % 2 != 0:
            second_half.append(current_card)
    shuffled_deck = [c for pair in zip(first_half, second_half) for c in pair]
print(shuffled_deck)

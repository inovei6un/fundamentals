energy = int(input())
command = input()
won_battle_counter = 0

while command != "End of battle":
    distance = int(command)
    energy -= distance
    if energy >= 0:
        won_battle_counter += 1
        if won_battle_counter % 3 == 0:
            energy += won_battle_counter
    elif energy < 0:
        break

    command = input()
if energy < 0:
    energy = 0
    print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battle_counter}. Energy left: {energy}")

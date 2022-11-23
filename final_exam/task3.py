command = input()
animals_dict = dict()
hungry_animal = 0

while command != "EndDay":
    command_params = command.split(':')
    action = command_params[0]
    animal_split = command_params[1].split('-')
    animal_name = animal_split[0]
    if action == "Add":
        needed_food = int(animal_split[1])
        area = animal_split[2]
        current_animal_dict = dict()
        current_animal_dict['needed food'] = int(needed_food)
        current_animal_dict['area'] = area
        if animal_name in animals_dict:
            animals_dict[animal_name]['needed food'] += current_animal_dict['needed food']
        else:
            animals_dict[animal_name] = current_animal_dict
    elif action == "Feed":
        food = int(animal_split[1])
        if animal_name in animals_dict:
            animals_dict[animal_name]['needed food'] -= food
            if animal_name not in animals_dict:
                pass
            else:
                animals_dict.pop(animal_name)
                print(f"{animal_name} was successfully fed")

    command = input()

area_dict = dict()
animals_list = list()
print(f"Animals")
for animal in animals_dict:
    print(f"{animal} -> {animals_dict[animal]['needed food']}g")
print(f"Areas with hungry animals")
for animal in animals_dict:
    for keys in animals_dict[animal]:
        if keys == "area":
                current_animal_dict['animal'] = animal
                area_dict[animals_dict[animal]['area']] = current_animal_dict
                print(area_dict)
for area in area_dict:
    hungry_animal = 0
    for animal in area_dict[area]:
        hungry_animal += 1
        print(f"{area}: {hungry_animal}")

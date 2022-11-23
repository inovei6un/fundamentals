command = input()
animals_dict = dict()
hungry_animal = 0

while command != "EndDay":
    command_params = command.split(':')
    action = command_params[0]
    other_split = command_params[1].split('-')
    animal_name = other_split[0]
    if action == "Add":
        needed_food = int(other_split[1])
        area = other_split[2]
        current_animal_dict = dict()
        current_animal_dict['needed food'] = int(needed_food)
        current_animal_dict['animal name'] = animal_name
        if area not in animals_dict:
            animals_dict[area] = current_animal_dict
        else:
            animals_dict[area]['needed food'] += current_animal_dict['needed food']
    elif command == "Feed":
        food = other_split[1]
        if animal_name in animals_dict:
            animals_dict[area]['']

    command = input()
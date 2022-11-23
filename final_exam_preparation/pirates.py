command = input()
targets_dict = dict()

while command != "Sail":
    targets = command.split('||')
    city = targets[0]
    population = int(targets[1])
    gold = int(targets[2])
    if city in targets_dict:
        targets_dict[city]["population"] += population
        targets_dict[city]["gold"] += gold

    current_target_dict = dict()
    if city not in targets_dict:
        targets_dict[city] = current_target_dict
        current_target_dict["population"] = population
        current_target_dict["gold"] = gold
    else:
        pass

    command = input()

while command != "End":
    command = input()
    if command == "End":
        break
    command_params = command.split('=>')
    action = command_params[0]
    city = command_params[1]
    if action == "Plunder":
        population = int(command_params[2])
        gold = int(command_params[3])
        targets_dict[city]["population"] -= population
        targets_dict[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        if targets_dict[city]["population"] == 0 or targets_dict[city]["gold"] == 0:
            targets_dict.pop(city)
            print(f"{city} has been wiped off the map!")
    elif action == "Prosper":
        coins = int(command_params[2])
        if coins < 0:
            print('Gold added cannot be a negative number!')
        else:
            targets_dict[city]["gold"] += coins
            print(f"{coins} gold added to the city treasury. {city} now has {targets_dict[city]['gold']} gold.")

if len(targets_dict) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(targets_dict)} wealthy settlements to go to:")
    for target in targets_dict:
        print(f"{target} -> Population: {targets_dict[target]['population']} citizens,"
              f" Gold: {targets_dict[target]['gold']} kg")

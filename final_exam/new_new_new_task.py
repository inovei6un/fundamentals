heroes_dict = dict()

command = input()

while command != "Results":
    command_params = command.split(':')
    action = command_params[0]
    if action == "Add":
        person_name = command_params[1]
        HP = int(command_params[2])
        EP = int(command_params[3])
        if person_name not in heroes_dict:
            current_hero_dict = dict()
            current_hero_dict['HP'] = HP
            current_hero_dict['EP'] = EP
            heroes_dict[person_name] = current_hero_dict
        else:
            heroes_dict[person_name]['HP'] += HP
    elif action == "Attack":
        attacker = command_params[1]
        defender = command_params[2]
        damage = int(command_params[3])
        if attacker in heroes_dict and defender in heroes_dict:
            heroes_dict[defender]['HP'] -= damage
            heroes_dict[attacker]['EP'] -= 1
            if heroes_dict[defender]['HP'] <= 0:
                heroes_dict.pop(defender)
                print(f"{defender} was disqualified!")
            if heroes_dict[attacker]['EP'] <= 0:
                heroes_dict.pop(attacker)
                print(f"{attacker} was disqualified!")
    elif action == "Delete":
        name = command_params[1]
        if name == "All":
            heroes_dict.clear()
        else:
            heroes_dict.pop(name)
    command = input()
print(f"People count: {len(heroes_dict)}")
for people in heroes_dict:
    print(f"{people} - {heroes_dict[people]['HP']} - {heroes_dict[people]['EP']}")

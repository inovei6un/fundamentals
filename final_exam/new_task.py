skill_name = input()

while True:
    command = input()
    if command == "For Azeroth":
        break
    command_params = command.split(' ')
    action = command_params[0]
    if action == "GladiatorStance":
        skill_name = skill_name.upper()
        print(skill_name)
    elif action == "DefensiveStance":
        skill_name = skill_name.lower()
        print(skill_name)
    elif action == "Dispel":
        index = int(command_params[1])
        letter = command_params[2]
        if -len(skill_name) <= index and index <= len(skill_name):
            skill_name_list = list(skill_name)
            skill_name_list[index] = letter
            skill_name = ''.join(skill_name_list)
            print("Success!")
        else:
            print("Dispel too weak")
    elif action == "Target":
        action_two = command_params[1]
        if action_two == "Change":
            first_substring = command_params[2]
            second_substring = command_params[3]
            if first_substring not in skill_name:
                print(skill_name)
            elif first_substring in skill_name:
                skill_name = skill_name.replace(first_substring, second_substring)
                print(skill_name)
        elif action_two == "Remove":
            substring = command_params[2]
            if substring in skill_name:
                skill_name = skill_name.replace(substring, '')
                print(skill_name)
            else:
                continue
        else:
            print("Command doesn't exist!")

    else:
        print("Command doesn't exist!")

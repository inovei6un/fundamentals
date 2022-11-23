some_string = input()
is_substring_in_command = False
command = input()

while command != "End":
    command_params = command.split(' ')
    if command_params[0] == "Translate":
        char = command_params[1]
        replacement = command_params[2]
        some_string = some_string.replace(char, replacement)
        print(some_string)
    elif command_params[0] == "Includes":
        substring = command_params[1]
        match = some_string.find(substring)
        if match > -1:
            is_substring_in_command = True
        else:
            is_substring_in_command = False
        print(is_substring_in_command)
    elif command_params[0] == "Start":
        substring = command_params[1]
        start_with = some_string.startswith(substring)
        print(start_with)
    elif command_params[0] == "Lowercase":
        some_string = lowercase = some_string.lower()
        print(some_string)
    elif command_params[0] == "FindIndex":
        char = command_params[1]
        print(some_string.rfind(char))
    elif command_params[0] == "Remove":
        start_index = int(command_params[1])
        count = int(command_params[2])
        removed_part = some_string[start_index: start_index + count]
        not_removed_part = some_string[:start_index]
        not_removed_part2 = some_string[start_index + count:]
        some_string = not_removed_part + not_removed_part2
        print(some_string)
    command = input()

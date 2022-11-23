raw_activation_key = input()
command = input()

while command != "Generate":
    command_params = command.split('>>>')
    if command_params[0] == "Contains":
        substring = command_params[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command_params[0] == "Flip":
        upper_lower = command_params[1]
        start_index = int(command_params[2])
        end_index = int(command_params[3])
        mutating_slice = raw_activation_key[start_index:end_index]
        slice_before = raw_activation_key[:start_index]
        slice_after = raw_activation_key[end_index:]
        if upper_lower == "Upper":
            raw_activation_key = slice_before + mutating_slice.upper() + slice_after
            print(raw_activation_key)
        else:
            mutating_slice.lower()
            raw_activation_key = slice_before + mutating_slice.lower() + slice_after
            print(raw_activation_key)
    elif command_params[0] == "Slice":
        start_index = int(command_params[1])
        end_index = int(command_params[2])
        slice_one = raw_activation_key[:start_index]
        slice_two = raw_activation_key[end_index:]
        raw_activation_key = slice_one + slice_two
        print(raw_activation_key)
    command = input()

print(f"Your activation key is: {raw_activation_key}")

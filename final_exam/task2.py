import re
inputs_count = int(input())
ascii_values = list()
pattern = r'!((?=[A-Z])[A-Za-z]{3,})!:[[]([A-Z a-z]{8,})[]]'


for element in range(inputs_count):
    some_string = input()
    matches = re.findall(pattern, some_string)
    if not matches:
        print(f"The message is invalid")
    else:
        for match in matches:
            match_list = list(match)
            command = match_list[0]
            message = match_list[1]
            for char in message:
                ascii_values.append(str((ord(char))))
            print(f"{command}: {' '.join(ascii_values)}")

message = input()
command = input()

while command != 'Decode':
    command_split = command.split('|')
    if command_split[0] == "Move":
        index = int(command_split[1])
        moving_part = message[:index]
        static_message = message[index:]
        message = static_message + moving_part
    elif command_split[0] == "Insert":
        index = int(command_split[1])
        some_symbol = command_split[2]
        message = message[:index] + some_symbol + message[index:]
    elif command_split[0] == "ChangeAll":
        old_part = command_split[1]
        new_part = command_split[2]
        message = message.replace(old_part, new_part)
    command = input()
print(f"The decrypted message is: {message}")

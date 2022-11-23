raw_password = input()
command = input()
new_password = ""
while command != "Done":
    command_params = command.split(' ')
    action = command_params[0]
    if action == "TakeOdd":
        for symbol in range(len(raw_password)):
            if symbol % 2 != 0:
                new_password += raw_password[symbol]
        raw_password = new_password
        print(raw_password)
    elif action == "Cut":
        index = int(command_params[1])
        length = int(command_params[2])
        static_symbols = raw_password[:index]
        more_symbols = raw_password[index + length:]
        raw_password = static_symbols + more_symbols
        print(raw_password)
    elif action == "Substitute":
        substring = command_params[1]
        substitute = command_params[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print(f"Nothing to replace!")
    command = input()

print(f"Your password is: {raw_password}")

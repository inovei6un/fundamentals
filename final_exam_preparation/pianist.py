number_of_pieces = int(input())
pieces_dict = dict()
current_dict = dict()

for number in range(number_of_pieces):
    piece = input()
    split_piece = piece.split('|')
    song = split_piece[0]
    composer = split_piece[1]
    key = split_piece[2]

    current_dict = dict()
    current_dict["composer"] = composer
    current_dict["key"] = key
    pieces_dict[song] = current_dict


command = input()


while command != "Stop":
    command_split = command.split('|')
    song = command_split[1]
    if command_split[0] == "Add":
        if song in pieces_dict:
            print(f"{song} is already in the collection!")
        else:
            new_current_dict = dict()
            current_composer = command_split[2]
            current_key = command_split[3]
            new_current_dict["composer"] = current_composer
            new_current_dict["key"] = current_key
            pieces_dict[song] = new_current_dict
            print(f"{song} by {current_composer} in {current_key} added to the collection!")
    elif command_split[0] == "Remove":
        if song in pieces_dict:
            pieces_dict.pop(song)
            print(f"Successfully removed {song}!")
        else:
            print(f"Invalid operation! {song} does not exist in the collection.")
    elif command_split[0] == "ChangeKey":
        if song in pieces_dict:
            key = command_split[2]
            pieces_dict[song]["key"] = key
            print(f"Changed the key of {song} to {key}!")
        else:
            print(f"Invalid operation! {song} does not exist in the collection.")

    command = input()

for element in pieces_dict:
    print(f"{element} -> Composer: {pieces_dict[element]['composer']}, Key: {pieces_dict[element]['key']}")

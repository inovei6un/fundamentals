import re

pattern = r'[*]((?=[A-Z])[A-Z][a-z]{3,}(?<![A-Z]))[*]: \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|(?=$)|[@]((?=[A-Z])[A-Z][a-z]{3,}(?<![A-Z]))[@]: \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|(?=$)'

num_of_strings = int(input())

for string in range(num_of_strings):
    line = input()
    matches = re.findall(pattern, line)
    if len(matches) == 0:
        print('Valid message not found!')
    else:
        match_tuple = tuple(matches[0])
        match_list = list(match_tuple)
        if match_list[0] == '':
            print(f'{match_list[4]}: {ord(match_list[5])} {ord(match_list[6])} {ord(match_list[7])}')
        else:
            print(f'{match_list[0]}: {ord(match_list[1])} {ord(match_list[2])} {ord(match_list[3])}')

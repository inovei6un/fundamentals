import re
matches_list = list()
text = input()

regex = r'\b(_)([A-Za-z0-9]+)\b'

matches = re.finditer(regex, text)

for match in matches:
    matches_list.append(match[2])


print(','.join(matches_list))

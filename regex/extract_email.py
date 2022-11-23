import re

line = input()

pattern = r'\b(?!_)(?<=\s)((\w+[._-]*\w+)@(\w+[.-]*\w+[.-]*\w*[.-]\w*))\b'

matches = re.finditer(pattern, line)

for match in matches:
    print(match.group(0))

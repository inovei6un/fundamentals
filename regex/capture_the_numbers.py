import re

pattern = r'\d+'

while True:
    text = input()

    if not text:
        break

    matches = re.findall(pattern, text)

    if len(matches) > 0:
        print(' '.join(matches), end=' ')



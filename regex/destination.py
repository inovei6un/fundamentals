import re

locations = list()
points = 0
text = input()

regex = r'([=/])([A-Z][A-Za-z]{2,})\1'

matches = re.finditer(regex, text)

for match in matches:
    points += len(match[2])
    locations.append(match[2])

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {points}")

import re

cool_threshold = 1
text = input()
pattern = r'(([::]{2})([A-Z](?![A-Z])[a-z]{2,}(?<![A-Z]))[::]{2}|([**]{2})([A-Z](?![A-Z])[a-z]{2,}(?<![A-Z]))[**]{2})'
pattern_for_numbers = r'\d'
matches = re.finditer(pattern, text)
num_matches = re.findall(pattern_for_numbers, text)
match_list = list(matches)

for element in num_matches:
    cool_threshold *= int(element)

print(f'Cool threshold: {cool_threshold}')
print(f"{len(match_list)} emojis found in the text. The cool ones are:")

matches = re.finditer(pattern, text)

for match in matches:
    emoji = match.group(3)
    if match.group(3) == None:
        emoji = match.group(5)
    else:
        pass
    sum_emoji = sum(ord(ch) for ch in emoji)
    if sum_emoji > cool_threshold:
        print(match.group(1))
    else:
        pass

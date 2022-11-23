import re

sentence = input()
repeated_word = input()

pattern = rf'\b{repeated_word}\b'

matches = re.findall(pattern, sentence, re.IGNORECASE)

print(len(matches))

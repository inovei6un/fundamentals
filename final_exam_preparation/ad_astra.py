import re
calories = 0
info = input()

pattern = r'#([A-Za-z]+\s*[A-Za-z]*)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([A-Za-z]+)\s*[A-Z-a-z]*\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'

matches = re.findall(pattern, info)

items = []

for item in matches:
    current_item = [el for el in item if el != ""]
    items.append(current_item)
    calories += int(current_item[2])

num_of_days = int(calories / 2000)
print(f"You have food to last you for: {num_of_days} days!")

for data in items:
    product = data[0]
    date = data[1]
    current_calories = data[2]
    print(f"Item: {product}, Best before: {date}, Nutrition: {current_calories}")

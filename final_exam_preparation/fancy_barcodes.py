import re
count_of_barcodes = int(input())

pattern = r'([@][#]+)(?=[A-Z])([A-Za-z0-9]{6,}(?<=[A-Z]))([@][#]+)'
number_pattern = r'\d'

invalid_matches = list()

for element in range(count_of_barcodes):
    input_string = input()
    matches = re.findall(pattern, input_string)
    if not matches:
        print('Invalid barcode')
    for match in matches:
        barcode = match[1]
        numbers = re.findall(number_pattern, barcode)
        if len(numbers) == 0:
            print(f"Product group: {0:02d}")
        else:
            print(f"Product group: {''.join(numbers)}")


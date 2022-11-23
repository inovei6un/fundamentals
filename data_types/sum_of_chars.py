num_of_chars = int(input())
sum_letter = 0
for i in range(1, num_of_chars + 1):
    letter = input()
    sum_letter += ord(letter)
print(f"The sum equals: {sum_letter}")

num_of_lines = int(input())
capacity = 0

for i in range(1, num_of_lines + 1):
    liters_of_water = int(input())
    capacity += liters_of_water
    if capacity > 255:
        capacity -= liters_of_water
        print("Insufficient capacity!")
print(capacity)

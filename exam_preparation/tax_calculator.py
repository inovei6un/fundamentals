input_string = input().split(">>")
input_list = list(input_string)
initial_tax = 0
counter = 0
tax = 0
tax1 = 0
tax2 = 0
sum_tax = 0

for vehicle in range(len(input_list)):
    vehicleX = input_list[vehicle].split(' ')
    if vehicleX[0] != "family" and vehicleX[0] != "heavyDuty" and vehicleX[0] != "sports":
        print(f"Invalid car type.")
    elif vehicleX[0] == "family":
        initial_tax = 50
        years_to_pay_tax = int(vehicleX[1])
        kilometers_traveled = int(vehicleX[2])
        tax = (initial_tax - years_to_pay_tax * 5) + (int(kilometers_traveled / 3000) * 12)
        print(f"A family car will pay {tax:.2f} euros in taxes.")
    elif vehicleX[0] == "heavyDuty":
        initial_tax = 80
        years_to_pay_tax = int(vehicleX[1])
        kilometers_traveled = int(vehicleX[2])
        tax1 = (initial_tax - years_to_pay_tax * 8) + (int(kilometers_traveled / 9000) * 14)
        print(f"A heavyDuty car will pay {tax1:.2f} euros in taxes.")
    elif vehicleX[0] == "sports":
        initial_tax = 100
        years_to_pay_tax = int(vehicleX[1])
        kilometers_traveled = int(vehicleX[2])
        tax2 = (initial_tax - years_to_pay_tax * 9) + (int(kilometers_traveled / 2000) * 18)
        print(f"A sports car will pay {tax2:.2f} euros in taxes.")
    sum_tax += tax + tax1 + tax2
    tax = 0
    tax1 = 0
    tax2 = 0

print(f"The National Revenue Agency will collect {sum_tax:.2f} euros in taxes.")
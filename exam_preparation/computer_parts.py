command = input()
full_price = 0
taxes = 0

if command == "regular" or command == "special":
    print(f"Invalid order!")
    exit()

while command != "regular" or command != "special":
    if command == "regular":
        break
    elif command == "special":
        break
    part_price = float(command)
    if part_price > 0:
        full_price += part_price
    elif part_price < 0:
        print("Invalid price!")
    command = input()

taxes = 20 / 100 * full_price

if command == "regular":
    if full_price + taxes <= 0:
        print("Invalid order!")
        exit()
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {full_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {full_price + taxes:.2f}$")
elif command == "special":
    additional_discount = (full_price + taxes) - 10 / 100 * (full_price + taxes)
    if additional_discount <= 0:
        print("Invalid order!")
        exit()
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {full_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {additional_discount:.2f}$")

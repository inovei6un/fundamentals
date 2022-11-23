product = input()
quantity = int(input())
coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

def check_please():
    if product == "coffee":
        return coffee * quantity
    elif product == "water":
        return water * quantity
    elif product == "coke":
        return coke * quantity
    elif product == "snacks":
        return snacks * quantity


print(f"{check_please():.2f}")

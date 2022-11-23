age = int(input())
adulthood = ""
if age <= 14:
    print("drink toddy")
elif age <= 18 and age > 14:
    print("drink coke")
elif age <= 21 and age > 18:
    print("drink beer")
else:
    print("drink whisky")

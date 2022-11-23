lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
times_shield_broken = 0
times_sword_broken = 0
times_helmet_broken = 0
times_armor_broken = 0
is_helmet_broken = False
is_sword_broken = False
is_shield_broken = False
is_armor_broken = False

for fights in range(1, lost_fights_count + 1):
    if fights % 2 == 0:
        times_helmet_broken += 1
        is_helmet_broken = True
    if fights % 3 == 0:
        times_sword_broken += 1
        is_sword_broken = True
    if is_helmet_broken and is_sword_broken:
        is_shield_broken = True
        times_shield_broken += 1
    if times_shield_broken % 2 == 0 and is_shield_broken:
        times_armor_broken += 1
    is_helmet_broken = False
    is_sword_broken = False
    is_shield_broken = False
    is_armor_broken = False

sum_all = times_helmet_broken * helmet_price + times_sword_broken * sword_price + times_shield_broken * shield_price + times_armor_broken * armor_price
print(f"Gladiator expenses: {sum_all:.2f} aureus")

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
for current_fight in range(1, lost_fights + 1):
    if current_fight % 2 == 0:
        total_expenses += helmet_price
    if current_fight % 3 == 0:
        total_expenses += sword_price
        if current_fight % 2 == 0:
            total_expenses += shield_price
    if current_fight % 12 == 0:
        total_expenses += armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
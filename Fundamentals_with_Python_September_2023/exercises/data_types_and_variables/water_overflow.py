number_of_lines = int(input())
tank_capacity = 255
liters_poured = 0
for current_line in range(number_of_lines):
    liters = int(input())
    if tank_capacity < liters:
        print("Insufficient capacity!")
        continue
    liters_poured += liters
    tank_capacity -= liters
print(liters_poured)
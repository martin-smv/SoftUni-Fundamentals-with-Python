fire_with_their_cells = input().replace("#", " ").replace("=", "").split()
water = int(input())
effort = 0
total_fire = 0
print("Cells:")
for current_cell in range(len(fire_with_their_cells) // 2):
    fire_type = fire_with_their_cells[0]
    cell_value = int(fire_with_their_cells[1])
    if fire_type == "High":
        if 81 <= cell_value <= 125 and water >= cell_value:
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            print(f" - {cell_value}")
    elif fire_type == "Medium":
        if 51 <= cell_value <= 80 and water >= cell_value:
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            print(f" - {cell_value}")
    elif fire_type == "Low":
        if 1 <= cell_value <= 50 and water >= cell_value:
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            print(f" - {cell_value}")
    fire_with_their_cells.pop(0)
    fire_with_their_cells.pop(0)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
first_line = input().replace(" ", "")
second_line = input().replace(" ", "")
third_line = input().replace(" ", "")

draw = True
first_player_won = True

list_with_all_lines = [first_line, second_line, third_line]
# Checking if horizontal line have three identical symbols
for element in list_with_all_lines:
    if element == "222":
        first_player_won = False
        draw = False
        break
    elif element == "111":
        draw = False
        break

# Checking if vertical line have three identical symbols
for index in range(3):
    vertical_line = ""
    vertical_line += first_line[index]
    vertical_line += second_line[index]
    vertical_line += third_line[index]
    if vertical_line == "222":
        first_player_won = False
        draw = False
        break
    elif vertical_line == "111":
        draw = False
        break

# Checking if diagonal line have three identical symbols
if first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == "2":
        first_player_won = False
        draw = False
    elif first_line[0] == "1":
        draw = False
if first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == "2":
        first_player_won = False
        draw = False
    elif first_line[2] == "1":
        draw = False

if draw:
    print("Draw!")
elif first_player_won:
    print("First player won")
else:
    print("Second player won")
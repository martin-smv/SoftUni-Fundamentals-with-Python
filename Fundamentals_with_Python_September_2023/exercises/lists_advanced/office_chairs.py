number_of_rooms = int(input())

free_chairs = 0
for current_room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()

    number_of_chairs = len(chairs_and_visitors[0])
    number_of_visitors = int(chairs_and_visitors[1])

    if number_of_chairs >= number_of_visitors:
        free_chairs += number_of_chairs - number_of_visitors

    else:
        needed_chairs = number_of_visitors - number_of_chairs
        free_chairs -= needed_chairs
        print(f"{needed_chairs} more chairs needed in room {current_room}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
number_of_rooms = int(input())

free_chairs = 0
for current_room in range(number_of_rooms):
    chairs_and_visitors = input().split()

    number_of_chairs = len(chairs_and_visitors[0])
    number_of_visitors = int(chairs_and_visitors[1])
    room_number = current_room + 1

    if number_of_chairs >= number_of_visitors:
        free_chairs += number_of_chairs - number_of_visitors

    else:
        needed_chairs = number_of_visitors - number_of_chairs
        free_chairs -= needed_chairs
        print(f"{needed_chairs} more chairs needed in room {room_number}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
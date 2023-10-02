persons = int(input())
elevator_capacity = int(input())
needed_courses = 0
while persons > 0:
    needed_courses += 1
    persons = persons - elevator_capacity
print(needed_courses)
from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

highest_attendance = 0
total_bonus = 0
for student in range(number_of_students):
    student_attendance = int(input())
    if student_attendance > highest_attendance:
        highest_attendance = student_attendance
    total_bonus = highest_attendance / number_of_lectures * (5 + additional_bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {highest_attendance} lectures.")
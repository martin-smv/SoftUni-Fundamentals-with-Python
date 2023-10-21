first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())

time = 0
sum_of_employees_efficiency = first_employee + second_employee + third_employee
while student_count > 0:
    time += 1

    if time % 4 == 0:
        continue

    student_count = student_count - sum_of_employees_efficiency

print(f"Time needed: {time}h.")
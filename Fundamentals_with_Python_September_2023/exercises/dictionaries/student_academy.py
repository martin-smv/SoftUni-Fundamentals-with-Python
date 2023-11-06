def average_grades():
    for current_student in student_info:
        number_of_grades = names.count(current_student)
        average_grade = student_info[current_student] / number_of_grades
        student_info[current_student] = average_grade


number = int(input())

student_info = {}
names = []
for i in range(number):
    student_name = input()
    grade = float(input())

    if student_name not in student_info.keys():
        student_info[student_name] = grade
    else:
        student_info[student_name] += grade

    names.append(student_name)

average_grades()

for name, average_grade in student_info.items():
    if student_info[name] >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

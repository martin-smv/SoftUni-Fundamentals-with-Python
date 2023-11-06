courses_status = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")
    if course_name not in courses_status:
        courses_status[course_name] = [student_name]
    else:
        courses_status[course_name] += [student_name]

for course in courses_status.keys():
    registered_students = len(courses_status[course])
    print(f"{course}: {registered_students}")
    for name in courses_status[course]:
        print(f"-- {name}")
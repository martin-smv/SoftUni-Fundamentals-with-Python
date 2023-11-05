student_status = {}

while True:
    command = input()

    if command.lower() == command:
        break

    name, id_num, course = command.split(":")
    student_status[name] = id_num, course

for name, value in student_status.items():
    id_num = value[0]
    course_name = value[1]

    if command[:1] == course_name[:1]:
        print(f"{name} - {id_num}")
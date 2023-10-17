schedule_lessons = input().split(", ")

list_with_commands_and_titles = input().split(":")
while list_with_commands_and_titles[0] != "course start":

    command = list_with_commands_and_titles[0]
    title = list_with_commands_and_titles[1]

    if command == "Add":
        if title not in schedule_lessons:
            schedule_lessons.append(title)

    elif command == "Insert":
        index = int(list_with_commands_and_titles[2])
        if index < len(schedule_lessons):
            if title not in schedule_lessons:
                schedule_lessons.insert(index, title)

    elif command == "Remove":
        if title in schedule_lessons:
            schedule_lessons.remove(title)
            if title + "-Exercise" in schedule_lessons:
                schedule_lessons.remove(title + "-Exercise")

    elif command == "Swap":
        first_title = list_with_commands_and_titles[1]
        second_title = list_with_commands_and_titles[2]

        if first_title in schedule_lessons:
            if second_title in schedule_lessons:
                first_index = schedule_lessons.index(first_title)
                second_index = schedule_lessons.index(second_title)
                schedule_lessons[first_index], schedule_lessons[second_index] =\
                    schedule_lessons[second_index], schedule_lessons[first_index]
                if first_title + "-Exercise" in schedule_lessons:
                    current_index = schedule_lessons.index(first_title)
                    index_of_exercise = schedule_lessons.index(first_title + "-Exercise")
                    swapping_exercise = schedule_lessons.pop(index_of_exercise)
                    schedule_lessons.insert(current_index + 1, first_title + "-Exercise")
                if second_title + "-Exercise" in schedule_lessons:
                    current_index = schedule_lessons.index(second_title)
                    index_of_exercise = schedule_lessons.index(second_title + "-Exercise")
                    swapping_exercise = schedule_lessons.pop(index_of_exercise)
                    schedule_lessons.insert(current_index + 1, second_title + "-Exercise")

    elif command == "Exercise":
        if title not in schedule_lessons:
            schedule_lessons.append(title)
            schedule_lessons.append(title + "-Exercise")
        else:
            index_of_title = schedule_lessons.index(title)
            if title + "-Exercise" not in schedule_lessons:
                schedule_lessons.insert(index_of_title + 1, title + "-Exercise")

    list_with_commands_and_titles = input().split(":")

for i in range(len(schedule_lessons)):
    print(f"{i + 1}.{schedule_lessons[i]}")
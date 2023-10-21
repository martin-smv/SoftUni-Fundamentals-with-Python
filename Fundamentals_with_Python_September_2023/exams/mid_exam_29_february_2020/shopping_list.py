shopping_list = input().split("!")


while True:
    list_of_command = input().split()
    current_command = list_of_command[0]
    item = list_of_command[1]

    if " ".join(list_of_command) == "Go Shopping!":
        break

    elif current_command == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif current_command == "Unnecessary":
        if item in shopping_list:
            shopping_list = [i for i in shopping_list if i != item]

    elif current_command == "Correct":
        if item in shopping_list:
            new_item = list_of_command[2]
            shopping_list = [i if i != item else new_item for i in shopping_list]

    elif current_command == "Rearrange":
        if item in shopping_list:
            shopping_list = [i for i in shopping_list if i != item]
            shopping_list.insert(len(shopping_list), item)

print(", ".join(shopping_list))
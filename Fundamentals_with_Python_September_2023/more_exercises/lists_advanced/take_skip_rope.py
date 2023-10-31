def show_hidden_message(take_list, skip_list, char_list):
    result = ""
    take_list = [int(s) for s in take_list]
    skip_list = [int(s) for s in skip_list]

    for index in range(len(take_list)):

        for i in range(take_list[index]):
            if len(char_list) == 0 or take_list[index] == 0:
                break
            result += char_list[0]
            char_list.pop(0)

        for i in range(skip_list[index]):
            if len(char_list) == 0 or skip_list[index] == 0:
                break
            char_list.pop(0)

    return result


def split_nums(n_list):
    take_list = []
    skip_list = []
    for i in range(len(n_list)):
        if i % 2 == 0:
            take_list.append(n_list[i])
        else:
            skip_list.append(n_list[i])

    return take_list, skip_list


def split_nums_and_strings(text):
    num_list = []
    char_list = []
    for char in text:
        if char.isdigit():
            num_list.append(char)
        else:
            char_list.append(char)

    return num_list, char_list


some_text = input()
numbers_list, characters_list = split_nums_and_strings(some_text)
take_list, skip_list = split_nums(numbers_list)

print(show_hidden_message(take_list, skip_list, characters_list))
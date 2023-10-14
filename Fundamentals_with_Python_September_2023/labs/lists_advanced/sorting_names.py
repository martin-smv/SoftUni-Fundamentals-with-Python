def sort_names_by_length():
    sorted_names = sorted(names_list, key=lambda x: (-len(x), x))
    return sorted_names


names_list = input().split(", ")
print(sort_names_by_length())
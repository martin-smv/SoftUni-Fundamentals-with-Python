some_string = input()
my_list = []
for index in range(len(some_string)):
    if some_string[index].isupper():
        my_list.append(index)
print(my_list)
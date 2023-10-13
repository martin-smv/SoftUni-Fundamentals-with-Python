def palindrome_checker(number):
    for current_number in number:
        if current_number == current_number[::-1]:
            print(True)
        else:
            print(False)


list_with_numbers = input().split(", ")
palindrome_checker(list_with_numbers)
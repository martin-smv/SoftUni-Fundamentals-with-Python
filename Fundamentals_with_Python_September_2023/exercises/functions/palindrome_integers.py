def palindrome_checker(number):
    for current_number in number:
        if current_number[0] == current_number[len(current_number) - 1]:
            print(True)
        else:
            print(False)


list_with_numbers = input().replace(",", "").split()
palindrome_checker(list_with_numbers)
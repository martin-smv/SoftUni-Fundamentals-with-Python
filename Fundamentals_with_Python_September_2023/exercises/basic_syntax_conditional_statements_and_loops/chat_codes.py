number = int(input())

secret_message = ""
for count_of_numbers in range(number):
    current_number = int(input())

    if current_number == 88:
        secret_message = "Hello"
    elif current_number == 86:
        secret_message = "How are you?"
    elif current_number != 86 and current_number < 88:
        secret_message = "GREAT!"
    elif current_number > 88:
        secret_message = "Bye."

    print(secret_message)
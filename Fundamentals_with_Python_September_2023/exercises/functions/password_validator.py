def password_validator(some_password: str) -> list:
    list_with_errors = []
    if 6 > len(some_password) or 10 < len(some_password):
        list_with_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_with_errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for digit in some_password:
        if digit.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_with_errors.append("Password must have at least 2 digits")
    return list_with_errors


password = input()
errors_in_password = password_validator(password)

if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))
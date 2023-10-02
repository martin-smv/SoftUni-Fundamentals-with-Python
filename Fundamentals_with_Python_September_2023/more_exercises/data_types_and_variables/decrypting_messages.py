key = int(input())
number_of_lines = int(input())
secret_message = ""
for letter in range(number_of_lines):
    character = input()
    secret_message += chr(ord(character) + key)
print(secret_message)
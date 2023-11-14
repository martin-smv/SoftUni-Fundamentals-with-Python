first_number = ord(input())
second_number = ord(input())
random_text = input()

total_sum = 0
for char in random_text:
    if first_number < ord(char) < second_number:
        total_sum += ord(char)

print(total_sum)
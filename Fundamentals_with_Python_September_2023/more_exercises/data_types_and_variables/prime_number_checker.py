number = int(input())
prime_number = True
for current_number in range(2, int(number / 2) + 1):
    if number % current_number == 0:
        prime_number = False
if prime_number:
    print("True")
else:
    print("False")
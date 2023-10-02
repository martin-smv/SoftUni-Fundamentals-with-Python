first_number = int(input())
second_number = int(input())
print(f"Before:\n"
      f"a = {first_number}\n"
      f"b = {second_number}")
third_number = second_number
second_number = first_number
first_number = third_number
print(f"After:\n"
      f"a = {first_number}\n"
      f"b = {second_number}")
numbers_list = input().split()
numbers_list = [int(i) for i in numbers_list]

print(f"The minimum number is {min(numbers_list)}")
print(f"The maximum number is {max(numbers_list)}")
print(f"The sum number is: {sum(numbers_list)}")
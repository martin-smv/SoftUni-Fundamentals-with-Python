def calculating_results(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return int(num1 / num2)
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2

operator = input()
first_numbers = int(input())
second_number = int(input())
result = calculating_results(operator, first_numbers, second_number)
print(result)
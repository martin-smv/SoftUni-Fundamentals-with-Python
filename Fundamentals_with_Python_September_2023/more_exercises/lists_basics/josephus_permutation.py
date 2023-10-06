list_with_numbers = input().split()
fatal_number = int(input())
order_of_executions = []
counter = 0

index = 0
while len(list_with_numbers) > 0:
    counter += 1

    if counter % fatal_number == 0:
        order_of_executions.append(list_with_numbers.pop(index))
    else:
        index += 1

    if index >= len(list_with_numbers):
        index = 0

for i in range(len(order_of_executions)):
    order_of_executions[i] = int(order_of_executions[i])

print(str(order_of_executions).replace(" ", ""))
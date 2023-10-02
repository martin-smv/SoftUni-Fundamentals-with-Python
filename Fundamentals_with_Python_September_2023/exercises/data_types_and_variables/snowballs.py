from sys import maxsize

number_of_snowballs = int(input())
max_value = - maxsize
greater_weight = 0
greater_time = 0
greater_quality = 0
for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value_of_the_snowball = (weight / time) ** quality
    if value_of_the_snowball > max_value:
        max_value = value_of_the_snowball
        greater_weight = weight
        greater_time = time
        greater_quality = quality
print(f"{greater_weight} : {greater_time} = {int(max_value)} ({greater_quality})")
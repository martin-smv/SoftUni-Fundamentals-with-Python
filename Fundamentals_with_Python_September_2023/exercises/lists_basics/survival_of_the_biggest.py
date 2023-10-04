list_of_strings = input().split()
count_of_numbers_for_removing = int(input())
list_of_integers = []
for current_number in list_of_strings:
    list_of_integers.append(int(current_number))
for remove in range(count_of_numbers_for_removing):
    list_of_integers.remove(min(list_of_integers))
final_numbers = ', '.join([str(s) for s in list_of_integers])
print(final_numbers)
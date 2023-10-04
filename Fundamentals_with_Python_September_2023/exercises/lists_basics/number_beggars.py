string_of_money = input().split(", ")
count_of_beggars = int(input())
integer_of_money = []
for money in string_of_money:
    integer_of_money.append(int(money))
final_sums = []
start_index = 0
while start_index < count_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(integer_of_money), count_of_beggars):
        current_beggar_sum += integer_of_money[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)
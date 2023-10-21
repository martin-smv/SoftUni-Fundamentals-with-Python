sequence = [int(s) for s in input().split()]
sorted_sequence = sorted(sequence, reverse=True)
top_five_numbers = []
average = sum(sequence) / len(sequence)

for number in sorted_sequence:
    if len(top_five_numbers) > 4:
        break

    if number > average:
        top_five_numbers.append(number)

if len(top_five_numbers) == 0:
    print("No")
else:
    top_five_numbers = [str(s) for s in top_five_numbers]
    print(" ".join(top_five_numbers))
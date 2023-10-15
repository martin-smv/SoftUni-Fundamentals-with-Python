def positive_or_negative():
    positive_numbers = []
    negative_numbers = []

    for number in numbers:
        if int(number) >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)

    return ", ".join(positive_numbers), ", ".join(negative_numbers)


def even_or_odd():
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if int(number) % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return ", ".join(even_numbers), ", ".join(odd_numbers)


numbers = input().split(", ")

positive, negative = positive_or_negative()
even, odd = even_or_odd()

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
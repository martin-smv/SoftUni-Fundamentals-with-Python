text = input().upper()
rage_message = ""
current_symbols = ""
repetitions = ""

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbols += text[index]
    else:
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]

        rage_message += current_symbols * int(repetitions)
        current_symbols = ""
        repetitions = ""

length_of_unique_symbols = len(set(rage_message))
print(f"Unique symbols used: {length_of_unique_symbols}")
print(rage_message)
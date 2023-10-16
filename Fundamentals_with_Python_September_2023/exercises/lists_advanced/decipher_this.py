secret_message = input().split()
new_secret_message = []

index = 0
for word in secret_message:
    word = list(word)
    number = []

    while word[0].isdigit():
        number.append(word[0])
        word.pop(0)
    number = "".join(number)
    char = chr(int(number))

    current_word = secret_message[index]
    new_word = current_word.replace(number, char)
    new_secret_message.append(new_word)

    index += 1

i = 0
for w in new_secret_message:
    letters = list(w)
    letters[1], letters[-1] = letters[-1], letters[1]
    new_secret_message[i] = "".join(letters)
    i += 1

print(" ".join(new_secret_message))
some_text = input().split()

counting_letters = {}

for word in some_text:
    for i in range(len(word)):
        if word[i] not in counting_letters:
            counting_letters[word[i]] = 1
        else:
            counting_letters[word[i]] += 1

for letter, number in counting_letters.items():
    print(f"{letter} -> {number}")
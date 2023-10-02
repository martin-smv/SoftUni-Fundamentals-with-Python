some_word = input()

reversed_word = ""
for reverse in range(len(some_word) - 1, - 1, - 1):
    reversed_word += some_word[reverse]

print(reversed_word)

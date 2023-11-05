number = int(input())

synonyms_dict = {}
for i in range(number):
    word = input()
    synonym = input()

    if word in synonyms_dict:
        synonyms_dict[word].append(synonym)
    else:
        synonyms_dict[word] = [synonym]


for word, synonyms_list in synonyms_dict.items():
    print(f"{word} - {', '.join(synonyms_dict[word])}")
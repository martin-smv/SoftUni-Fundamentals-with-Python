some_text = input()

count = some_text.count(":")
index = 0
for i in range(count):
    index = some_text.find(":", index)
    emoticon = some_text[index: index + 2]
    index += 1
    print(emoticon)

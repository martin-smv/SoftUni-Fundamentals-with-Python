some_text = input()

sorted_text = [char for char in some_text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(sorted_text))

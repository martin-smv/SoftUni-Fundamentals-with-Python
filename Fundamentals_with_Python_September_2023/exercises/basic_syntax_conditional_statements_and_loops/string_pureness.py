number = int(input())

for current_number in range(number):
    some_text = input()
    if "," in some_text or "." in some_text or "_" in some_text:
        print(f"{some_text} is not pure!")
    else:
        print(f"{some_text} is pure.")
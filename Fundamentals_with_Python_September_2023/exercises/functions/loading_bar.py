def is_all_chr_same(some_list):
    return len(set(some_list)) == 1


def loading(some_number: int):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    is_loading_complete = False

    for i in range(some_number // 10):
        bar[i] = "%"
    if is_all_chr_same(bar) and some_number > 0:
        is_loading_complete = True
    return bar, is_loading_complete


number = int(input())
loading_bar_list, is_complete = loading(number)

loading_bar = ""
for character in loading_bar_list:
    loading_bar += character

if is_complete:
    print(f"{number}% Complete!")
    print(f"[{loading_bar}]")
else:
    print(f"{number}% [{loading_bar}]")
    print("Still loading...")
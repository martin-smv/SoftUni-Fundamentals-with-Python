def collect_func(journal, item):
    if item not in journal:
        journal.append(item)


def drop_func(journal, item):
    if item in journal:
        index = journal.index(item)
        journal.pop(index)


def combine_items_func(journal, old_item, new_item):
    if old_item in journal:
        index_after_old_item = journal.index(old_item) + 1
        journal.insert(index_after_old_item, new_item)


def renew_func(journal, item):
    if item in journal:
        journal.remove(item)
        journal.insert(len(journal), item)


journal = input().split(", ")

command = input()
while command != "Craft!":
    command = command.split(" - ")
    current_command = command[0]

    if current_command == "Collect":
        item = command[1]
        collect_func(journal, item)

    elif current_command == "Drop":
        item = command[1]
        drop_func(journal, item)

    elif current_command == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        combine_items_func(journal, old_item, new_item)

    elif current_command == "Renew":
        item = command[1]
        renew_func(journal, item)

    command = input()

print(", ".join(journal))
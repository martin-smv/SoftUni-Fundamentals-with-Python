def add_book(shelf, book_name):
    if book_name not in shelf:
        shelf.insert(0, book_name)


def take_book(shelf, book_name):
    if book_name in shelf:
        shelf.remove(book_name)


def swap_books(shelf, first_book, second_book):
    if first_book in shelf and second_book in shelf:
        index_of_first = shelf.index(first_book)
        index_of_second = shelf.index(second_book)
        shelf[index_of_first], shelf[index_of_second] = shelf[index_of_second], shelf[index_of_first]


def insert_book(shelf, book_name):
    if book_name not in shelf:
        shelf.append(book_name)


def check_box(shelf, index):
    if 0 <= index < len(shelf):
        print(shelf[index])


shelf_with_books = input().split("&")

command = input()
while command != "Done":
    command = command.split(" | ")
    current_command = command[0]

    if current_command == "Add Book":
        book_name = command[1]
        add_book(shelf_with_books, book_name)

    elif current_command == "Take Book":
        book_name = command[1]
        take_book(shelf_with_books, book_name)

    elif current_command == "Swap Books":
        first_book = command[1]
        second_book = command[2]
        swap_books(shelf_with_books, first_book, second_book)

    elif current_command == "Insert Book":
        book_name = command[1]
        insert_book(shelf_with_books, book_name)

    elif current_command == "Check Book":
        index = int(command[1])
        check_box(shelf_with_books, index)

    command = input()

print(", ".join(shelf_with_books))
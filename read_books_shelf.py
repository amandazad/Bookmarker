def add_book_read(books):
    name_book = input("Write the name of the book: ")
    books.append({"name": name_book})
    print("The book was succesfully added :)")

def sort_key(d):
    return d["name"]

def edit_shelf_read(books):
    while True:
        try:
            edit_read = int(input(" 1. Sort A-Z \n 2. Reverse List \n How do you want to edit? "))
            if edit_read == 1:
                books.sort(key=sort_key)
                print("Your wishlist is now sorted from A-Z!")
            elif edit_read == 2:
                books.reverse()
                print("Your wishlist is reversed!")
            else:
                raise ValueError()
            break
        except Exception:
            print("You need to choose a number from 1-2")

def remove_book_read(books):
    pass

def info_book_read(books):
    pass

def show_bookshelf_read(books):
    index = 0
    for book in books:
        index += 1
        print(f"{index}. {book['name']}")


book_shelf_option_to_function = {}
book_shelf_option_to_function[1] = add_book_read
book_shelf_option_to_function[2] = edit_shelf_read
book_shelf_option_to_function[3] = remove_book_read
book_shelf_option_to_function[4] = info_book_read
book_shelf_option_to_function[5] = show_bookshelf_read

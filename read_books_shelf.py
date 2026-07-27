def add_book_read(books):
    name_book = input("Write the name of the book: ")
    books.append({"name": name_book})
    print("The book was succesfully added :)")

def edit_shelf_read(books):
    edit_read = input("1. Sort A-Z \n 2. Reverse List \n How do you want to edit? ")

def remove_book_read(books):
    pass

def info_book_read(books):
    pass

def show_bookshelf_read(books):
    print(books)


book_shelf_option_to_function = {}
book_shelf_option_to_function[1] = add_book_read
book_shelf_option_to_function[2] = edit_shelf_read
book_shelf_option_to_function[3] = remove_book_read
book_shelf_option_to_function[4] = info_book_read
book_shelf_option_to_function[5] = show_bookshelf_read

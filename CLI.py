import read_books_shelf
import wishlist_bookshelf


#main
def request_main_menu():
    print("\033[1;95m\n--- The Bookmarker ---\n\033[0m")

    print("1. Books")
    print("2. Wishlist")
    print("3. Move a book between shelves")
    print("4. Search a book")
    print("5. Exit")
    option = input("Choose an option: ")
    return option

def show_to_user(msg):
    print(msg)

def request_bookshelf():
        print("\033[1;93m\n --- Your read books --- \n\033[0m")

        print("1. Add a book")
        print("2. Edit Shelf")
        print("3. Remove a book")
        print("4. Rate, date and write")
        print("5. Show informations about the book")
        print("6. Show your bookshelf")
        print("7. Go back to main")
        option = input("Choose an option: ")
        return option

def request_wishlist():
    print("\033[1;96m\n --- Your wishlist --- \n\033[0m")

    print("1. Add a book")
    print("2. Edit Shelf")
    print("3. Remove a book")
    print("4. Recomend a random book")
    print("5. Show your bookshelf")
    print("6. Go back to main")
    option = input("Choose an option: ")
    return option

def request_move_books_name():
    book_name = input(" 1. Move from wishlist to read books \n 2. Move from read books to wishlist \n What do you want to do? ")
    return book_name

def request_move_books():
    move = input("What's the NUMBER of the book you want to move? ")
    return move

def request_name_book():
    name_book = input("Write the name of the book: ")
    return name_book

#read_books_shelf
def request_name_book_add():
    ask_name_book = input("What's the name of the book you want to add: ")
    return ask_name_book

def request_edit_read_bookshelf():
    edit_read = input(" 1. Sort A-Z \n 2. Reverse List \n How do you want to edit? ")
    return edit_read

def request_edit_wishlist():
    edit_wishlist = input(" 1. Sort A-Z \n 2. Reverse List \n 3. Clear List \n How do you want to edit? ")
    return edit_wishlist

def request_name_book_remove_read(books, wishlist):
    read_books_shelf.show_bookshelf_read(books, wishlist)
    remove_book = input("Write the NAME of the book you want to remove: ")
    return remove_book

def request_name_book_remove_wish(books, wishlist):
    wishlist_bookshelf.show_bookshelf_wish(books, wishlist)
    remove_book = input("Write the NAME of the book you want to remove: ")
    return remove_book

def request_option_info():
    choice = input("1. Rate the book. \n2. Date of ending. \n3. Write some detail. \n Which information you want to add? ")
    return choice

def request_name_book_read(books, wishlist):
    read_books_shelf.show_bookshelf_read(books, wishlist)
    name_book = input("Write the name of the book: ")
    return name_book

def request_rating():
    rate = input("Write how many stars this book deserves: ")
    return rate

def request_date():
    date = input("Which day did you finish: ")
    return date

def request_details():
    info = input("Write the details: ")
    return info

#utils
def request_exact_book():
    exact_book = input("What is the NUMBER of the book you are looking for? ")
    return exact_book
def get_input():
    print("\n--- The Bookmarker ---\n")

    print("1. Books")
    print("2. Wishlist")
    print("3. Move a book between shelves")
    print("4. Search a book")
    print("5. Exit")
    while True:
        try:
            option = input("Choose an option: ")
            option = int(option)
            return option_to_function[option]
        except:
            print("Invalid option. Try again")


def main():
    books = []
    wishlist = []
    while True:
        function = get_input()
        function(books, wishlist)

import read_books_shelf

def books_shelf_menu(books, wishlist):
    while True:
        print("\n --- Your read books --- \n")
        print("1. Add a book")
        print("2. Edit Shelf")
        print("3. Remove a book")
        print("4. Rate, date and write")
        print("5. Show your bookshelf")
        print("6. Go back to main")
        try:
            option = input("Choose an option: ")
            option = int(option)
            if option == 6:
                return
            function = read_books_shelf.book_shelf_option_to_function[option]
            function(books)
        except:
            print("Invalid option. Pick a number from 1 to 6")

import wishlist_bookshelf

def wishlist_shelf(books, wishlist):
    while True:
            print("\n --- Your wishlist --- \n")
            print("1. Add a book")
            print("2. Edit Shelf")
            print("3. Remove a book")
            print("4. Recomend a random book")
            print("5. Show your bookshelf")
            print("6. Go back to main")
            try:
                option = input("Choose an option: ")
                option = int(option)
                if option == 6:
                    return
                function = wishlist_bookshelf.wishlist_option_to_function[option]
                function(wishlist)
            except:
                print("Invalid option. Pick a number from 1 to 6!")

def find_books(lst, ask_name_book):
    result_list = []
    for book in lst:
        if ask_name_book in book["name"]:
            result_list.append(book)
    return result_list

def move_book(books, wishlist):
    while True:
        try:
            book_name = int(input(" 1. Move from wishlist to read books \n 2. Move from read books to wishlist \n What do you want to do? "))
            if book_name == 1:
                try:
                    wishlist_bookshelf.show_bookshelf_wish(wishlist)
                    wish_move = int(input("What's the number of the book you want to move? "))
                    book = wishlist[wish_move -1]
                    del wishlist[wish_move -1]
                    books.append(book)
                    print("Your book now is in read books!")
                    break
                except:
                    print("Invalid book, please select a number.")
        except:
            print("Please, choose a number from 1-2.")


def search_book(books, wishlist):
    ask_name_book = input("What's the name of the book you want? ")
    books_local = find_books(books, ask_name_book)
    wishlist_local = find_books(wishlist, ask_name_book)
    if books_local:
        print("These are the books we found in your read books: ")
        for book in books_local:
            print(book["name"])
    if wishlist_local:
        print("These are the books we found in your wishlist: ")
        for book in wishlist_local:
            print(book["name"])
    if not books_local and not wishlist_local:
        print("This book is not in your list of books!")


def exit(books, wishlist):
    import sys
    sys.exit(0)

option_to_function = {}
option_to_function[1] = books_shelf_menu
option_to_function[2] = wishlist_shelf
option_to_function[3] = move_book
option_to_function[4] = search_book
option_to_function[5] = exit

main()
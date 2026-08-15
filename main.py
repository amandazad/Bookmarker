import read_books_shelf
import wishlist_bookshelf
from utils import find_books
from utils import save_data

def get_input():
    #get the option the user wants to use
    print("\033[1;95m--- The Bookmarker ---\033[0m")

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
            #if is not a number it is going to raise an Error
            print("Invalid option. Try again")


def main():
    #creates the lists and calls the function based on the input chosen
    from utils import load_data 
    books, wishlist = load_data()
    while True:
        function = get_input()
        function(books, wishlist)


def books_shelf_menu(books, wishlist):
    """
    This is the main function of the read bookshelf
    It is going to provide the possible options
    """
    while True:
        print("\033[1;93m\n --- Your read books --- \n\033[0m")
        print("1. Add a book")
        print("2. Edit Shelf")
        print("3. Remove a book")
        print("4. Rate, date and write")
        print("5. Show informations about the book")
        print("6. Show your bookshelf")
        print("7. Go back to main")
        try:
            option = input("Choose an option: ")
            option = int(option)
            if option == 7:
                return
            function = read_books_shelf.book_shelf_option_to_function[option]
            function(books, wishlist)
        except:
            print("Invalid option. Pick a number from 1 to 7")


def wishlist_shelf(books, wishlist):
    """
    This is the main function of the wishlist bookshelf
    It is going to provide the possible options
    """
    while True:
            print("\033[1;96m\n --- Your wishlist --- \n\033[0m")
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
                function(books, wishlist)
            except:
                print("Invalid option. Pick a number from 1 to 6!")


def move_book(books, wishlist):
    #it is going to move books between shelves
    while True:
        if len(books, wishlist) == 0:
            print("There's no books in your bookshelf, please add one book.")
            return
        try:
            book_name = int(input(" 1. Move from wishlist to read books \n 2. Move from read books to wishlist \n What do you want to do? "))
            if book_name == 1:
                #move from wishlist to read books
                try:
                    wishlist_bookshelf.show_bookshelf_wish(books, wishlist)
                    wish_move = int(input("What's the NUMBER of the book you want to move? "))
                    book_wish = wishlist[wish_move -1]
                    del wishlist[wish_move -1]
                    books.append(book_wish)
                    save_data(books, wishlist)
                    print("Your book now is in read books!")
                    break
                except:
                    print("Invalid book, please select a number.")
            if book_name == 2:
                #move from read books to wishlist
                try:
                    read_books_shelf.show_bookshelf_read(books, wishlist)
                    read_move = int(input("What's the NUMBER of the book you want to move? "))
                    book_read = books[read_move -1]
                    del books[read_move -1]
                    wishlist.append(book_read)
                    save_data(books, wishlist)
                    print("Your book now is in wishlist books!")
                    break
                except:
                    print("Invalid book, please select a number.")
        except:
            print("Please, choose a number from 1-2.")


def search_book(books, wishlist):
    """
    Search and locate the book the user wants to find
    it is going to show every book with that word/title that is in some if the bookshelfs
    """
    ask_name_book = input("What's the name of the book you want? ")
    books_local = find_books(books, ask_name_book)
    wishlist_local = find_books(wishlist, ask_name_book)
    if books_local:
        #here it is going to show the books on the read bookshelf
        print("These are the books we found in your read books: ")
        for book in books_local:
            print(book["name"])
    if wishlist_local:
        #here it is going to show the books on the wishlist bookshelf
        print("These are the books we found in your wishlist: ")
        for book in wishlist_local:
            print(book["name"])
    if not books_local and not wishlist_local:
        #this is if the book doesn't exits
        print("This book is not in your list of books!")


def exit(books, wishlist):
    #exit this time of use
    import sys
    sys.exit(0)

#dictionary for the functions
option_to_function = {}
option_to_function[1] = books_shelf_menu
option_to_function[2] = wishlist_shelf
option_to_function[3] = move_book
option_to_function[4] = search_book
option_to_function[5] = exit

main()
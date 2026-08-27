import read_books_shelf
import wishlist_bookshelf
from utils import find_books
from utils import save_data
import CLI


def get_input():
    #get the option the user wants to use
    while True:
        try:
            option = CLI.request_main_menu()
            option = int(option)
            return option_to_function[option]
        except:
            #if is not a number it is going to raise an Error
            CLI.show_to_user("Invalid option. Try again")


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
        try:
            option = CLI.request_bookshelf()
            option = int(option)
            if option == 7:
                return
            function = read_books_shelf.book_shelf_option_to_function[option]
            function(books, wishlist)
        except:
            CLI.show_to_user("Invalid option. Pick a number from 1 to 7")


def wishlist_shelf(books, wishlist):
    """
    This is the main function of the wishlist bookshelf
    It is going to provide the possible options
    """
    while True:
            try:
                option = CLI.request_wishlist()
                option = int(option)
                if option == 6:
                    return
                function = wishlist_bookshelf.wishlist_option_to_function[option]
                function(books, wishlist)
            except:
                CLI.show_to_user("Invalid option. Pick a number from 1 to 6!")


def move_book(books, wishlist):
    #it is going to move books between shelves
    while True:
        try:
            if len(books) == 0 and len(wishlist) == 0:
                CLI.show_to_user("There's no books in your bookshelf, please add one book.")
                return
            book_name = CLI.request_move_books_name()
            book_name = int(book_name)
            if book_name == 1:
                #move from wishlist to read books
                if len(wishlist) == 0:
                    CLI.show_to_user("There's no books in your wishlist, please add one book.")
                    return
                else:
                    try:
                        wishlist_bookshelf.show_bookshelf_wish(books, wishlist)
                        move = CLI.request_move_books()
                        move = int(move)
                        book_wish = wishlist[move -1]
                        del wishlist[move -1]
                        books.append(book_wish)
                        save_data(books, wishlist)
                        CLI.show_to_user("Your book now is in read books!")
                        break
                    except:
                        CLI.show_to_user("Invalid book, please select a number.")
            if book_name == 2:
                #move from read books to wishlist
                if len(books) == 0:
                    CLI.show_to_user("There's no books in your read books, please add one book.")
                    return
                else:
                    try:
                        read_books_shelf.show_bookshelf_read(books, wishlist)
                        move = CLI.request_move_books()
                        move = int(move)
                        book_read = books[move -1]
                        del books[move -1]
                        wishlist.append(book_read)
                        save_data(books, wishlist)
                        CLI.show_to_user("Your book now is in wishlist books!")
                        break
                    except:
                        CLI.show_to_user("Invalid book, please select a number.")
        except:
            CLI.show_to_user("Please, choose a number from 1-2.")


def search_book(books, wishlist):
    """
    Search and locate the book the user wants to find
    it is going to show every book with that word/title that is in some if the bookshelfs
    """
    if len(books) == 0 and len(wishlist) == 0:
        CLI.show_to_user("There's no book in your bookshelves!")
        return
    ask_name_book = CLI.request_name_book()
    books_local = find_books(books, ask_name_book)
    wishlist_local = find_books(wishlist, ask_name_book)
    if books_local:
        #here it is going to show the books on the read bookshelf
        CLI.show_to_user("These are the books we found in your read books: ")
        for book in books_local:
            CLI.show_to_user(book["name"])
    if wishlist_local:
        #here it is going to show the books on the wishlist bookshelf
        CLI.show_to_user("These are the books we found in your wishlist: ")
        for book in wishlist_local:
            CLI.show_to_user(book["name"])
    if not books_local and not wishlist_local:
        #this is if the book doesn't exits
        CLI.show_to_user("This book is not in your list of books!")


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

if __name__ == "__main__":
    main()
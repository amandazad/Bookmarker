from utils import find_unique_book
from utils import save_data
import CLI

def add_book_read(books, wishlist):
    """
    This adds some book in the read bookshelf.
    """
    name_book = CLI.request_name_book_add()
    if name_book == '' or name_book.isspace():
        CLI.show_to_user("You need to write a name for the book.")
        return
    else:
        books.append({"name": name_book})
        save_data(books, wishlist)
        CLI.show_to_user("The book was succesfully added :)")


def sort_key(d):
    return d["name"]


def edit_shelf_read(books, wishlist):
    """
    This function is used to sort the list from A-Z or to reverse the list.
    """
    while True:
        if len(books) == 0:
            CLI.show_to_user("There's no books in your bookshelf, please add one book.")
            return
        try:
            edit_read = CLI.request_edit_read_bookshelf()
            edit_read = int(edit_read)
            if edit_read == 1:
                #sort the list from A-Z
                books.sort(key=sort_key)
                save_data(books, wishlist)
                CLI.show_to_user("Your wishlist is now sorted from A-Z!")
            elif edit_read == 2:
                #reverse the entire list
                books.reverse()
                save_data(books, wishlist)
                CLI.show_to_user("Your wishlist is reversed!")
            else:
                raise ValueError()
            break
        except Exception:
            CLI.show_to_user("You need to choose a number from 1-2")


def remove_book_read(books, wishlist):
    """
    This functions remove some book from the read list.
    """
    while True:
        if len(books) == 0:
            CLI.show_to_user("There's no books in your bookshelf, please add one book.")
            return
        remove_book = CLI.request_name_book_remove_read(books, wishlist)
        i = 0
        for rem in books:
            if rem['name'] == remove_book:
                del books[i]
                save_data(books, wishlist)
                CLI.show_to_user("The book was removed from your shelf!")
                return
            i += 1
        CLI.show_to_user("This book is not in your bookshelf. Please try again!")


def info_book_read(books, wishlist):
    """
    This is going to add some aditional information for that book.
    It can rate the book, insert the date of ending or write something that the user want to remember about that book.
    """
    while True:
        if len(books) == 0:
            CLI.show_to_user("There's no books in your bookshelf, please add one book.")
            return
        choice = CLI.request_option_info()
        choice = int(choice)
        try: 
            if choice == 1:
                #this will add the rating (by stars) for certain book
                while True:
                    name_book = CLI.request_name_book_read(books, wishlist)
                    book = find_unique_book(books, name_book)
                    if book is None:
                        continue
                    rate = CLI.request_rating()
                    book["rating"] = rate
                    save_data(books, wishlist)
                    CLI.show_to_user("Now, the rate is available in option 5!")
                    break
            if choice == 2:
                #this will add the ending date of certain book
                while True:
                    name_book = CLI.request_name_book_read(books, wishlist)
                    book = find_unique_book(books, name_book)
                    if book is None:
                        continue
                    date = CLI.request_date()
                    book["date"] = date
                    save_data(books, wishlist)
                    CLI.show_to_user("Now, the date is available in option 5!")
                    break
            if choice == 3:
                #this will add the aditional informations that the user wants
                while True:
                    name_book = CLI.request_name_book_read(books, wishlist)
                    book = find_unique_book(books, name_book)
                    if book is None:
                        continue
                    info = CLI.request_details()
                    book["informations"] = info
                    save_data(books, wishlist)
                    CLI.show_to_user("Now, the details are available in option 5!")
                    break
            break
        except:
            CLI.show_to_user("Please choose a number between 1-3!")
            raise ValueError


def show_information_book(books, wishlist):
    """
    Show some information about one book
    """
    if len(books) == 0:
        CLI.show_to_user("There's no books in your bookshelf, please add one book.")
        return
    index = 0
    for book in books:
        index += 1
        CLI.show_to_user(f"{index}. {book['name']} \n{book.get('rating')} stars \nFinish date: {book.get('date')} \nDetails: {book.get('informations')}")


def show_bookshelf_read(books, wishlist):
    """
    This shows the entire read bookshelf with name and number in the list
    """
    if len(books) == 0:
        CLI.show_to_user("There's no books in your bookshelf, please add one book.")
        return
    index = 0
    for book in books:
        index += 1
        CLI.show_to_user(f"{index}. {book['name']}")


#dictionary for the functions
book_shelf_option_to_function = {}
book_shelf_option_to_function[1] = add_book_read
book_shelf_option_to_function[2] = edit_shelf_read
book_shelf_option_to_function[3] = remove_book_read
book_shelf_option_to_function[4] = info_book_read
book_shelf_option_to_function[5] = show_information_book
book_shelf_option_to_function[6] = show_bookshelf_read

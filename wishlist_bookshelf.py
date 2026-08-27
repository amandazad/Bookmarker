from utils import save_data
import CLI

def add_book_wish(books, wishlist):
    """
    This adds some book in the wishlist bookshelf.
    """
    name_book = CLI.request_name_book_add()
    wishlist.append({"name": name_book})
    save_data(books, wishlist)
    CLI.show_to_user("The book was succesfully added :)")

def sort_key(d):
    return d["name"]

def edit_shelf_wish(books, wishlist):
    """
    This function is used to sort the list from A-Z, reverse the list or clear the list.
    """
    while True:
        if len(wishlist) == 0:
            CLI.show_to_user("There's no books in your bookshelf, please add one book.")
            return
        try:
            edit_wishlist = CLI.request_edit_wishlist
            edit_wishlist = int(edit_wishlist)
            if edit_wishlist == 1:
                #this will sort the list from A-Z
                wishlist.sort(key=sort_key)
                save_data(books, wishlist)
                CLI.show_to_user("Your wishlist is now sorted from A-Z!")
            elif edit_wishlist == 2:
                #this will reverse the list
                wishlist.reverse()
                save_data(books, wishlist)
                CLI.show_to_user("Your wishlist is reversed!")
            elif edit_wishlist == 3:
                #this will clear the list
                wishlist.clear()
                save_data(books, wishlist)
                CLI.show_to_user("Your wishlist is cleared!")
            else:
                raise ValueError()
            break
        except Exception:
            CLI.show_to_user("You need to choose a number from 1-3")

def remove_book_wish(books, wishlist):
    """
    This functions remove some book from the wishlist.
    """
    while True:
        if len(wishlist) == 0:
            CLI.show_to_user("There's no books in your bookshelf, please add one book.")
            return
        remove_book = CLI.request_name_book_remove_wish(books, wishlist)
        i = 0
        for rem in wishlist:
            if rem['name'] == remove_book:
                del wishlist[i]
                save_data(books, wishlist)
                CLI.show_to_user("The book was removed from your shelf!")
                return
            i += 1

        CLI.show_to_user("This book is not in your wishlist bookshelf. Please try again!")

def random_book_wish(books, wishlist):
    """
    This will provide a random book name from the wishlist.
    """
    if len(wishlist) == 0:
        CLI.show_to_user("There's no books in your bookshelf, please add one book first.")
        return
    import random
    book_wish = random.choice(wishlist)
    CLI.show_to_user(f"We chose: {book_wish['name']} for you! ")

def show_bookshelf_wish(books, wishlist):
    """
    This shows the entire read bookshelf with name and number in the list.
    """
    if len(wishlist) == 0:
        CLI.show_to_user("There's no books in your bookshelf, please add one book first.")
        return
    index = 0
    for book in wishlist:
        index += 1
        CLI.show_to_user(f"{index}. {book['name']}")


#dictionary for the functions
wishlist_option_to_function = {}
wishlist_option_to_function[1] = add_book_wish
wishlist_option_to_function[2] = edit_shelf_wish
wishlist_option_to_function[3] = remove_book_wish
wishlist_option_to_function[4] = random_book_wish
wishlist_option_to_function[5] = show_bookshelf_wish

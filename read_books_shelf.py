from utils import find_unique_book
from utils import save_data

def add_book_read(books, wishlist):
    """
    This adds some book in the read bookshelf.
    """
    name_book = input("Write the name of the book: ")
    books.append({"name": name_book})
    save_data(books, wishlist)
    print("The book was succesfully added :)")

def sort_key(d):
    return d["name"]

def edit_shelf_read(books, wishlist):
    """
    This function is used to sort the list from A-Z or to reverse the list.
    """
    while True:
        if len(books) == 0:
            print("There's no books in your bookshelf, please add one book.")
            return
        try:
            edit_read = int(input(" 1. Sort A-Z \n 2. Reverse List \n How do you want to edit? "))
            if edit_read == 1:
                #sort the list from A-Z
                books.sort(key=sort_key)
                save_data(books, wishlist)
                print("Your wishlist is now sorted from A-Z!")
            elif edit_read == 2:
                #reverse the entire list
                books.reverse()
                save_data(books, wishlist)
                print("Your wishlist is reversed!")
            else:
                raise ValueError()
            break
        except Exception:
            print("You need to choose a number from 1-2")

def remove_book_read(books, wishlist):
    """
    This functions remove some book from the read list.
    """
    while True:
        if len(books) == 0:
            print("There's no books in your bookshelf, please add one book.")
            return
        show_bookshelf_read(books, wishlist)
        remove_book = input("Write the NAME of the book you want to remove: ")
        i = 0
        for rem in books:
            if rem['name'] == remove_book:
                del books[i]
                save_data(books, wishlist)
                print("The book was removed from your shelf!")
                return
            i += 1

        print("This book is not in your bookshelf. Please try again!")

def info_book_read(books, wishlist):
    """
    This is going to add some aditional information for that book.
    It can rate the book, insert the date of ending or write something that the user want to remember about that book.
    """
    while True:
        if len(books) == 0:
            print("There's no books in your bookshelf, please add one book.")
            return
        choice = int(input("1. Rate the book. \n2. Date of ending. \n3. Write some detail. \n Which information you want to add? "))
        try: 
            if choice == 1:
                #this will add the rating (by stars) for certain book
                while True:
                    show_bookshelf_read(books, wishlist)
                    find_name = input("What is the NAME of the book you want to add rating? ")
                    book = find_unique_book(books, find_name)
                    if book is None:
                        continue
                    rate = input("Write how many stars this book deserves: ")
                    book["rating"] = rate
                    save_data(books, wishlist)
                    print("Now, the rate is available in option 5!")
                    break
            if choice == 2:
                #this will add the ending date of certain book
                while True:
                    show_bookshelf_read(books, wishlist)
                    name = input("What is the name of the book you want to add date? ")
                    book = find_unique_book(books, name)
                    if book is None:
                        continue
                    date = input("Which day did you finished: ")
                    book["date"] = date
                    save_data(books, wishlist)
                    print("Now, the date is available in option 5!")
                    break
            if choice == 3:
                #this will add the aditional informations that the user wants
                while True:
                    show_bookshelf_read(books, wishlist)
                    get_name = input("What is the name of the book you want to add info? ")
                    book = find_unique_book(books, get_name)
                    if book is None:
                        continue
                    info = input("Write the details: ")
                    book["informations"] = info
                    save_data(books, wishlist)
                    print("Now, the details are available in option 5!")
                    break
            break
        except:
            print("Please choose a number between 1-3!")
            raise ValueError

def show_information_book(books, wishlist):
    """
    Show some information about one book
    """
    if len(books) == 0:
        print("There's no books in your bookshelf, please add one book.")
        return
    index = 0
    for book in books:
        index += 1
        print(f"{index}. {book['name']} \n{book.get('rating')} stars \nFinish date: {book.get('date')} \nDetails: {book.get('informations')}")

def show_bookshelf_read(books, wishlist):
    """
    This shows the entire read bookshelf with name and number in the list
    """
    if len(books) == 0:
        print("There's no books in your bookshelf, please add one book.")
        return
    index = 0
    for book in books:
        index += 1
        print(f"{index}. {book['name']}")


#dictionary for the functions
book_shelf_option_to_function = {}
book_shelf_option_to_function[1] = add_book_read
book_shelf_option_to_function[2] = edit_shelf_read
book_shelf_option_to_function[3] = remove_book_read
book_shelf_option_to_function[4] = info_book_read
book_shelf_option_to_function[5] = show_information_book
book_shelf_option_to_function[6] = show_bookshelf_read

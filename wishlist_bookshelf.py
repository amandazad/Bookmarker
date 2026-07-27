def add_book_wish(wishlist):
    name_wishlist = input("Write the name of the book: ")
    wishlist.append({"name": name_wishlist})
    print("The book was succesfully added :)")

def edit_shelf_wish(wishlist):
    while True:
        try:
            edit_wishlist = int(input(" 1. Sort A-Z \n 2. Reverse List \n 3. Clear List \n How do you want to edit?"))
            if edit_wishlist == 1:
                wishlist.sort()
                print("Your wishlist is now sorted from A-Z!")
            elif edit_wishlist == 2:
                wishlist.reverse()
                print("Your wishlist is reversed!")
            elif edit_wishlist == 3:
                wishlist.clear()
                print("Your wishlist is cleared!")
            else:
                raise ValueError()
            break
        except Exception:
            print("You need to choose a number from 1-3")

    

def remove_book_wish(wishlist):
    pass

def random_book_wish(wishlist):
    pass

def show_bookshelf_wish(wishlist):
    index = 0
    for book in wishlist:
        index += 1
        print(f"{index}. {book['name']}")



wishlist_option_to_function = {}
wishlist_option_to_function[1] = add_book_wish
wishlist_option_to_function[2] = edit_shelf_wish
wishlist_option_to_function[3] = remove_book_wish
wishlist_option_to_function[4] = random_book_wish
wishlist_option_to_function[5] = show_bookshelf_wish
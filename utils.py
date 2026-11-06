"""
This module contains helper functions.
"""
import json

from pathlib import Path

def find_books(lst, ask_name_book):
    #to locate if the book is in the system already and return the list
    result_list = []
    for book in lst:
        if ask_name_book in book["name"]:
            result_list.append(book)
    return result_list

def find_unique_book(lst, ask_name_book):
    import CLI
    #to find the exact book, not all with that word
    books = find_books(lst, ask_name_book)
    if len(books) == 1:
        return books[0]
    if len(books) > 1:
        index = 0
        for book in books:
            index += 1
            CLI.show_to_user(f"{index}. {book['name']}")
        exact_book = CLI.request_exact_book()
        exact_book = int(exact_book)
        return books[exact_book - 1]
    CLI.show_to_user("You don't have this book on the list.")
    return None

DATA_FILE = Path(__file__).resolve().parent / "data.json"
USERS_FILE = Path(__file__).resolve().parent / "users.json"

def load_data():
    #this is for when the user is reading, which is going to only load the data
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data["books"], data["wishlist"]
    except FileNotFoundError:
        return [], []
    except json.JSONDecodeError:
        return [], []


def save_data(books, wishlist):
    #this one is for writing, so it is going to save the edited data
    data = {"books": books, "wishlist": wishlist}
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        import CLI
        CLI.show_to_user("There was a problem saving your data.")


def update_data_users(users):
    #this one is for writing, so it is going to save the edited data
    data = {"users": users}
    try:
        with open(USERS_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        import CLI
        CLI.show_to_user("There was a problem making your login.")


def load_data_users():
    #this is for when the user is reading, which is going to only load the data
    try:
        with open(USERS_FILE, "r") as file:
            data = json.load(file)
            return data["users"]
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

"""
This module contains helper functions.
"""
import json

def find_books(lst, ask_name_book):
    #to locate if the book is in the system already and return the list
    result_list = []
    for book in lst:
        if ask_name_book in book["name"]:
            result_list.append(book)
    return result_list

def find_unique_book(lst, ask_name_book):
    #to find the exact book, not all with that word
    books = find_books(lst, ask_name_book)
    if len(books) == 1:
        return books[0]
    if len(books) > 1:
        index = 0
        for book in books:
            index += 1
            print(f"{index}. {book['name']}")
        exact_book = int(input("What is the NUMBER of the book you are looking for? "))
        return books[exact_book - 1]
    print("You don't have this book on the list.")
    return None


def load_data():
    #this is for when the user is reading, which is going to only load the data
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data["books"], data["wishlist"]
    except FileNotFoundError:
        return [], []


def save_data(books, wishlist):
    #this one is for writing, so it is going to save the edited data
    data = {"books": books, "wishlist": wishlist}
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
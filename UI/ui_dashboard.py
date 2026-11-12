from unicodedata import name

import streamlit as st
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

import utils

def open_dashboard():
    st.set_page_config(page_title="Bookmarker App", page_icon=":books:", layout="wide")

    with st.container(horizontal_alignment="center"):
        st.title(":open_book: Welcome to the bookmarker app!",
                width="content", 
                anchor=False)

    books, wishlist = utils.load_data()
    show_bookshelf_read(books, wishlist)
    show_bookshelf_wishlist(books, wishlist)

def show_bookshelf_read(books, wishlist):
    with st.form(key="new_item_form", border=False):
        with st.container(
            horizontal=True,
            vertical_alignment="bottom",
        ):
            st.text_input(
                "Book name",
                placeholder="Enter the name of the book you want to add to your bookshelf",
                key="name",
            )

            st.text_input(
                "Rate the book",
                placeholder="Rate the book from 1 to 5",
                key="rating",
            )

            st.date_input(
                "Date of reading",
                value="today",
                key="date",
                format="YYYY-MM-DD",
            )

            st.text_input(
                "Add details about the book",
                placeholder="Enter any additional details about the book",
                key="informations"
            )

            st.form_submit_button("Add Book", on_click=add_book_to_bookshelf)

    st.subheader("Your Bookshelf")
    if len(books) == 0:
        st.info("There's no books in your bookshelf, please add one book.")
    else:
        with st.container(border=True):
            # Table header
            widths = [3, 1, 2, 3, 1, 1]
            header = st.columns(widths)

            header[0].markdown("**Book**")
            header[1].markdown("**Rating**")
            header[2].markdown("**Date of Reading**")
            header[3].markdown("**Details**")
            header[4].markdown("**Edit**")
            header[5].markdown("**Remove**")

            st.divider()

            # Table rows
            for index, book in enumerate(books):
                columns = st.columns(widths, vertical_alignment="center")

                columns[0].write(f"{index + 1}. {book['name']}")
                columns[1].write(book.get("rating", ""))
                columns[2].write(book.get("date", ""))
                columns[3].write(book.get("informations", ""))

                # Buttons can be implemented here later
                columns[4].button(
                    "Edit",
                    key=f"edit_{index}",
                )
                columns[5].button(
                    "🗑️",
                    key=f"remove_{index}",
                    on_click=remove_book_from_bookshelf,
                    args=(index, books, wishlist),
                )


def show_bookshelf_wishlist(books, wishlist):
    with st.form(key="wish_item_form", border=False):
        with st.container(
            horizontal=True,
            vertical_alignment="bottom",
        ):
            st.text_input(
                "Book name",
                placeholder="Enter the name of the book you want to add to your wishlist",
                key="w_name",
            )

            st.form_submit_button("Add Book", on_click=add_book_to_wishlist)

    st.subheader("Your Wishlist")
    if len(wishlist) == 0:
        st.info("There's no books in your wishlist, please add one book.")
    else:
        with st.container(border=True):
            # Table header
            widths = [3, 1, 1]
            header = st.columns(widths)

            header[0].markdown("**Book**")
            header[1].markdown("**Edit**")
            header[2].markdown("**Remove**")

            st.divider()

            # Table rows
            for index, book in enumerate(wishlist):
                columns = st.columns(widths, vertical_alignment="center")

                columns[0].write(f"{index + 1}. {book['name']}")

                columns[1].button(
                    "Edit",
                    key=f"edit_wishlist_{index}",
                )
                columns[2].button(
                    "🗑️",
                    key=f"remove_wishlist_{index}",
                    on_click=remove_book_from_wishlist,
                    args=(index, books, wishlist),
                )


def remove_book_from_bookshelf(index, books, wishlist):
    books.pop(index)
    utils.save_data(books, wishlist)


def remove_book_from_wishlist(index, books, wishlist):
    wishlist.pop(index)
    utils.save_data(books, wishlist)


def add_book_to_bookshelf():
    books, wishlist = utils.load_data()
    new_book = {
        "name": st.session_state.name,
        "rating": st.session_state.rating,
        "date": str(st.session_state.date),
        "informations": st.session_state.informations
    }
    if not name:
            st.warning("Please enter a book name.")
            return

    books.append(new_book)
    utils.save_data(books, wishlist)


def add_book_to_wishlist():
    books, wishlist = utils.load_data()
    name = st.session_state.w_name.strip()

    if not name:
        st.warning("Please enter a book name.")
        return
    
    wishlist.append({"name": name})
    utils.save_data(books, wishlist)


# Run on import!
open_dashboard()
import streamlit as st

def show_bookshelf_read(books, wishlist):
    print("\033[1;93m\n --- Your read books --- \n\033[0m")
    if len(books) == 0:
        print("There's no books in your bookshelf, please add one book.")
    else:
        for index, book in enumerate(books):
            print(f"{index + 1}. {book['name']}")

def show_bookshelf_wish(books, wishlist):
    print("\033[1;96m\n --- Your wishlist --- \n\033[0m")
    if len(wishlist) == 0:
        print("There's no books in your wishlist, please add one book.")
    else:
        for index, book in enumerate(wishlist):
            print(f"{index + 1}. {book['name']}")


def open_dashboard():
    st.set_page_config(page_title="Bookmarker App", page_icon=":books:", layout="wide")

    with st.container(horizontal_alignment="center"):
        st.title(":pink[:material/:open_book:] Welcome to the bookmarker app! Here's your bookshelf:",
                width="content", 
                anchor=False)

    with st.form(key="new_item_form", border=False):
        with st.container(
            horizontal=True,
            vertical_alignment="bottom",
        ):
            st.text_input(
                "Book name:",
                label_visibility="collapsed",
                placeholder="Enter the name of the book you want to add to your bookshelf",
                key="name",
            )

            st.text_input(
                "Rate the book:",
                label_visibility="collapsed",
                placeholder="Rate the book from 1 to 5",
                key="rating",
            )

            st.date_input(
                "Date of reading:",
                value="today",
                key="date",
                format="YYYY-MM-DD",
            )

            st.text_input(
                "Add details about the book:",
                label_visibility="collapsed",
                placeholder="Enter any additional details about the book",
                key="informations"
            )

            st.selectbox(
                "Select the bookshelf:",
                options=["Read Bookshelf", "Wishlist"],
                label_visibility="collapsed",
                key="bookshelf"
            )

            st.form_submit_button("Add Book", on_click=add_book_to_bookshelf)

def add_book_to_bookshelf():
    pass

open_dashboard()
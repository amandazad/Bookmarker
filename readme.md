*Project Overview*

The Bookmarker is a Python application designed to help readers organize and keep track of their reading experiences. It provides a simple and interactive interface where users can manage the books they have read and the ones they wish to read in the future.

1. Features

- Personal Bookshelf: Add books you have read, including their names, ratings, reading dates, and additional information.

- Wishlist: Create a list of books you want to read in the future.

- Edit Books: Update book information whenever necessary.

- Remove Books: Delete entries from your bookshelf or wishlist.

- Data Storage: Save and load book information using JSON files, allowing data to persist between sessions.

2. Technologies

- Python
- Streamlit
- JSON

3. Project Structure

- UI: Main application file containing the Streamlit interface and application functionality.

- main.py: Is where the main options for the user to choose is located.

- read_books_shelf.py: Contains the functions of the read bookshelf.

- wishlist_bookshelf.py: Contains the functions of the wishlist bookshelf.

- utils.py: Contains helper functions for searching, loading, and saving book information.

- data/: Stores the application's JSON data.

4. How to Run

- Open your terminal, navigate to the project directory, and execute:
        streamlit run UI/ui_login.py
        or
        streamlir run UI/ui_dashboard.py

- The application will open in your browser, allowing you to organize your personal bookshelf and wishlist.

5. Purpose

This project was developed to practice Python programming, application development, data management, and user interface design while creating a practical tool for everyday reading.
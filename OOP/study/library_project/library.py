from book import Book, InvalidPageCount, BookNotFoundError
import os
import json

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_instance):
        if any(book.title == book_instance.title for book in self.books):
            raise ValueError(f"{book_instance.title} already exists in library")
        self.books.append(book_instance)

    def show_books(self):
        print("-------Library Inventory-------")
        if not self.books:
            print("The library is empty")
            return
        for book in self.books:
            print(f"Book: {book.title} by {book.author} ({book.pages} pages)")

    def get_long_books(self):
        return [book for book in self.books if book.pages > 300]

    def find_by_author(self, author_name):
        search_term = author_name.lower()
        return [book for book in self.books if search_term in book.author.lower()]

    def find_by_genre(self, genre_name):
        search_term = genre_name.lower()
        return [book for book in self.books if search_term in book.genre.lower()]

    def remove_book(self, title):
        book_to_remove = next(
            (book for book in self.books if book.title.lower() == title.lower()),
            None
        )

        if book_to_remove is None:
            raise BookNotFoundError(f"Book '{title}' not found in library.")
        self.books.remove(book_to_remove)

    def get_most_pages(self):
        if not self.books:
            raise ValueError("There are no books in library")

        return max(self.books, key=lambda book: book.pages)

    def save_to_file(self, filename):
        data = [book.to_dict() for book in self.books]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return

        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError, InvalidPageCount, KeyError):
            self.books = []
            print("Error reading from file. Please check the file and try again.")

    def __str__(self):
        if not self.books:
            return "Library: empty"
        book_list = "\n".join(f"  -  {book}" for book in self.books)
        return f"Library: {len(self.books)} book(s)\n{book_list}"
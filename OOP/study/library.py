class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_instance):
        if any(book.title == book_instance.title for book in self.books):
            return
        self.books.append(book_instance)

    def get_long_books(self):
        return [book for book in self.books if book.pages > 300]

    def find_by_author(self, author_name):
        search_term = author_name.lower()
        return [book for book in self.books if search_term in book.author.lower()]

    def remove_book(self, title):
        book_to_remove = None
        for book in self.books:
            if book.title.lower() == title.lower():
                book_to_remove = book
                break

        if book_to_remove:
            self.books.remove(book_to_remove)
            return f"Successfully removed book '{book_to_remove.title}' from library"
        else:
            raise ValueError(f"Book '{title}' not found in library.")

    def get_most_pages(self):
        if not self.books:
            raise ValueError(f"There are no books in library")

        return max(self.books, key=lambda book: book.pages)

    def __str__(self):
        if not self.books:
            return "Library: empty"
        book_list = "\n".join(f"  -  {book}" for book in self.books)
        return f"Library: {len(self.books)} book(s)\n{book_list}"

lib = Library()

b1 = Book("1984", "George Orwell", 328)
b2 = Book("Animal Farm", "orwell", 112)
b3 = Book("The Hobbit", "Tolkien", 310)

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(Book("1984", "Orwell", 328))

print(lib)
print(f"Long books: {[book.title for book in lib.get_long_books()]}")
print(f"Orwell books: {[book.title for book in lib.find_by_author('ORWELL')]}")

try:
    print(lib.remove_book("Moby Dick"))
except ValueError as e:
    print(f"Error: {e}")

try:
    print(lib.get_most_pages())
except ValueError as e:
    print(f"Error: {e}")


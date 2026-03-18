class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        # Composition: Library HAS a list of books
        self.books = []

    def add_book(self, book_instance):
        # We store the whole object, not just the string name
        self.books.append(book_instance)
        print(f"Added: {book_instance.title}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"You borrowed: {book.title}")
                return True
        print(f"Error: {title} not found")
        return False

    def show_books(self):
        print("-------Library Inventory-------")
        if not self.books:
            print("The library is empty")
            return
        for book in self.books:
            print(f"Book: {book.title}")

my_library = Library()
book1 = Book("Python Basics")
book2 = Book("OOP for dummies")

my_library.add_book(book1)
my_library.add_book(book2)

my_library.show_books()
my_library.borrow_book("Python Basics")
my_library.show_books()
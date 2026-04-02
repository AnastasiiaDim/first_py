from library import Library
from book import Book

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

print(f"Biggest book: {lib.get_most_pages()}")


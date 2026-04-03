from library import Library
from book import Book

lib = Library()

# CLI
print("Welcome to the library!")
while True:
    print("\n-----Menu-----:")
    print("1. Add a book")
    print("2. List all books")
    print("3. Find by author")
    print("4. Remove a book")
    print("5. Show longest book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "6":
        print("Bye! Hope to see you again!")
        break

    if choice == "1":
        user_title = input("Enter a book title: ")
        user_author = input("Enter a book author: ")
        try:
            user_pages = int(input("Enter a book page count: "))
            new_book = Book(user_title, user_author, user_pages)
            lib.add_book(new_book)
            print(f"Successfully added {new_book}.")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "2":
        print(lib)

    elif choice == "3":
        user_author = input("Enter a book author: ")
        found_books = lib.find_by_author(user_author)
        if not found_books:
            print(f"Sorry, no books by {user_author} were found.")
        else:
            print(f"Books by {user_author}:")
            for book in found_books:
                print(f"- {book.title}")

    elif choice == "4":
        title_to_remove = input("Enter a book you want to remove: ")
        try:
            lib.remove_book(title_to_remove)
            print(f"Successfully removed '{title_to_remove}'.")
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "5":
        try:
            longest = lib.get_most_pages()
            print(f"The longest book is {longest}")
        except ValueError as e:
            print(f"Notification: {e}")

    else:
        print(f"Sorry, {choice} is not a valid option.")

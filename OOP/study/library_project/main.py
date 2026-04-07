from library import Library
from book import Book, InvalidPageCount, BookNotFoundError

lib = Library()
lib.load_from_file("library.json")
# CLI
print("Welcome to the library!")
while True:
    print("\n-----Menu-----:")
    print("1. Add a book")
    print("2. List all books")
    print("3. Find by author")
    print("4. Find by genre")
    print("5. Remove a book")
    print("6. Show longest book")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "7":
        print("Bye! Hope to see you again!")
        break

    if choice == "1":
        user_title = input("Enter a book title: ")
        user_author = input("Enter a book author: ")
        user_genre = input("Enter a book genre (leave blank for Unknown): ") or "Unknown"
        new_book = Book(user_title, user_author, user_pages, user_genre)
        try:
            user_pages = int(input("Enter a book page count: "))

            lib.add_book(new_book)
            print(f"Successfully added {new_book}.")
        except ValueError as e:
            print(f"Error: {e}")
        except InvalidPageCount as e:
            print(f"Error: {e}")

        lib.save_to_file("library.json")

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
        user_genre = input("Enter a book genre: ")
        found_books = lib.find_by_genre(user_genre)
        if not found_books:
            print(f"Sorry, no books by {user_genre} were found.")
        else:
            print(f"Books by {user_genre}:")
            for book in found_books:
                print(f"- {book.title}")

    elif choice == "5":
        title_to_remove = input("Enter a book you want to remove: ")
        try:
            lib.remove_book(title_to_remove)
            print(f"Successfully removed '{title_to_remove}'.")
        except BookNotFoundError as e:
            print(f"Error: {e}")

        lib.save_to_file("library.json")

    elif choice == "6":
        try:
            longest = lib.get_most_pages()
            print(f"The longest book is {longest}")
        except ValueError as e:
            print(f"Notification: {e}")

    else:
        print(f"Sorry, {choice} is not a valid option.")

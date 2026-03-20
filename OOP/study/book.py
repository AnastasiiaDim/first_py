class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

    def summary(self):
        return f"{self.title} by {self.author} - {self.pages} pages"

    def __str__(self):
        return self.summary()

book1 = Book("Thinking Fast and Slow", "D. Kahneman", 600)
book2 = Book("Animal Farm", "G. Orwell", 150)

print(book1.is_long())
print(book1)
#instead of book1.summary() we use method __str__, Python calls __str__ automatically
# whenever it needs to display an object as text. That's the whole point of it — your
# object learns how to describe itself, so you never have to call .summary() manually


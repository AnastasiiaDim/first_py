class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

    def summary(self):
        return f"{self.title} by {self.author} - {self.pages} pages"

    def add_pages(self, amount):
        if amount <= 0:
            return
        self.pages += amount

    def reading_progress(self, pages_read):
        if pages_read <= 0 or pages_read > self.pages:
            return 0.0
        return round(pages_read / self.pages * 100, 1)

    def __str__(self):
        return self.summary()

book1 = Book("Thinking Fast and Slow", "D. Kahneman", 600)

book1.add_pages(50)        # valid — pages becomes 650
book1.add_pages(-10)       # invalid — nothing happens

print(book1)               # 650 pages now
print(book1.is_long())     # True
print(book1.reading_progress(325))   # 50.0
print(book1.reading_progress(-5))    # 0.0  ← testing the guard
print(book1.reading_progress(9999))  # 0.0  ← testing the other guard

#instead of book1.summary() we use method __str__, Python calls __str__ automatically
# whenever it needs to display an object as text. That's the whole point of it — your
# object learns how to describe itself, so you never have to call .summary() manually


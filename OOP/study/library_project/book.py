class InvalidPageCount(Exception):
    pass

class BookNotFoundError(Exception):
    pass

class Book:
    def __init__(self, title, author, pages, genre="Unknown"):
        if pages <= 0:
            raise InvalidPageCount("Page count must be greater than zero.")
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "genre": self.genre
        }
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages, genre: {self.genre})"
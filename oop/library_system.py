# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
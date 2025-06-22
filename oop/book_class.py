# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message upon deletion of the Book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string that can recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
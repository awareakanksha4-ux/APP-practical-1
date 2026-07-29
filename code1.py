class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(patron.name, "registered successfully.")

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(patron.name, "borrowed", book.title)
        else:
            print(book.title, "is not available.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            print(patron.name, "returned", book.title)
        else:
            print("Book was not borrowed by", patron.name)


library = Library()

book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Java Programming", "James Gosling")
book3 = Book("C Programming", "Dennis Ritchie")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

patron1 = Patron("Rahul")
patron2 = Patron("Priya")

library.register_patron(patron1)
library.register_patron(patron2)

library.borrow_book(patron1, book1)
library.borrow_book(patron2, book2)
library.borrow_book(patron2, book1)

library.return_book(patron1, book1)

library.borrow_book(patron2, book1)

print("-------- Final Status --------")

for book in library.books:
    print(book.title, "-", book.available)

for patron in library.patrons:
    print(patron.name, "has borrowed:")
    if len(patron.borrowed_books) == 0:
        print("No books")
    else:
        for book in patron.borrowed_books:
            print(book.title)
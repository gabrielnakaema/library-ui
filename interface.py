from database import Book, session


def select_all_books():
    return session.query(Book).all()


def insert_one_book(barcode, title, author, amount):
    new_book = Book(barcode, title, author, amount)
    session.add(new_book)
    session.commit()

from database import Book, session


def select_all_books():
    return session.query(Book).order_by(Book.title).all()

def select_one_book(barcode):
    return session.query.filter(Book.barcode == barcode).first()


def insert_one_book(barcode, title, author, amount):
    new_book = Book(barcode, title, author, amount)
    session.add(new_book)
    session.commit()

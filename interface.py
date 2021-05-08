from database import Book, session


def select_all_books():
    return session.query(Book).all()


def insert_one_book(barcode, title, author, amount):
    new_book = Book(barcode, title, author, amount)
    session.add(new_book)
    session.commit()


 def loadData(self):
        book_list = interface.select_all_books()
        self.booksTableWidget.setRowCount(len(book_list))

        for book in book_list:
            if self.book_filter["barcode"] in book.barcode:
                self.booksTableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(book.barcode))
                self.booksTableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(book.title))
                self.booksTableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(book.author))
                self.booksTableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem(str(book.amount)))
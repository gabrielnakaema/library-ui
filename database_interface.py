from database import connection
from PyQt5.QtSql import QSqlQuery
from datetime import datetime

def insertBook(barcode, title, author, amount):
    insertQuery = QSqlQuery(connection)
    insertQuery.prepare(
    """INSERT INTO books(barcode, title, author, amount_available, amount_borrowed) VALUES(?,?,?,
        ?, 0)
        ON CONFLICT(barcode) DO UPDATE SET amount_available=amount_available+?;
    """)
    insertQuery.addBindValue(barcode)
    insertQuery.addBindValue(title)
    insertQuery.addBindValue(author)
    insertQuery.addBindValue(amount)
    insertQuery.addBindValue(amount)
    insertQuery.exec()

def addOneBorrowedBook(barcode, title, author):
    insertQuery = QSqlQuery(connection)
    insertQuery.prepare(
        """
        INSERT INTO books(barcode, title, author, amount_available, amount_borrowed) VALUES(?,?,?,0,1)
        ON CONFLICT(barcode) DO UPDATE SET amount_available=amount_available-1, amount_borrowed=amount_borrowed+1;
        """
    )
    insertQuery.addBindValue(barcode)
    insertQuery.addBindValue(title)
    insertQuery.addBindValue(author)
    insertQuery.exec()
    updateNegativeAmountQuery = QSqlQuery(connection)
    updateNegativeAmountQuery.exec(
        """
        UPDATE books
        SET amount_available=0
        WHERE amount_available<0
        """
    )


def addWithdrawalEntry(barcode, student_name, student_grade):
    current_date = datetime.now().strftime("%d/%m/%Y")
    insertWithdrawalQuery = QSqlQuery(connection)
    insertWithdrawalQuery.prepare(
        """
        INSERT INTO withdrawals(book_barcode, student_name, student_grade, withdrawal_date) VALUES(?,?,?,?)
        """
    )
    insertWithdrawalQuery.addBindValue(barcode)
    insertWithdrawalQuery.addBindValue(student_name)
    insertWithdrawalQuery.addBindValue(student_grade)
    insertWithdrawalQuery.addBindValue(current_date)
    insertWithdrawalQuery.exec()

def returnOneBook(id, barcode):
    currentDate = datetime.now().strftime("%d/%m/%Y")
    returnBookQuery = QSqlQuery(connection)
    returnBookQuery.prepare(
        """
        UPDATE withdrawals
        SET is_returned=1, return_date=?
        WHERE id=?
        """
    )
    returnBookQuery.addBindValue(currentDate)
    returnBookQuery.addBindValue(id)
    returnBookQuery.exec()
    updateBookEntryQuery = QSqlQuery(connection)
    updateBookEntryQuery.prepare(
        """
        UPDATE books
        SET amount_available=amount_available+1, amount_borrowed=amount_borrowed-1
        WHERE barcode=?
        """
    )
    updateBookEntryQuery.addBindValue(barcode)
    updateBookEntryQuery.exec()

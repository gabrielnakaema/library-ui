import sys
from PyQt5.QtSql import QSqlQuery
from database import connection


def initialize_db():
    if not connection.open():
        print("Database Error : %s" % connection.lastError().databaseText())
        sys.exit(1)

    createBookTableQuery = QSqlQuery(connection)
    createBookTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS books (
            barcode VARCHAR(50) PRIMARY KEY UNIQUE NOT NULL,
            title VARCHAR(100) NOT NULL,
            author VARCHAR(100),
            amount_available INTEGER DEFAULT 0,
            amount_borrowed INTEGER DEFAULT 0
        )
        """
    )

    createWithdrawalsTableQuery = QSqlQuery(connection)
    createWithdrawalsTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS withdrawals (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            book_barcode VARCHAR(50),
            student_name VARCHAR(100) NOT NULL,
            student_grade VARCHAR(100),
            withdrawal_date VARCHAR(50) NOT NULL,
            is_returned BOOLEAN DEFAULT 0,
            return_date VARCHAR(50),
            FOREIGN KEY(book_barcode) REFERENCES books(barcode)
        )
        """
    )


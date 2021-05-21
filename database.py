from PyQt5.QtSql import QSqlDatabase

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName("library.sqlite")

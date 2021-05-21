# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Biblioteca.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import PyQt5.QtSql
from PyQt5 import QtCore, QtGui, QtWidgets

import database_interface
from database import connection

class Ui_MainWidget(object):

    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(891, 684)
        self.gridLayout = QtWidgets.QGridLayout(MainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(MainWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(651, 621))
        self.tabWidget.setObjectName("tabWidget")

        # AUTO RESIZING LAYOUT
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # BOOKS TAB

        self.booksTab = QtWidgets.QWidget()
        self.booksTab.setObjectName("booksTab")
        sizePolicy.setHeightForWidth(self.booksTab.sizePolicy().hasHeightForWidth())
        self.booksTabLayout = QtWidgets.QGridLayout(self.booksTab)
        self.booksTabLayout.setObjectName("booksTabLayout")

        self.booksModel = PyQt5.QtSql.QSqlTableModel()
        self.booksModel.setTable("books")
        self.booksModel.setEditStrategy(PyQt5.QtSql.QSqlTableModel.OnFieldChange)
        self.booksModel.setHeaderData(0, QtCore.Qt.Horizontal, "Codigo")
        self.booksModel.setHeaderData(1, QtCore.Qt.Horizontal, "Titulo")
        self.booksModel.setHeaderData(2, QtCore.Qt.Horizontal, "Autor")
        self.booksModel.setHeaderData(3, QtCore.Qt.Horizontal, "Qtd Disp")
        self.booksModel.setHeaderData(4, QtCore.Qt.Horizontal, "Qtd Retirada")

        self.booksModel.select()
        self.booksView = PyQt5.QtWidgets.QTableView(self.booksTab)
        self.booksView.setObjectName("booksView")
        self.booksView.setMinimumSize(500, 300)
        sizePolicy.setHeightForWidth(self.booksView.sizePolicy().hasHeightForWidth())
        self.booksView.setModel(self.booksModel)
        self.booksView.resizeColumnsToContents()
        self.booksView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.booksView.setSortingEnabled(True)
        self.booksView.selectionModel().selectionChanged.connect(self.handleBookSelectionChange)
        self.booksTabLayout.addWidget(self.booksView, 2, 0, 0, 1)

        # Books search form

        self.booksSearchFrame = QtWidgets.QFrame(self.booksTab)
        self.booksSearchFrame.setGeometry(QtCore.QRect(10, 10, 241, 171))
        self.booksSearchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.booksSearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.booksSearchFrame.setObjectName("booksSearchFrame")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.booksSearchFrame)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 221, 151))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.booksSearchFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.booksSearchFormLayout.setContentsMargins(0, 0, 0, 0)
        self.booksSearchFormLayout.setObjectName("booksSearchFormLayout")
        self.booksSearchLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.booksSearchLabel.setStyleSheet("font-size:16px;\n"
"")
        self.booksSearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.booksSearchLabel.setObjectName("booksSearchLabel")
        self.booksSearchFormLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.booksSearchLabel)
        self.booksSearchBarcodeLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.booksSearchBarcodeLabel.setStyleSheet("font-size:16px")
        self.booksSearchBarcodeLabel.setObjectName("booksSearchBarcodeLabel")
        self.booksSearchFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.booksSearchBarcodeLabel)
        self.booksSearchBarcodeInput = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.booksSearchBarcodeInput.setObjectName("booksSearchBarcodeInput")
        self.booksSearchBarcodeInput.returnPressed.connect(self.handleBarcodeInputEnter)
        self.booksSearchFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.booksSearchBarcodeInput)
        self.booksSearchTitleLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.booksSearchTitleLabel.setStyleSheet("font-size:16px")
        self.booksSearchTitleLabel.setObjectName("booksSearchTitleLabel")
        self.booksSearchFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.booksSearchTitleLabel)
        self.booksSearchTitleInput = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.booksSearchTitleInput.setObjectName("booksSearchTitleInput")
        self.booksSearchFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.booksSearchTitleInput)
        self.booksSearchAuthorLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.booksSearchAuthorLabel.setStyleSheet("font-size:16px")
        self.booksSearchAuthorLabel.setObjectName("booksSearchAuthorLabel")
        self.booksSearchFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.booksSearchAuthorLabel)
        self.booksSearchAuthorInput = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.booksSearchAuthorInput.setObjectName("booksSearchAuthorInput")
        self.booksSearchFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.booksSearchAuthorInput)

        # Add book amount form

        self.booksAmountFrame = QtWidgets.QFrame(self.booksTab)
        self.booksAmountFrame.setGeometry(QtCore.QRect(260, 10, 241, 101))
        self.booksAmountFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.booksAmountFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.booksAmountFrame.setObjectName("booksAmountFrame")
        self.formLayoutWidget = QtWidgets.QWidget(self.booksAmountFrame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.booksAmountFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.booksAmountFormLayout.setContentsMargins(0, 0, 0, 0)
        self.booksAmountFormLayout.setObjectName("booksAmountFormLayout")
        self.booksAmountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.booksAmountLabel.setStyleSheet("font-size:16px")
        self.booksAmountLabel.setObjectName("booksAmountLabel")
        self.booksAmountFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.booksAmountLabel)
        self.booksAmountInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.booksAmountInput.setObjectName("booksAmountInput")
        self.booksAmountFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.booksAmountInput)
        self.booksAmountButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.booksAmountButton.setObjectName("booksAmountButton")
        self.booksAmountButton.pressed.connect(self.insertBook)
        self.booksAmountFormLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.booksAmountButton)

        # Book withdrawal form

        self.booksWithdrawalFrame = QtWidgets.QFrame(self.booksTab)
        self.booksWithdrawalFrame.setGeometry(QtCore.QRect(260, 110, 241, 131))
        self.booksWithdrawalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.booksWithdrawalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.booksWithdrawalFrame.setObjectName("booksWithdrawalFrame")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.booksWithdrawalFrame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 221, 112))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.booksWithdrawalFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.booksWithdrawalFormLayout.setContentsMargins(0, 0, 0, 0)
        self.booksWithdrawalFormLayout.setObjectName("booksWithdrawalFormLayout")
        self.booksWithdrawalStudentLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.booksWithdrawalStudentLabel.setStyleSheet("font-size:16px")
        self.booksWithdrawalStudentLabel.setObjectName("booksWithdrawalStudentLabel")
        self.booksWithdrawalFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.booksWithdrawalStudentLabel)
        self.booksWithdrawalStudentInput = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.booksWithdrawalStudentInput.setObjectName("booksWithdrawalStudentInput")
        self.booksWithdrawalFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.booksWithdrawalStudentInput)
        self.booksWithdrawalGradeLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.booksWithdrawalGradeLabel.setStyleSheet("font-size:16px")
        self.booksWithdrawalGradeLabel.setObjectName("booksWithdrawalGradeLabel")
        self.booksWithdrawalFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.booksWithdrawalGradeLabel)
        self.booksWithdrawalGradeInput = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.booksWithdrawalGradeInput.setObjectName("booksWithdrawalGradeInput")
        self.booksWithdrawalFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.booksWithdrawalGradeInput)
        self.booksWithdrawalButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.booksWithdrawalButton.setObjectName("booksWithdrawalButton")
        self.booksWithdrawalButton.pressed.connect(self.withdrawBook)
        self.booksWithdrawalFormLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.booksWithdrawalButton)

        # WITHDRAWALS TAB

        self.tabWidget.addTab(self.booksTab, "")
        self.withdrawalsTab = QtWidgets.QWidget()
        self.withdrawalsTabLayout = QtWidgets.QGridLayout(self.withdrawalsTab)
        self.withdrawalsTabLayout.setObjectName("withdrawalsTabLayout")
        self.withdrawalsTab.setObjectName("withdrawalsTab")

        self.withdrawalsModel = PyQt5.QtSql.QSqlRelationalTableModel()
        self.withdrawalsModel.setJoinMode(PyQt5.QtSql.QSqlRelationalTableModel.JoinMode(1))
        self.withdrawalsModel.setTable("withdrawals")
        self.withdrawalsModel.setRelation(1, PyQt5.QtSql.QSqlRelation("books", "barcode", "barcode, title"))
        # In SQLITE booleans are stored as integers, false = 0 and true = 1
        self.withdrawalsModel.setFilter("is_returned = 0")
        self.withdrawalsModel.setEditStrategy(PyQt5.QtSql.QSqlTableModel.OnFieldChange)
        self.withdrawalsModel.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.withdrawalsModel.setHeaderData(1, QtCore.Qt.Horizontal, "Codigo")
        self.withdrawalsModel.setHeaderData(2, QtCore.Qt.Horizontal, "Titulo")
        self.withdrawalsModel.setHeaderData(3, QtCore.Qt.Horizontal, "Nome Aluno")
        self.withdrawalsModel.setHeaderData(4, QtCore.Qt.Horizontal, "Serie")
        self.withdrawalsModel.setHeaderData(5, QtCore.Qt.Horizontal, "Data Retirada")
        self.withdrawalsModel.setHeaderData(6, QtCore.Qt.Horizontal, "Devolvido")
        self.withdrawalsModel.setHeaderData(7, QtCore.Qt.Horizontal, "Data Dev")
        self.withdrawalsModel.select()

        self.withdrawalsView = PyQt5.QtWidgets.QTableView(self.withdrawalsTab)
        self.withdrawalsView.setObjectName("withdrawalsView")
        self.withdrawalsView.setMinimumSize(500, 300)
        sizePolicy.setHeightForWidth(self.withdrawalsView.sizePolicy().hasHeightForWidth())
        self.withdrawalsView.setModel(self.withdrawalsModel)
        self.withdrawalsView.setColumnHidden(0, True)
        self.withdrawalsView.setColumnHidden(6, True)
        self.withdrawalsView.setColumnHidden(7, True)
        self.withdrawalsView.resizeColumnsToContents()
        self.withdrawalsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.withdrawalsView.setSortingEnabled(True)
        self.withdrawalsTabLayout.addWidget(self.withdrawalsView, 2, 0, 0, 1)

        # Withdrawals Form

        self.withdrawalsSearchFrame = QtWidgets.QFrame(self.withdrawalsTab)
        self.withdrawalsSearchFrame.setGeometry(QtCore.QRect(10, 10, 241, 241))
        self.withdrawalsSearchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.withdrawalsSearchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.withdrawalsSearchFrame.setObjectName("withdrawalsSearchFrame")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.withdrawalsSearchFrame)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 221, 221))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.withdrawlsSearchFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.withdrawlsSearchFormLayout.setContentsMargins(0, 0, 0, 0)
        self.withdrawlsSearchFormLayout.setObjectName("withdrawlsSearchFormLayout")
        self.withdrawalsSearchLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.withdrawalsSearchLabel.setStyleSheet("font-size:16px;\n"
"")
        self.withdrawalsSearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.withdrawalsSearchLabel.setObjectName("withdrawalsSearchLabel")
        self.withdrawlsSearchFormLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.withdrawalsSearchLabel)
        self.withdrawalsSearchBarcodeLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.withdrawalsSearchBarcodeLabel.setStyleSheet("font-size:16px")
        self.withdrawalsSearchBarcodeLabel.setObjectName("withdrawalsSearchBarcodeLabel")
        self.withdrawlsSearchFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.withdrawalsSearchBarcodeLabel)
        self.withdrawalsSearchBarcodeInput = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.withdrawalsSearchBarcodeInput.setObjectName("withdrawalsSearchBarcodeInput")
        self.withdrawlsSearchFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.withdrawalsSearchBarcodeInput)
        self.withdrawalsSearchTitleLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.withdrawalsSearchTitleLabel.setStyleSheet("font-size:16px")
        self.withdrawalsSearchTitleLabel.setObjectName("withdrawalsSearchTitleLabel")
        self.withdrawlsSearchFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.withdrawalsSearchTitleLabel)
        self.withdrawalsSearchTitleInput = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.withdrawalsSearchTitleInput.setObjectName("withdrawalsSearchTitleInput")
        self.withdrawlsSearchFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.withdrawalsSearchTitleInput)
        self.withdrawalsSearchStudentLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.withdrawalsSearchStudentLabel.setStyleSheet("font-size:16px")
        self.withdrawalsSearchStudentLabel.setObjectName("withdrawalsSearchStudentLabel")
        self.withdrawlsSearchFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.withdrawalsSearchStudentLabel)
        self.withdrawalsSearchStudentInput = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.withdrawalsSearchStudentInput.setObjectName("withdrawalsSearchStudentInput")
        self.withdrawlsSearchFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.withdrawalsSearchStudentInput)
        self.withdrawalsSearchGradeInput = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.withdrawalsSearchGradeInput.setObjectName("withdrawalsSearchGradeInput")
        self.withdrawlsSearchFormLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.withdrawalsSearchGradeInput)
        self.withdrawalsSearchGradeLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.withdrawalsSearchGradeLabel.setStyleSheet("font-size:16px")
        self.withdrawalsSearchGradeLabel.setObjectName("withdrawalsSearchGradeLabel")
        self.withdrawlsSearchFormLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.withdrawalsSearchGradeLabel)
        self.withdrawalsButton = QtWidgets.QPushButton(self.withdrawalsTab)
        self.withdrawalsButton.setGeometry(QtCore.QRect(280, 110, 88, 34))
        self.withdrawalsButton.setObjectName("withdrawalsButton")
        self.tabWidget.addTab(self.withdrawalsTab, "")

        # RETURNS TAB

        self.returnsTab = QtWidgets.QWidget()
        self.returnsTab.setObjectName("returnsTab")
        self.returnsTabLayout = QtWidgets.QGridLayout(self.returnsTab)
        self.returnsTabLayout.setObjectName("returnsTabLayout")
        # Returns Table

        self.returnsModel = PyQt5.QtSql.QSqlRelationalTableModel()
        self.returnsModel.setJoinMode(PyQt5.QtSql.QSqlRelationalTableModel.JoinMode(1))
        self.returnsModel.setTable("withdrawals")
        self.returnsModel.setRelation(1, PyQt5.QtSql.QSqlRelation("books", "barcode", "barcode, title"))
        # In SQLITE booleans are stored as integers, false = 0 and true = 1
        self.returnsModel.setFilter("is_returned = 1")
        self.returnsModel.setEditStrategy(PyQt5.QtSql.QSqlTableModel.OnFieldChange)
        self.returnsModel.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.returnsModel.setHeaderData(1, QtCore.Qt.Horizontal, "Codigo")
        self.returnsModel.setHeaderData(2, QtCore.Qt.Horizontal, "Titulo")
        self.returnsModel.setHeaderData(3, QtCore.Qt.Horizontal, "Nome Aluno")
        self.returnsModel.setHeaderData(4, QtCore.Qt.Horizontal, "Serie")
        self.returnsModel.setHeaderData(5, QtCore.Qt.Horizontal, "Data Retirada")
        self.returnsModel.setHeaderData(6, QtCore.Qt.Horizontal, "Devolvido")
        self.returnsModel.setHeaderData(7, QtCore.Qt.Horizontal, "Data Devolvido")
        self.returnsModel.select()

        self.returnsView = PyQt5.QtWidgets.QTableView(self.withdrawalsTab)
        self.returnsView.setObjectName("returnsView")
        self.returnsView.setMinimumSize(500, 300)
        sizePolicy.setHeightForWidth(self.returnsView.sizePolicy().hasHeightForWidth())
        self.returnsView.setModel(self.returnsModel)
        self.returnsView.setColumnHidden(0, True)
        self.returnsView.setColumnHidden(6, True)
        self.returnsView.resizeColumnsToContents()
        self.returnsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.returnsView.setSortingEnabled(True)
        self.withdrawalsTabLayout.addWidget(self.returnsView, 2, 0, 0, 1)

        self.tabWidget.addTab(self.returnsView, "Devoluções")

        # END
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.retranslateUi(MainWidget)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Biblioteca"))

        self.booksSearchLabel.setText(_translate("MainWidget", "Livro"))
        self.booksSearchBarcodeLabel.setText(_translate("MainWidget", "Codigo"))
        self.booksSearchTitleLabel.setText(_translate("MainWidget", "Titulo"))
        self.booksSearchAuthorLabel.setText(_translate("MainWidget", "Autor"))
        self.booksAmountLabel.setText(_translate("MainWidget", "Quantidade"))
        self.booksAmountButton.setText(_translate("MainWidget", "Adicionar"))
        self.booksWithdrawalStudentLabel.setText(_translate("MainWidget", "Aluno"))
        self.booksWithdrawalGradeLabel.setText(_translate("MainWidget", "Serie"))
        self.booksWithdrawalButton.setText(_translate("MainWidget", "Retirar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booksTab), _translate("MainWidget", "Livros"))

        self.withdrawalsSearchLabel.setText(_translate("MainWidget", "Dados Retirada"))
        self.withdrawalsSearchBarcodeLabel.setText(_translate("MainWidget", "Codigo"))
        self.withdrawalsSearchTitleLabel.setText(_translate("MainWidget", "Titulo"))
        self.withdrawalsSearchStudentLabel.setText(_translate("MainWidget", "Aluno"))
        self.withdrawalsSearchGradeLabel.setText(_translate("MainWidget", "Serie"))
        self.withdrawalsButton.setText(_translate("MainWidget", "Devolver"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.withdrawalsTab), _translate("MainWidget", "Retiradas"))

    def resetBooksInputs(self):
        self.booksSearchAuthorInput.setText("")
        self.booksSearchTitleInput.setText("")
        self.booksSearchBarcodeInput.setText("")
        self.booksAmountInput.setText("")
        self.booksWithdrawalStudentInput.setText("")
        self.booksWithdrawalGradeInput.setText("")

    def insertBook(self):
        barcode = self.booksSearchBarcodeInput.text()
        title = self.booksSearchTitleInput.text()
        author = self.booksSearchAuthorInput.text()
        amount = int(self.booksAmountInput.text())
        database_interface.insertBook(barcode, title, author, amount)
        self.booksModel.select()

    def handleBarcodeInputEnter(self):
        barcode = self.booksSearchBarcodeInput.text()
        matches = self.booksModel.match(self.booksModel.index(0, 0), PyQt5.QtCore.Qt.DisplayRole, barcode)
        if len(matches) > 0:
            foundItemIndex = matches[0]
            self.booksView.selectRow(foundItemIndex.row())
        else:
            pass

    def handleBookSelectionChange(self):
        selected = self.booksView.selectionModel().selectedRows()
        row = selected[0].row()
        barcode = selected[0].sibling(row, 0).data()
        title = selected[0].sibling(row, 1).data()
        author = selected[0].sibling(row, 2).data()
        self.booksSearchBarcodeInput.setText(barcode)
        self.booksSearchTitleInput.setText(title)
        self.booksSearchAuthorInput.setText(author)

    def withdrawBook(self):
        barcode = self.booksSearchBarcodeInput.text()
        title = self.booksSearchTitleInput.text()
        author = self.booksSearchAuthorInput.text()
        student_name = self.booksWithdrawalStudentInput.text()
        student_grade = self.booksWithdrawalGradeInput.text()
        database_interface.addOneBorrowedBook(barcode, title, author)
        database_interface.addWithdrawalEntry(barcode, student_name, student_grade)
        self.booksModel.select()
        self.withdrawalsModel.select()
        self.resetBooksInputs()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    if not connection.open():
        PyQt5.QtWidgets.QMessageBox.critical(None, "DATABASE ERROR: %s" % connection.lastError().databaseText())
        sys.exit(1)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    ui.setupUi(MainWidget)
    MainWidget.show()
    sys.exit(app.exec_())


# foundBook = self.booksModel.match(self.booksModel.index(column=0), role=0, value=barcode)
        # print('hello2')
        # if len(foundBook) > 0:
        #     print(foundBook)
        #     # print(self.booksModel.data(foundBook[0]))
        #     # self.booksModel.setData(foundBook[0])
        # else:
        #     newRecord = self.booksModel.record()
        #     newRecord.setValue("barcode", barcode)
        #     newRecord.setValue("title", title)
        #     newRecord.setValue("author", author)
        #     newRecord.setValue("amount_available", int(amount))
        #     if self.booksModel.insertRecord(-1, newRecord):
        #         self.resetBooksInputs()
        #     else:
        #         PyQt5.QtWidgets.QMessageBox.critical(None, "DATABASE ERROR: %s" % connection.lastError().databaseText())
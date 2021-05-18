# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Biblioteca.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import interface


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
        self.booksTableWidget = QtWidgets.QTableWidget(self.booksTab)
        self.booksTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # self.booksTableWidget.setGeometry(QtCore.QRect(6, 254, 851, 371))
        self.booksTableWidget.setMinimumSize(QtCore.QSize(500, 300))
        self.booksTableWidget.setObjectName("booksTableWidget")
        self.booksTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.booksTableWidget.setColumnCount(5)
        self.booksTableWidget.setRowCount(0)
        sizePolicy.setHeightForWidth(self.booksTableWidget.sizePolicy().hasHeightForWidth())
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(0, item)
        self.booksTableWidget.setColumnWidth(0, 250)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(1, item)
        self.booksTableWidget.setColumnWidth(1, 250)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(2, item)
        self.booksTableWidget.setColumnWidth(2, 250)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(3, item)
        self.booksTableWidget.setColumnWidth(3, 100)
        item = QtWidgets.QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(4, item)
        self.booksTableWidget.setColumnWidth(4, 100)
        self.booksTabLayout.addWidget(self.booksTableWidget, 2, 0, 0, 1)

        #Books search form

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
        self.booksWithdrawalFormLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.booksWithdrawalButton)

        # WITHDRAWALS TAB

        self.tabWidget.addTab(self.booksTab, "")
        self.withdrawalsTab = QtWidgets.QWidget()
        self.withdrawalsTabLayout = QtWidgets.QGridLayout(self.withdrawalsTab)
        self.booksTabLayout.setObjectName("withdrawalsTabLayout")
        self.withdrawalsTab.setObjectName("withdrawalsTab")
        self.withdrawalsTable = QtWidgets.QTableWidget(self.withdrawalsTab)
        self.withdrawalsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.withdrawalsTable.setGeometry(QtCore.QRect(10, 260, 851, 361))
        self.withdrawalsTable.setObjectName("withdrawalsTable")
        self.withdrawalsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.withdrawalsTable.setColumnCount(5)
        self.withdrawalsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.withdrawalsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.withdrawalsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.withdrawalsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.withdrawalsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.withdrawalsTable.setHorizontalHeaderItem(4, item)
        sizePolicy.setHeightForWidth(self.withdrawalsTable.sizePolicy().hasHeightForWidth())
        self.withdrawalsTable.setMinimumSize(QtCore.QSize(500, 300))
        self.withdrawalsTabLayout.addWidget(self.withdrawalsTable, 2, 0, 0, 1)
        self.withdrawalsTable.itemSelectionChanged.connect(self.handleWithdrawalSelectionChange)

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
        self.withdrawalsButton.pressed.connect(self.returnBook)
        self.tabWidget.addTab(self.withdrawalsTab, "")

        # RETURNS TAB

        self.returnsTab = QtWidgets.QWidget()
        self.returnsTab.setObjectName("returnsTab")
        self.returnsTabLayout = QtWidgets.QGridLayout(self.returnsTab)
        self.returnsTabLayout.setObjectName("returnsTabLayout")
        # Returns Table Widget
        self.returnsTable = QtWidgets.QTableWidget(self.returnsTab)
        self.returnsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.returnsTable.setObjectName("returnsTable")
        self.returnsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.returnsTable.setColumnCount(6)
        self.returnsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.returnsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.returnsTable.setHorizontalHeaderItem(5, item)
        sizePolicy.setHeightForWidth(self.returnsTable.sizePolicy().hasHeightForWidth())
        self.returnsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.returnsTable.setMinimumSize(QtCore.QSize(500, 300))
        self.returnsTabLayout.addWidget(self.returnsTable)
        self.tabWidget.addTab(self.returnsTab, "Devoluções")

        # END
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.booksTableWidget.itemSelectionChanged.connect(self.handleBookSelectionChange)
        self.retranslateUi(MainWidget)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Biblioteca"))
        item = self.booksTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWidget", "Codigo"))
        item = self.booksTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWidget", "Titulo"))
        item = self.booksTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWidget", "Autor"))
        item = self.booksTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWidget", "Disponivel"))
        item = self.booksTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWidget", "Retirados"))
        self.booksSearchLabel.setText(_translate("MainWidget", "Livro"))
        self.booksSearchBarcodeLabel.setText(_translate("MainWidget", "Codigo"))
        self.booksSearchTitleLabel.setText(_translate("MainWidget", "Titulo"))
        self.booksSearchAuthorLabel.setText(_translate("MainWidget", "Autor"))
        self.booksAmountLabel.setText(_translate("MainWidget", "Quantidade"))
        self.booksAmountButton.setText(_translate("MainWidget", "Adicionar"))
        self.booksAmountButton.clicked.connect(self.handleAddBookAmountForm)
        self.booksWithdrawalStudentLabel.setText(_translate("MainWidget", "Aluno"))
        self.booksWithdrawalGradeLabel.setText(_translate("MainWidget", "Serie"))
        self.booksWithdrawalButton.setText(_translate("MainWidget", "Retirar"))
        self.booksWithdrawalButton.clicked.connect(self.handleWithdrawBookForm)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booksTab), _translate("MainWidget", "Livros"))
        item = self.withdrawalsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWidget", "Codigo"))
        item = self.withdrawalsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWidget", "Titulo"))
        item = self.withdrawalsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWidget", "Aluno"))
        item = self.withdrawalsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWidget", "Serie"))
        item = self.withdrawalsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWidget", "Data Retirada"))
        self.withdrawalsSearchLabel.setText(_translate("MainWidget", "Dados Retirada"))
        self.withdrawalsSearchBarcodeLabel.setText(_translate("MainWidget", "Codigo"))
        self.withdrawalsSearchTitleLabel.setText(_translate("MainWidget", "Titulo"))
        self.withdrawalsSearchStudentLabel.setText(_translate("MainWidget", "Aluno"))
        self.withdrawalsSearchGradeLabel.setText(_translate("MainWidget", "Serie"))
        self.withdrawalsButton.setText(_translate("MainWidget", "Devolver"))
        item = self.returnsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWidget", "Codigo"))
        item = self.returnsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWidget", "Titulo"))
        item = self.returnsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWidget", "Aluno"))
        item = self.returnsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWidget", "Serie"))
        item = self.returnsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWidget", "Data Retirada"))
        item = self.returnsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWidget", "Devolvido"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.withdrawalsTab), _translate("MainWidget", "Retiradas"))

    def loadBooksData(self):
        book_list = interface.select_all_books()
        self.booksTableWidget.setRowCount(len(book_list))
        for index, book in enumerate(book_list):
            self.booksTableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(book.barcode))
            self.booksTableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(book.title))
            self.booksTableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(book.author))
            self.booksTableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(book.amount_available)))
            self.booksTableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(str(book.amount_borrowed)))

    def loadWithdrawalData(self):
        withdrawal_list = interface.select_all_withdrawals()
        self.withdrawalsTable.setRowCount((len(withdrawal_list)))
        for index, withdrawal in enumerate(withdrawal_list):
            self.withdrawalsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(withdrawal.book.barcode))
            self.withdrawalsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(withdrawal.book.title))
            self.withdrawalsTable.setItem(index, 2, QtWidgets.QTableWidgetItem(withdrawal.student_name))
            self.withdrawalsTable.setItem(index, 3, QtWidgets.QTableWidgetItem(withdrawal.student_grade))
            self.withdrawalsTable.setItem(index, 4, QtWidgets.QTableWidgetItem(withdrawal.withdrawal_date.strftime("%d/%m/%Y")))


    def loadReturnsData(self):
        returns_list = interface.select_all_returns()
        self.returnsTable.setRowCount((len(returns_list)))
        for index, withdrawal in enumerate(returns_list):
            self.returnsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(withdrawal.book.barcode))
            self.returnsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(withdrawal.book.title))
            self.returnsTable.setItem(index, 2, QtWidgets.QTableWidgetItem(withdrawal.student_name))
            self.returnsTable.setItem(index, 3, QtWidgets.QTableWidgetItem(withdrawal.student_grade))
            self.returnsTable.setItem(index, 4, QtWidgets.QTableWidgetItem(withdrawal.withdrawal_date.strftime("%d/%m/%Y")))
            self.returnsTable.setItem(index, 5, QtWidgets.QTableWidgetItem(withdrawal.return_date.strftime("%d/%m/%Y")))



    def handleWithdrawBookForm(self):
        barcode = self.booksSearchBarcodeInput.text()
        student_name = self.booksWithdrawalStudentInput.text()
        student_grade = self.booksWithdrawalGradeInput.text()
        interface.withdraw_book(barcode, student_name, student_grade)
        self.loadWithdrawalData()
        self.loadBooksData()

    def handleAddBookAmountForm(self):
        barcode = self.booksSearchBarcodeInput.text()
        title = self.booksSearchTitleInput.text()
        author = self.booksSearchAuthorInput.text()
        amount = self.booksAmountInput.text()
        interface.insert_one_book(barcode, title, author, int(amount))
        self.loadBooksData()

    def handleBookSelectionChange(self):
        items = self.booksTableWidget.selectedItems()
        rows_selected = len(items) // self.booksTableWidget.columnCount()
        if rows_selected == 1:
            self.booksSearchBarcodeInput.setText(items[0].text())
            self.booksSearchTitleInput.setText(items[1].text())
            self.booksSearchAuthorInput.setText(items[2].text())

    def handleBarcodeInputEnter(self):
        for rowIndex in range(self.booksTableWidget.rowCount()):
            if self.booksTableWidget.item(rowIndex, 0).text() == self.booksSearchBarcodeInput.text():
                self.booksTableWidget.selectRow(rowIndex)

    def handleWithdrawalSelectionChange(self):
        items = self.withdrawalsTable.selectedItems()
        rows_selected = len(items) // self.booksTableWidget.columnCount()
        if rows_selected == 1:
            self.withdrawalsSearchBarcodeInput.setText(items[0].text())
            self.withdrawalsSearchTitleInput.setText(items[1].text())
            self.withdrawalsSearchStudentInput.setText(items[2].text())
            self.withdrawalsSearchGradeInput.setText(items[3].text())

    def returnBook(self):
        barcode = self.withdrawalsSearchBarcodeInput.text()
        student_name = self.withdrawalsSearchStudentInput.text()
        interface.return_book(barcode, student_name)
        self.loadWithdrawalData()
        self.loadReturnsData()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWidget = QtWidgets.QWidget()
    ui = Ui_MainWidget()
    interface.initialize_db()
    ui.setupUi(MainWidget)
    ui.loadBooksData()
    ui.loadWithdrawalData()
    ui.loadReturnsData()
    MainWidget.show()
    sys.exit(app.exec_())

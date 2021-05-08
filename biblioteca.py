# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Biblioteca.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 729)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(651, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.booksTab = QtWidgets.QWidget()
        self.booksTab.setObjectName("booksTab")
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
        self.booksTableView = QtWidgets.QTableView(self.booksTab)
        self.booksTableView.setGeometry(QtCore.QRect(10, 260, 901, 411))
        self.booksTableView.setObjectName("booksTableView")
        self.tabWidget.addTab(self.booksTab, "")
        self.withdrawalsTab = QtWidgets.QWidget()
        self.withdrawalsTab.setObjectName("withdrawalsTab")
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
        self.withdrawalsSearchAuthorLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.withdrawalsSearchAuthorLabel.setStyleSheet("font-size:16px")
        self.withdrawalsSearchAuthorLabel.setObjectName("withdrawalsSearchAuthorLabel")
        self.withdrawlsSearchFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.withdrawalsSearchAuthorLabel)
        self.withdrawalsSearchAuthorInput = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.withdrawalsSearchAuthorInput.setObjectName("withdrawalsSearchAuthorInput")
        self.withdrawlsSearchFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.withdrawalsSearchAuthorInput)
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
        self.withdrawalsTableView = QtWidgets.QTableView(self.withdrawalsTab)
        self.withdrawalsTableView.setGeometry(QtCore.QRect(10, 260, 901, 411))
        self.withdrawalsTableView.setObjectName("withdrawalsTableView")
        self.tabWidget.addTab(self.withdrawalsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.booksSearchLabel.setText(_translate("MainWindow", "Pesquisar"))
        self.booksSearchBarcodeLabel.setText(_translate("MainWindow", "Codigo"))
        self.booksSearchTitleLabel.setText(_translate("MainWindow", "Titulo"))
        self.booksSearchAuthorLabel.setText(_translate("MainWindow", "Autor"))
        self.booksAmountLabel.setText(_translate("MainWindow", "Quantidade"))
        self.booksAmountButton.setText(_translate("MainWindow", "Adicionar"))
        self.booksWithdrawalStudentLabel.setText(_translate("MainWindow", "Aluno"))
        self.booksWithdrawalGradeLabel.setText(_translate("MainWindow", "Serie"))
        self.booksWithdrawalButton.setText(_translate("MainWindow", "Retirar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booksTab), _translate("MainWindow", "Livros"))
        self.withdrawalsSearchLabel.setText(_translate("MainWindow", "Pesquisar"))
        self.withdrawalsSearchBarcodeLabel.setText(_translate("MainWindow", "Codigo"))
        self.withdrawalsSearchTitleLabel.setText(_translate("MainWindow", "Titulo"))
        self.withdrawalsSearchAuthorLabel.setText(_translate("MainWindow", "Autor"))
        self.withdrawalsSearchStudentLabel.setText(_translate("MainWindow", "Aluno"))
        self.withdrawalsSearchGradeLabel.setText(_translate("MainWindow", "Serie"))
        self.withdrawalsButton.setText(_translate("MainWindow", "Devolver"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.withdrawalsTab), _translate("MainWindow", "Retiradas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
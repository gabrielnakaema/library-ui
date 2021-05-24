from PyQt5.QtWidgets import QLineEdit


class FocusQLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(FocusQLineEdit, self).__init__(parent)

    def mousePressEvent(self, e):
        self.selectAll()

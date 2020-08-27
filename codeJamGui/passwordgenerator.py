# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QAction, QFormLayout, QLineEdit, QSpinBox, QWidget


class PasswordGenerator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.createNewPasswordField = QFormLayout()

        self.setWindowTitle("Password Generator")
        self.setFixedSize(400,500)
        self.statusBar()
        self.menu = self.menuBar()
        self.spinBox = QSpinBox()
        self.passwordLengthInputLabel = QLabel(self.tr("Password Length:"))

        self.createNewPasswordField.addRow(self.passwordLengthInputLabel,self.spinBox)

        self.centralWidget.setLayout(self.createNewPasswordField)
        #add actions below
        self.viewPasswords = QAction("View Passwords",self)
        self.addPassword = QAction("Add Password",self)
        self.deletePassword = QAction("Delete Password",self)
        self.deleteAllPasswords = QAction("Delete All Passwords",self)
        self.createNewPassword = QAction("Create New Password",self)
        self.passMenu = QMenu("Add/Delete Passwords",self)
        #set menu below
        self.passMenu.addAction(self.addPassword)
        self.passMenu.addAction(self.deletePassword)
        self.passMenu.addAction(self.deleteAllPasswords)
        self.passMenu.addAction(self.createNewPassword)
        self.file = self.menu.addMenu("&File")
        self.file.addAction(self.viewPasswords)
        self.passMenu = self.file.addMenu(self.passMenu)

if __name__ == "__main__":
    app = QApplication([])
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())

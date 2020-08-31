#Copyright (C) 2020 author name here
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

# This Python file uses the following encoding: utf-8
# var = 4 used so program still compiles while functions incomplete
# Add function to enter old passwords
# Use length to reccommend to change old passwords
# Create function to edit update passwords
import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QAction, QFormLayout, QLineEdit, QSpinBox, QWidget, QDialog, QVBoxLayout, QDialogButtonBox, QPlainTextEdit
import hashlib
import pyjamGen as gen
import decode as d

masterPass = ""
vaultAuth = False
newLine = 0

class CreatePassDialog(QDialog):
    def __init__(self,*args,**kwargs):
        super(CreatePassDialog,self).__init__(*args,**kwargs)

        self.label = QLabel("Create a master password to access all of your passwords:",self)
        self.enterLine = QLineEdit(self)
        self.dialog = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog.accepted.connect(self.applyPass)
        self.dialog.rejected.connect(CreatePassDialog.exit)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.enterLine)
        self.layout.addWidget(self.dialog)
        self.setLayout(self.layout)

    def applyPass(self):
        global masterPass
        password = self.enterLine.text()
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        masterPass = password
        self.close()

    def exit():
        sys.exit()

class AccessVaultDialog(QDialog):
    def __init__(self,*args,**kwargs):
        super(AccessVaultDialog,self).__init__(*args,**kwargs)

        self.label = QLabel("Enter your master password to unlock your password vault:",self)
        self.enterLine = QLineEdit(self)
        self.dialog = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog.accepted.connect(self.verifyPassword)
        self.dialog.rejected.connect(self.close)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.enterLine)
        self.layout.addWidget(self.dialog)
        self.setLayout(self.layout)

    def verifyPassword(self):
        global masterPass
        masterPass = masterPass.rstrip("\n")
        global vaultAuth
        comp = (hashlib.sha256(self.enterLine.text().encode('utf-8'))).hexdigest()

        if masterPass == comp:
            vaultAuth = True

        self.close()

class DeletePassDialog(QDialog):
    def __init__(self,saveFile,*args,**kwargs):
        super(DeletePassDialog,self).__init__(*args,**kwargs)

        self.saveFile = saveFile
        self.label = QLabel("Enter the account name of the password you want to remove:",self)
        self.enterLine = QLineEdit(self)
        self.dialog = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog.accepted.connect(self.selectAccToDelete)
        self.dialog.rejected.connect(self.close)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.enterLine)
        self.layout.addWidget(self.dialog)
        self.setLayout(self.layout)

    def selectAccToDelete(self):
        for i in range(0,self.saveFile.numberOfLines()):
            if self.saveFile[i][self.enterLine.text()]:
                self.done(i)
        self.done(-1)

class AddExistingPassDialog(QDialog):
    def __init__(self,saveFile,*args,**kwargs):
        super(AddExistingPassDialog,self).__init__(*args,**kwargs)

        self.saveFile = saveFile
        self.label = QLabel("Enter the account name of the password you want to add:",self)
        self.enterLine = QLineEdit(self)
        self.enterLine2 = QLineEdit(self)
        self.label2 = QLabel("Enter the password:")
        self.dialog = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.dialog.accepted.connect(self.addPass)
        self.dialog.rejected.connect(self.close)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.enterLine)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.enterLine2)
        self.layout.addWidget(self.dialog)
        self.setLayout(self.layout)

    def addPass(self):
        global newLine
        for i in self.saveFile:
            if i[self.enterLine.text()]:
                self.done(-1)
        newLine = SaveFileLine(self.enterLine.text(),d.encrypt(b'ACYDb3cNfYTuI0AuX6aUdScLNZfo_Vcowh47Q_uUMdM=',self.enterLine2.text()))
        self.close()

class SaveFileLine:
    def __init__(self,account,encryptedPassword): #class to store each line of the save file
        self.encryptedPassword = encryptedPassword
        self.account = account

    def __getitem__(self,index):
        if index == self.account:
            return True
        else:
            return False

    def __str__(self):
        return self.account + ',' + str(self.encryptedPassword) + "\n"

    def getAccountName(self):
        return self.account

    def decryptPassword(self):
        global vaultAuth
        if vaultAuth == False:
            sys.exit()
        return d.decrypt(b'ACYDb3cNfYTuI0AuX6aUdScLNZfo_Vcowh47Q_uUMdM=',self.encryptedPassword)

class SaveFile: #data type to store all of the lines
    def __init__(self,passwordHash,lines):
        self.passwordHash = passwordHash
        self.lines = lines

    def __getitem__(self,index):
        if index > len(self.lines):
            raise IndexError("Index out of range")
        return self.lines[index]

    def getPasswordHash(self):
        return self.passwordHash

    def getLines(self):
        return self.lines

    def append(self,line):
        self.lines.append(line)

    def setHashPass(self,hash):
        self.passwordHash = hash

    def __sub__(self,index):
        self.lines.pop(index)

    def numberOfLines(self):
        return len(self.lines)

class PasswordGenerator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()

        self.createNewPasswordField = QFormLayout()

        self.setWindowTitle("Password Generator")
        self.setFixedSize(400,500)
        self.statusBar()
        self.menu = self.menuBar()
        self.spinBox = QSpinBox()
        self.userLineEdit = QLineEdit()
        self.userLineLabel = QLabel(self.tr("Enter website password is for:"))
        self.spinBox.valueChanged.connect(self.generatePassword)
        self.passwordLengthInputLabel = QLabel(self.tr("Password Length:"))
        self.passwordField = QPlainTextEdit(self)

        self.createNewPasswordField.addRow(self.userLineLabel,self.userLineEdit)
        self.createNewPasswordField.addRow(self.passwordLengthInputLabel,self.spinBox)

        self.layout.addLayout(self.createNewPasswordField)
        self.layout.addWidget(self.passwordField)

        self.centralWidget.setLayout(self.layout)
        #add actions below
        self.viewPasswords = QAction("View Passwords",self)
        self.viewPasswords.triggered.connect(self.viewPass)
        self.addPassword = QAction("Add Password",self)
        self.addPassword.triggered.connect(self.addExistingPass)
        self.deletePassword = QAction("Delete Password",self)
        self.deletePassword.triggered.connect(self.deletePasswordFunc)
        self.deleteAllPasswords = QAction("Delete All Passwords",self)
        self.deleteAllPasswords.triggered.connect(self.deleteAllPasswordsFunc)
        self.passMenu = QMenu("Add/Delete Passwords",self)
        #set menu below
        self.passMenu.addAction(self.addPassword)
        self.passMenu.addAction(self.deletePassword)
        self.passMenu.addAction(self.deleteAllPasswords)
        self.file = self.menu.addMenu("&File")
        self.file.addAction(self.viewPasswords)
        self.passMenu = self.file.addMenu(self.passMenu)

        self.saveFile = SaveFile(0,[])
        self.account = ""
        self.encryptedPass = ""
        self.filename = "passwordSaveData.sav"

        self.readFileData()
        global masterPass
        masterPass = self.saveFile.getPasswordHash()
        self.authThisSession()

    def resetParameters(self):
        self.userLineEdit.clear()
        self.spinBox.setValue(0)
        self.passwordField.clear()

    def deletePasswordFunc(self,account):
        global vaultAuth
        if vaultAuth == False:
            sys.exit()

        deletePass = DeletePassDialog(self.saveFile)
        deletePass.setWindowTitle("Choose which password you want to remove!")
        accountIndex = deletePass.exec_()
        if isinstance(accountIndex,int):
            self.saveFile - accountIndex
        else:
            none = QDialog()
            none.setWindowTitle("Failed")
            none.setText("No account with that name!")
            none.exec_()

        for i in range(0,self.saveFile.numberOfLines()):
            if self.saveFile[i][account]:
                self.saveFile - i
        self.savePassToFile()
        self.resetParameters()
        self.viewPass()

    def viewPass(self):
        self.resetParameters()
        text = ""
        for i in self.saveFile:
            text += i.getAccountName() + ": " + str(i.decryptPassword())[2:-1] + "\n"
            print(text)
        self.passwordField.insertPlainText(text)

    def deleteAllPasswordsFunc(self):
        global vaultAuth
        global masterPass
        if vaultAuth == False:
            sys.exit()
        self.saveFile = SaveFile(masterPass,[])
        self.savePassToFile()
        self.resetParameters()
        self.viewPass()

    def addExistingPass(self):
        global newLine
        done = AddExistingPassDialog(self.saveFile)
        done.setWindowTitle("Add existing password!")
        answer = done.exec_()
        if answer == -1:
            done = QDialog()
            done.setWindowTitle("Account Already Exists!")
            done.exec_()
            return
        else:
            if newLine != 0:
                self.saveFile.append(newLine)
                self.savePassToFile()
                self.resetParameters()
                self.viewPass()

    def generatePassword(self):
        global vaultAuth

        if vaultAuth == False:
            sys.exit()

        if self.spinBox.value() < 1:
            return
        password = gen.gen_code(self.spinBox.value())
        self.account = self.userLineEdit.text()
        if self.account == "":
            return
        for i in self.saveFile:
            if i[self.account]:
                return
        self.encryptedPass = d.encrypt(b'ACYDb3cNfYTuI0AuX6aUdScLNZfo_Vcowh47Q_uUMdM=',password)
        self.saveFile.append(SaveFileLine(self.account,self.encryptedPass))
        self.savePassToFile()
        self.resetParameters()
        self.viewPass()
        for i in self.saveFile:
            print(str(i))
        
    def authThisSession(self):
        global vaultAuth
        if vaultAuth == False:
            enterMasterPass = AccessVaultDialog(self)
            enterMasterPass.setWindowTitle("Access your password vault!")
            enterMasterPass.exec_()

    def savePassToFile(self): #pass savefile object to save
        file = open(self.filename,'wt')
        hashPass = self.saveFile.getPasswordHash()

        file.write(hashPass + '\n')
        if self.saveFile.numberOfLines() > 0:
            for i in self.saveFile:
                line = str(i)
                file.write(line)
        file.close()

    def readFileData(self):
        fileExists = os.path.isfile(self.filename)

        if fileExists == False:
            createPassword = CreatePassDialog(self)
            createPassword.setWindowTitle("Create master password!")
            createPassword.exec_()
            self.saveFile.setHashPass(masterPass)
            self.savePassToFile()
            self.readFileData()

        file = open(self.filename,'r')
        lines = []

        for line in file:
            lines.append(line.rstrip("\n"))

        file.close()

        self.saveFile.setHashPass(lines[0])
        lines.pop(0)

        for line in lines:
            comma = self.findComma(line)
            if comma is None:
                return
            passcode = line[comma + 1:]
            passcode = passcode[2:-1]
            passcode = passcode.encode()
            saveFileLine = SaveFileLine(line[0:comma],passcode)
            self.saveFile.append(saveFileLine)

    def searchForPassword(accountName):
        for i in saveFile:
            if i[accountName]:
                return str(i)
        return "No Password Found"

    def findComma(c,line):
        for i in range(0,len(line)):
            if line[i] == ',':
                return i

if __name__ == "__main__":
    app = QApplication([])
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())

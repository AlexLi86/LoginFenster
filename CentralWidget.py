from PyQt6.QtWidgets import QWidget, QSlider, QLabel, QTextEdit, QVBoxLayout, QPushButton, QApplication, QTextBrowser, \
    QGridLayout, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.labelbenutzername = QLabel("Benutzername:", self)
        self.labelpasswort = QLabel("Passwort:", self)


        self.textpasswort = QLineEdit(self)
        self.textpasswort.setFixedWidth(150)
        self.textpasswort.setFixedHeight(30)
        self.textpasswort.setEchoMode(QLineEdit.EchoMode.Password)

        self.textbenutzername = QLineEdit(self)
        self.textbenutzername.setFixedWidth(150)
        self.textbenutzername.setFixedHeight(30)



        self.button = QPushButton("Login", self)
        self.button.clicked.connect(self.einlogen)
        self.button.setFixedWidth(150)
        self.button.setFixedHeight(30)

        self.buttonschliesen = QPushButton("Schließen", self)
        self.buttonschliesen.clicked.connect(QApplication.instance().quit)
        self.buttonschliesen.setFixedWidth(150)
        self.buttonschliesen.setFixedHeight(30)

        layout = QGridLayout(self)
        layout.addWidget(self.labelbenutzername, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.textbenutzername, 0, 1, 1, 2, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.labelpasswort, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.textpasswort, 1, 1, 1, 2, Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.button, 2, 1, 1, 1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.buttonschliesen, 2, 2, 1, 1, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)



    def einlogen (self):
        if self.textpasswort.text() == "asdf1234" and self.textbenutzername.text() == "Alex":
            QMessageBox.information(self, "Success", "Success")
        else:
            QMessageBox.information(self, "Passwort Falsch", "Passwort Falsch")











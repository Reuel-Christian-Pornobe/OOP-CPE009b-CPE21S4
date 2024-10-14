import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon

class RegistrationGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("Paw Patrol Registration")
        self.setGeometry(300, 300, 400, 300)
        self.setWindowIcon(QIcon('icon.ico')) # sets an icon
        

        self.program_title = QLabel("Paw Patrol Officer Registration: ", self)
        self.program_title.move(50, 20)
        self.setStyleSheet("QLabel{font-size: 10pt;}")

        self.first_name_label = QLabel("First Name:", self)
        self.first_name_label.move(50, 50)
        self.first_name_entry = QLineEdit(self)
        self.first_name_entry.move(150, 50)

        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_label.move(50, 80)
        self.last_name_entry = QLineEdit(self)
        self.last_name_entry.move(150, 80)

        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 110)
        self.username_entry = QLineEdit(self)
        self.username_entry.move(150, 110)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 140)
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.move(150, 140)

        self.email_label = QLabel("Email Address:", self)
        self.email_label.move(50, 170)
        self.email_entry = QLineEdit(self)
        self.email_entry.move(150, 170)

        self.contact_number_label = QLabel("Contact Number:", self)
        self.contact_number_label.move(50, 200)
        self.contact_number_entry = QLineEdit(self)
        self.contact_number_entry.move(150, 200)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(50, 230)
        self.submit_button.clicked.connect(self.submit)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.move(250, 230)
        self.clear_button.clicked.connect(self.clear)

    def submit(self):
        print("Submit button clicked")

    def clear(self):
        self.first_name_entry.clear()
        self.last_name_entry.clear()
        self.username_entry.clear()
        self.password_entry.clear()
        self.email_entry.clear()
        self.contact_number_entry.clear()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_gui = RegistrationGUI()
    registration_gui.show()
    sys.exit(app.exec_())
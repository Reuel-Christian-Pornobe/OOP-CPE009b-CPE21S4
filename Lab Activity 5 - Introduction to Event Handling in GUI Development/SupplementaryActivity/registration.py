import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from csv import writer

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
        self.submit_button.clicked.connect(self.on_click)

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
        
        
    @pyqtSlot()
    def on_click(self):
        submit_button = QMessageBox.question(self, "Testing Response", "Confirm your Submission",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        
        
        if not self.first_name_entry.text() or not self.last_name_entry.text() or not self.username_entry.text() or not self.password_entry.text() or not self.email_entry.text() or not self.contact_number_entry.text():
            QMessageBox.warning(self, "Evaluation", "Please fill all the blanks!", QMessageBox.Ok, QMessageBox.Ok)
            return
        
        elif submit_button == QMessageBox.Yes:
            QMessageBox.warning(self, "Evaluation", "Account Saved to DataBase", QMessageBox.Ok, QMessageBox.Ok)

            # Define the data to be written to the CSV file
            data = [[self.first_name_entry.text(),  self.last_name_entry.text(), self.username_entry.text(), 
                         self.password_entry.text(), self.email_entry.text(), self.contact_number_entry.text()]]
  
            # Specify the file name
            filename = 'dataBase.csv'
 
            # Write data to the CSV file with a pipe delimiter
            with open(filename, 'a', newline='') as csvfile:
                csvwriter = writer(csvfile, delimiter='|')
                csvwriter.writerows(data)
                filename.close()
                    
            
        else:
            QMessageBox.information(self, "Evaluation", "Account Not Saved to DataBase", QMessageBox.Ok, QMessageBox.Ok)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_gui = RegistrationGUI()
    registration_gui.show()
    sys.exit(app.exec_())
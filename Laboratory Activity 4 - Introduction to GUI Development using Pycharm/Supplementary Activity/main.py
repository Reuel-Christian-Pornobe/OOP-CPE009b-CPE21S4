import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from registration import RegistrationGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_gui = RegistrationGUI()
    registration_gui.show()
    sys.exit(app.exec_())
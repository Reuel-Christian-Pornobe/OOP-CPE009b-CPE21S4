"""
@author: Pornobe, Reuel Christian, M.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.x = 200
        self.y = 200
        self.width = 300 
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        self.createGridLayout()
        self.setLayout(self.layout)
        
        self.show()
    
    def createGridLayout(self):
        
        self.layout = QGridLayout()
        
        self.layout.setColumnStretch(1,2)
        
        
        self.textboxlbl = QLabel("Enter your full name: ", self) # Label
        self.textboxlbl.setStyleSheet("QLabel{color: red}")
        
        self.textbox = QLineEdit(self) # textbox
    
        self.display = QLineEdit(self) # display
        
        self.button = QPushButton('Click to Display your full name', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.setStyleSheet("QPushButton{color: red}")
        self.button.clicked.connect(self.on_click)
        
        
        self.layout.addWidget(self.textboxlbl,0,1)
        self.layout.addWidget(self.textbox, 0,2)
       
        self.layout.addWidget(self.display, 1, 2)
        self.layout.addWidget(self.button, 1, 1)         

        
    @pyqtSlot()
    def on_click(self):
        self.display = QLineEdit(self.textbox.text(), self)
        self.layout.addWidget(self.display, 1, 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
































































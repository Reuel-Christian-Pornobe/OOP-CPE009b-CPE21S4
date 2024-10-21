import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    
    def __init__(self):
        super().__init__() # initializes the main window like in the previous one
        # window = QMainWindow()
        
        self.title = "PyQt Button"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        # In GUI Python, these button, textboxes, labels are called Widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100,70) # button.move(x,y)
        self.button.clicked.connect(self.on_click)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        buttonReply = QMessageBox.question(self, "Testing Response", "Do you like PyQt5?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            QMessageBox.warning(self, "Evaluation", "User Clicked Yes", QMessageBox.Ok, QMessageBox.Ok)
            
        else:
            QMessageBox.information(self, "Evaluation", "User Clicked No", QMessageBox.Ok, QMessageBox.Ok)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


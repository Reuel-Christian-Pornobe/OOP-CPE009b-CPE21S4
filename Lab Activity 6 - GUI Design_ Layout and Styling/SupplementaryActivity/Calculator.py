import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QMenu, QAction, QMenuBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paw Patrol Calculator")
        self.setWindowIcon(QIcon('icon.ico'))
        self.initUI()

    def initUI(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        grid = QGridLayout()
        row = 1
        col = 0
        for button in buttons:
            button_widget = QPushButton(button)
            button_widget.clicked.connect(lambda checked, b=button: self.button_clicked(b))
            grid.addWidget(button_widget, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        func_buttons = [
            'sin', 'cos', 'exp', 'C'
        ]

        func_grid = QGridLayout()
        func_row = 1
        func_col = 0
        for func_button in func_buttons:
            func_button_widget = QPushButton(func_button)
            func_button_widget.clicked.connect(lambda checked, b=func_button: self.func_button_clicked(b))
            func_grid.addWidget(func_button_widget, func_row, func_col)
            func_col += 1


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid)
        main_layout.addLayout(func_grid)

        self.setLayout(main_layout)

        # Create menu bar
        menubar = QMenuBar(self)
        fileMenu = QMenu("&File", self)
        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        menubar.addMenu(fileMenu)

        self.layout().setMenuBar(menubar)

    def button_clicked(self, button):
        if button == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
                self.store_operation(self.display.text(), result)
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + button)

    def func_button_clicked(self, button):
        if button == 'sin':
            try:
                result = str(math.sin(float(self.display.text())))
                self.display.setText(result)
                self.store_operation("sin(" + self.display.text() + ")", result)
            except Exception as e:
                self.display.setText("Error")
        elif button == 'cos':
            try:
                result = str(math.cos(float(self.display.text())))
                self.display.setText(result)
                self.store_operation("cos(" + self.display.text() + ")", result)
            except Exception as e:
                self.display.setText("Error")
        elif button == 'exp':
            try:
                result = str(math.exp(float(self.display.text())))
                self.display.setText(result)
                self.store_operation("exp(" + self.display.text() + ")", result)
            except Exception as e:
                self.display.setText("Error")
        elif button == 'C':
            self.display.clear()


    def store_operation(self, operation, result):
        with open("calculator_history.txt", "a") as f:
            f.write(f"Operation: {operation}, Result: {result}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
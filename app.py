import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QStackedWidget, QGridLayout, QComboBox)
from PyQt5.QtCore import Qt
from calculator import SimpleCalculator, ScientificCalculator

class CalculatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Advanced Calculator')
        self.setGeometry(100, 100, 400, 500)
        self.mode = 'Simple'
        self.simple_calc = SimpleCalculator()
        self.sci_calc = ScientificCalculator()
        self.current_input = ''
        self.create_ui()

    def create_ui(self):
        main_layout = QVBoxLayout()
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(['Simple', 'Scientific'])
        self.mode_selector.currentTextChanged.connect(self.switch_mode)
        main_layout.addWidget(self.mode_selector)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(40)
        main_layout.addWidget(self.display)

        self.stacked = QStackedWidget()
        self.stacked.addWidget(self.simple_buttons())
        self.stacked.addWidget(self.scientific_buttons())
        main_layout.addWidget(self.stacked)

        self.setLayout(main_layout)
        self.switch_mode('Simple')

    def simple_buttons(self):
        widget = QWidget()
        layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0),
        ]
        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self.button_clicked)
            layout.addWidget(btn, row, col)
        widget.setLayout(layout)
        return widget

    def scientific_buttons(self):
        widget = QWidget()
        layout = QGridLayout()
        sci_buttons = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('^', 0, 3),
            ('log', 1, 0), ('log10', 1, 1), ('sqrt', 1, 2), ('exp', 1, 3),
            ('(', 2, 0), (')', 2, 1), ('pi', 2, 2), ('e', 2, 3),
            ('asin', 3, 0), ('acos', 3, 1), ('atan', 3, 2), ('!', 3, 3),
        ]
        # Add number and symbol buttons as in simple
        for text, row, col in sci_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self.button_clicked)
            layout.addWidget(btn, row, col)
        # Add number and symbol buttons
        num_buttons = [
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
            ('0', 7, 0), ('.', 7, 1), ('=', 7, 2), ('+', 7, 3),
            ('C', 8, 0),
        ]
        for text, row, col in num_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(self.button_clicked)
            layout.addWidget(btn, row, col)
        widget.setLayout(layout)
        return widget

    def switch_mode(self, mode):
        self.mode = mode
        self.display.clear()
        self.current_input = ''
        if mode == 'Simple':
            self.stacked.setCurrentIndex(0)
        else:
            self.stacked.setCurrentIndex(1)

    def button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == 'C':
            self.display.clear()
            self.current_input = ''
        elif text == '=':
            self.calculate()
        elif text in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'log10', 'sqrt', 'exp', 'pi', 'e', '^', '!', '(', ')']:
            self.current_input += text + '('
            self.display.setText(self.current_input)
        else:
            self.current_input += text
            self.display.setText(self.current_input)

    def calculate(self):
        expr = self.current_input
        try:
            if self.mode == 'Simple':
                result = str(eval(expr))
            else:
                result = str(self.eval_scientific(expr))
            self.display.setText(result)
            self.current_input = result
        except Exception as e:
            self.display.setText('Error')
            self.current_input = ''

    def eval_scientific(self, expr):
        # Replace symbols with function calls
        expr = expr.replace('^', '**').replace('pi(', 'self.sci_calc.pi()').replace('e(', 'self.sci_calc.e()')
        # Map functions
        for func in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'log10', 'sqrt', 'exp']:
            expr = expr.replace(f'{func}(', f'self.sci_calc.{func}(')
        expr = expr.replace('!(', 'self.sci_calc.factorial(')
        return eval(expr)

def main():
    app = QApplication(sys.argv)
    window = CalculatorGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

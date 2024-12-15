from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
import random

app = QApplication([])

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generate)

    def generate(self): 
        symvols = ""
        if self.ui.Generate.isChecked():
            symvols += "qwertyuiopasdfghjklzxcvbnm"
        if self.ui.use_numbers.isChecked():
            symvols += "1234567890"

        password = ""
        i = random.randint(8, 12)

        while i > 0:
            password += random.choice(symvols)
            i -= 1
        print(password)
        
        self.ui.lbl_result.setText(password)


window = Widget()

style = '''
QWidget {
    background-color: rgb(217, 234, 253);
}
QLabel {
    color: rgb(154, 166, 178);
}
QPushButton {
    background-color: rgb(188, 204, 220);
    color: rgb(154, 166, 178);
    border-radius: 5px;
    font-weight: bold;
    height: 25px;
}
'''
app.setStyleSheet(style)


window.show()
app.exec_()
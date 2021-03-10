import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)


class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30,30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120,35)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300,300,300,200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:') # 입력 대화창 생성 / input Dialog : 대화창의 타이틀 / Enter your name : 대화창 안에 보여질 메시지

        if ok:
            self.le.setText(str(text)) # 줄 편집 위젯에 표시

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

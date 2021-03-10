import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0) # 배경 검정색

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(300,300,250,180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor() # 색상 저장

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
            # 색상을 선택하고 'OK' 버튼을 눌렀다면 col.isValid()의 불 값이 True이고, 'Cancle' 버튼을 눌렀다면 불 값이 False가 됨


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
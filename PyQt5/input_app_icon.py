import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.jpg'))
        self.setGeometry(300,300,300,200)  #1,2 - 창의 위치(x,y) / 3,4 - 창의 높이와 넓이
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
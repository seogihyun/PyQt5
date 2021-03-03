import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self) # 'Show title'이라는 텍스트 라벨을 갖는 체크박스 생성
        cb.move(20,20)
        cb.toggle() # 체크박스 on 상태로 변환
        cb.stateChanged.connect(self.changeTitle) 
        
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300,300,300,200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')

        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
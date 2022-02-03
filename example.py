import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic # ui 파일을 사용하기 위한 모듈 import

UI_class = uic.loadUiType("example.ui")[0]

class MyWindow(QMainWindow, UI_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()     # 이벤트 루프
                # '닫기' 이벤트 발생 전까지 계속 GUI 프로그램을 실행시키는 코드
                # app은 QApplication 클래스의 인스턴스

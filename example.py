import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # 윈도우 타이틀 변경
        self.setWindowTitle("GUI TEST")

        # 윈도우 크기 변경
        self.setGeometry(300, 300, 400, 400)    # 순서대로 창 위치 x,y  창 크기 x,y

    def initUI(self):
        btn = QPushButton("Button", self)
        btn.clicked.connect(self.surprise)

    def surprise(self):
        print("Button is Clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()     # 이벤트 루프 
                    # '닫기' 이벤트 발생 전까지 계속 GUI 프로그램을 실행시키는 코드
                    # app은 QApplication 클래스의 인스턴스
app.exec_()
print("루프 밖")
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI 파일 연결
# 단, UI 파일은 Python 코드 파일과 같은 디렉토리에 위치해야 한다.
form_class = uic.loadUiType("test.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass (QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # test

        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
        """
        -------------------------------------------------------------
        이 부분에 시그널을 입력해야 합니다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
        -------------------------------------------------------------
        """

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는 (프로그램을 작동시키는) 코드
    app.exec_()
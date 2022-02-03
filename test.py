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

        # pushButtno (Start!)을 누르면 아래 functionStart 메소드와 연결됨
        self.pushButton.clicked.connect(self.functionStart)
        """
        -------------------------------------------------------------
        이 부분에 시그널을 입력해야 합니다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
        -------------------------------------------------------------
        """

    # Start! 버튼 눌렀을 때 실행되는 메소드
    def functionStart(self):
        self.progressBar.setRange(0, 19) # progressBar 초기 설정 (100을 0~19, 20단계로 나눔)

        for i in range(1, 21):
            print("출력 : ", str(i))
            self.progressBar.setValue(i)    # progress bar 진행률 올리기
            self.textBrowser.append("출력 : " + str(i))

# 코드 실행시 GUI 창을 띄우는 부분
# __name__ == "__main__" : 모듈로 활용되는 것이 아니라, 해당 .py파일에서 직접 실행되는 경우에만 코드 실행

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

'''
if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는 (프로그램을 작동시키는) 코드
    app.exec_()
'''

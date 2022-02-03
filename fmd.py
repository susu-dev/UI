import cv2
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui

# UI파일 연결
load_ui = uic.loadUiType("fmd.ui")[0]
print(load_ui)

class ShowVideo(QtCore.QObject):

    flag = 0

    cam = cv2.VideoCapture(0)

    ret, image = cam.read()
    height, width = image.shape[:2]

    mVideo = QtCore.pyqtSignal(QtGui.QImage)
    tVideo = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):
        global image

        run_video = True
        while run_video:
            ret, image = self.cam.read()
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)


            if self.flag:
                img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                img_canny = cv2.Canny(img_gray, 50, 100)

                qt_image2 = QtGui.QImage(img_canny.data,
                                         self.width,
                                         self.height,
                                         img_canny.strides[0],
                                         QtGui.QImage.Format_Grayscale8)

                self.VideoSignal2.emit(qt_image2)


            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit) #25 ms
            loop.exec_()

    @QtCore.pyqtSlot()
    def canny(self):
        self.flag = 1 - self.flag

class WindowClass (QMainWindow, load_ui) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # test

        # pushButton (Start!)을 누르면 아래 functionStart 메소드와 연결됨
        self.mOpen.clicked.connect(self.functionStart)
        self.mClose.clicked.connect(self.functionStart)
        """
        -------------------------------------------------------------
        이 부분에 시그널을 입력해야 합니다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수로 작성합니다.
        -------------------------------------------------------------
        """

    # Open/Close 버튼 눌렀을 때 실행되는 메소드
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

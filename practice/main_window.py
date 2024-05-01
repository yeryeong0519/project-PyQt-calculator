# main_window.py

"""Main window-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class Window(QMainWindow):  # QMainWindow를 상속한 Window 클래스 생성
    def __init__(self): # 클래스 초기화 메소드 정의
        super().__init__(parent=None)   # 기본 클래스의 초기화 메소드 호출
        self.setWindowTitle("QMainWindow")  # 창 제목 설정
        self.setCentralWidget(QLabel("I'm the Central Widget")) # 중심 위젯 설정
        self._createMenu()  
        self._createToolBar()
        self._createStatusBar() # 비공개 메소드를 호출하여 다양한 GUI 요소 생성

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close) # 메인 메뉴 바를 만들고 Menu라는 드랍다운 메뉴 생성

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)  # 툴바 생성. 툴바에는 앱을 종료할 버튼이 포함됨

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)   # 앱의 상태 표시줄 생성

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
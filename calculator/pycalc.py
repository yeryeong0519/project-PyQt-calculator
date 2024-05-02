import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QWidget

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235   # 창의 크기
DISPLAY_HEIGHT = 35 # 디스플레이 높이
BUTTON_SIZE = 40    # 버튼 크기

class PyCalcWindow(QMainWindow):    # PyCalcWindow 클래스는 QMainWindow를 상속, 메인 화면 정의
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")   # 창 제목 설정
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE) #고정 크기 설정
        self.generalLayout = QVBoxLayout()  # 수직 레이아웃 생성
        self._centralWidget = QWidget(self) # 중앙 위젯 생성
        self.setCentralWidget(self._centralWidget)  # 중앙 위젯 생성
        self._centralWidget.setLayout(self.generalLayout)   # 레이아웃 생성
        self._createDisplay()   # 디스플레이 생성
        self._createButtons()   # 버튼 생성

    def _createDisplay(self):
        # 디스클레이 생성 메소드
        self.display = QLineEdit()  #QLineEdit 위젯 생성
        self.display.setFixedHeight(DISPLAY_HEIGHT) # 고정 높이 설정
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)  # 오른쪽 정렬 설정
        self.display.setReadOnly(True)  # 읽기 전용으로 설정
        self.generalLayout.addWidget(self.display)  # 레이아웃에 추가

    def _createButtons(self):
        # 버튼 생성 메소드
        self.buttonMap = {} # 버튼을 저장할 딕셔너리
        buttonsLayout = QGridLayout()   # 그리드 레이아웃 생성
        keyboard = [    # 키보드 버튼의 레이아웃
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyboard):   # 그리드에 버튼 추가
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)  # 버튼 생성
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)  # 버튼 크기 설정
                buttonsLayout.addWidget(self.buttonMap[key], row, col)  # 그리드에 버튼 추가

        self.generalLayout.addLayout(buttonsLayout) # 버튼 레이아웃을 메인 레이아웃에 추가

    def setDisplayText(self, text):
        """디스플레이 텍스트 설정 메소드"""
        self.display.setText(text)  # 텍스트 설정
        self.display.setFocus() # 포커스 설정

    def displayText(self):
        """디스플레이 텍스트 반환 메소드"""
        return self.display.text()  # 텍스트 반환

    def clearDisplay(self):
        """디스플레이 지우기 메소드"""
        self.setDisplayText("") # 텍스트 지우기

class PyCalc:
    """PyCalc의 컨트롤러 클래스."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        """결과 계산 메소드"""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        """수식 작성 메소드"""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        """시그널 및 슬롯 연결 메소드"""
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

def evaluateExpression(expression):
    """수식 평가 메소드"""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result
     
def main():
    """PyCalc's main function"""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()

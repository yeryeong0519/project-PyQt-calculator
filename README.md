### What is PyQt?
> **Qt**는 C++를 주 언어로 사용하는 GUI(Graphic User Interface) 프레임워크이다. '큐트'라고 읽으며, C++와 QML이라는 자체 스크립트 언어를 기반으로 한다. 플랫폼에 독립적인 GUI를 위한 추상화를 제공한다. 또한 네트워킹, 스레드, 정규 표현식, SQL, SVG 등 다양하고 강력한 기능을 제공한다. 

> PyQt는 윈도우, 유닉스, 리눅스, 맥, iOS 및 안드로이드와 호환된다. 

> 프로젝트 개요 :
OS : macOS
작업환경 : VSC(Visual Studio Code)
프레임워크 : PyQt6(파이썬 3.6.1이상 필요)

### PyQt installation

```
python -m venv venv
source venv/bin/activate
python -m pip install pyqt6
```
혹은
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pyqt6
```
![](https://velog.velcdn.com/images/yeryoong/post/dc2c4e1f-9b25-4278-9a5d-884d65c0b457/image.png)

### Hello, World!

```
#hello.py

import sys #내장 모듈 'exit()'함수 사용하기위해 호출

#1. 이들을 사용하여 GUI 애플리케이션을 만들고 관리
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

#2. 'QApplication'클래스의 인스턴스를 생성하여 애플리케이션 객체 생성
app = QApplication([])

#3. 애플리케이션 GUI 생성
window = QWidget()
window.setWindowTitle("PyQt App")   #애플리케이션의 창 제목 설정
window.setGeometry(100, 100, 280, 80)   #애플리케이션의 창의 크기와 화면 위치 정의(x좌표, y좌표, 너비, 높이)
helloMsg = QLabel("<h1>Hello, World</h1>", parent=window)   #QLabel 객체는 HTML 형식의 텍스트 표시
helloMsg.move(60, 15)   #'helloMsg'를 창의 좌표 (60, 15)에 배치

#4. 애플리케이션 GUI 보이기
window.show()
#5. 이벤트 루프 실행
sys.exit(app.exec())
```

#### 실행
```
(venv) yeryeongseo@seoyelyeong-ui-MacBookPro pyqt % python3 hello.py
```

#### 결과화면
![](https://velog.velcdn.com/images/yeryoong/post/8663928e-0b8f-4ae9-8b3a-3bd7933775bf/image.png)


이제 그리드 레이아웃을 사용하는 간단한 예제를 해보좌

```
# g_layout.py

"""Grid layout example."""

import sys

from PyQt6.QtWidgets import (QApplication, QGridLayout, QPushButton, QWidget,)

# PyQt 애플리케이션 생성
app = QApplication([])

# 윈도우 생성 및 제목 생성
window = QWidget()
window.setWindowTitle("QGridLayout")

# 그리드 레이아웃 생성
layout = QGridLayout()

#버튼 위젯 그리드 레이아웃에 추가
# .addWidget()메소드에 전달하는 두번째, 세번째 인수는 각 위젯의 그리드 내 위치 정의
layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
layout.addWidget(
    QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
)

#윈도우에 레이아웃 설정
window.setLayout(layout)

#윈도우 표시
window.show()

#애플리케이션 이벤트 루프 실행 및 종료
sys.exit(app.exec())

```
#### 결과화면
![](https://velog.velcdn.com/images/yeryoong/post/2e470d52-c36a-43e9-aa4f-c3745199d033/image.png)

이제 QFormLayout 객체를 사용하여 위젯을 배열하는 애플리케이션을 생성해본다.

### 위젯 배열 예제 애플리케이션

```
# f_layout.py

"""Form layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

# '.addRow()'라는 메소드를 사용하여 두 개의 위젯이 포함된 행을 레이아웃에 추가
# '.addRow()'의 첫 번째 인수는 라벨 또는 문자열이어야함.
# 두 번째 인수는 사용자가 데이터를 입력/편집 할 수 있는 어떤 위젯이던 무관.
# 이 예제에서는 QLineEdit() 사용
layout = QFormLayout()
layout.addRow("이름:", QLineEdit())
layout.addRow("나이:", QLineEdit())
layout.addRow("직업:", QLineEdit())
layout.addRow("취미:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())
```

#### 결과화면
![](https://velog.velcdn.com/images/yeryoong/post/c1c52db2-a47e-4d2f-bca0-e4a67a5f8aeb/image.png)

QDialog 클래스를 사용하여 대화 상자 스타일의 애플리케이션을 만들어보자.


### 대화형 상자 애플리케이션
```
# dialog.py

"""대화형 애플리케이션"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        #super()을 사용하여 부모클래스의 __init__() 메소드를 호출하여 클래스의 인스턴스 초기화
        #이 예제에서는 부모 인수를 None으로 설정. 이 대화상자가 메인 창이 되기 때문
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout()    #QVBoxLayout 객체를 'dialogLayout'에 할당
        formLayout = QFormLayout()
        formLayout.addRow("환자명:", QLineEdit())
        formLayout.addRow("생년월일:", QLineEdit())
        formLayout.addRow("혈액형:", QLineEdit())
        formLayout.addRow("몸무게:", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)

#조건문 안의 들여쓰인 코드가 모듈로 가져와지는것이 아님
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
```

#### 결과화면
![](https://velog.velcdn.com/images/yeryoong/post/72f6dea8-c359-427f-b92e-c3905ba997ae/image.png)

### Main Windows
> 대부분의 경우 GUI 애플리케이션은 메인 창 형태로 만들어진다. 메뉴바, 툴바, 상태표시줄 및 위젯이 포함된 유형이다. 사용자의 입력에 따라 여러 대화상자가 필요할수도 있다. 메인 창 형태의 애플리케이션을 만들려면 QMainWindow를 상속해야하는데, 이를 상속한 클래스의 인스턴스는 애플리케이션의 주요 창으로 간주되고, 유일해야한다. QMainWindow는 애플리케이션의 GUI를 빠르게 구축 할 수 있도록 해주는 프레임워크를 제공한다. 이 클래스에는 내장 레이아웃이 있는데 이 중 중심 위젯은 반드시 필요하다. 필요하지 않은 경우, QWidget객체를 사용하여 빈 공간으로 사용 할 수 있다. 

![](https://velog.velcdn.com/images/yeryoong/post/e8045a13-7aea-46cb-aa2f-7472bb16fa69/image.png)


메인 창 예제로 연습해보자.

#### Main Windows 예제
```
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
```

#### 결과화면
![](https://velog.velcdn.com/images/yeryoong/post/ae5ef21f-0169-45c6-bd42-e85f95ff3634/image.png)


macOS 특성 상 메뉴 옵션의 표시 방식이 다를 수 있다. 애플리케이션을 실행 할 때 'Exit' 혹은 'Quit' 옵션이 메뉴바에서 표시되지않거나 앱의 상단메뉴에서 표시 될 수 있다. 이럴 때는 메인창을 닫거나 'Command + Q'로 종료 할 수 있다... 

### 시그널과 슬롯(Signal and Slot)
> 시그널 자체는 어떠한 동작도 수행하지 않는다. 시그널 작동을 위해서는 슬롯에 연결해야한다. 이는 시그널이 발생 할 때마다 동작을 수행 할 함수 또는 메소드다. 시그널이 슬롯에 연결되어있으면 시그널이 발생 할 때마다 슬롯이 호출된다. 슬롯에 연결되어있지 않는 경우에는 아무 일도 일어나지 않고 시그널이 무시된다. 다음은 시그널과 슬롯의 가장 중요한 특징들이다.

* 시그널은 하나 이상의 슬롯에 연결 될 수 없다.
* 시그널은 또 다른 시그널에 연결 될 수 있다.
* 슬롯은 하나 이상의 시그널에 연결 될 수 있다.

```
widget.signal.connect(slot_function)
```

#### 시그널과 슬롯 예제

 ```
 signals_slots.py

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet():    #'greet()'함수를 생성하여 이를 버튼 클릭 시 실행될 슬롯으로 사용
    if msgLabel.text(): # 만약 .msgLable의 텍스트가 있는 경우
        msgLabel.setText("")    # 라벨의 텍스트 삭제
    else:
        msgLabel.setText("환영합니다!") # 아닐경우 텍스트로 설정

app = QApplication([])  # 애플리케이션 초기화
window = QWidget()  # 메인 화면 생성
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()  # 수직 박스 레이아웃 생성. 버튼과 라벨을 수직으로 배치

button = QPushButton("Greet")
button.clicked.connect(greet)   # 버튼 클릭 시 'greet()' 함수 출력

layout.addWidget(button)    # 버튼을 수직 레이아웃에 추가
msgLabel = QLabel("")   # 빈 QLabel 위젯 생성. 버튼이 클릭 될 때 환영메세지 표시
layout.addWidget(msgLabel)  # 레이블을 수직 레이아웃에 추가
window.setLayout(layout)    # 윈도우에 레이아웃 설정
window.show()
sys.exit(app.exec())
```

#### 결과화면
![](https://velog.velcdn.com/images/yeryoong/post/cbe61bc8-5523-4ba0-b533-2e989da95461/image.png)![](https://velog.velcdn.com/images/yeryoong/post/4be550e4-7d76-4a22-9568-173b62735766/image.png)

여기까지 PyQt 기본을 정리해보았습니다..

이번엔 MVC(Model-View-Controller) 디자인 패턴을 이용하여 계산기 GUI 앱을 구현해볼것이다.

우선 MVC 에 대해 간단히 설명해보자면...

### MVC 디자인
> * Model : 앱의 비즈니스 로직을 처리한다. 핵심 기능과 데이터를 포함한다. 계산기 앱에서는 입력 값과 계산을 처리한다.
* View : 앱의 GUI를 구현한다. 사용자가 상호작용 할 수 있는 모든 위젯을 포함하며, 사용자의 동작과 이벤트를 수신한다. 계산기 앱에서는 화면에 표시되는 창이 뷰다.
* Controller : 모델과 뷰를 연결하여 애플리케이션을 작동시킨다. 사용자의 이벤트나 요청은 컨트롤러로 전송되며, 컨트롤러는 모델을 작동시킨다. 모델이 올바른 형식으로 요청된 결과나 데이터를 제공하면 컨트롤러가 뷰로 전달한다. 계산기 앱에서 컨트롤러는 GUI에서 대상 수식을 받아 모델에게 계산을 요청하고 결과를 GUI에 반영한다. 


### 계산기 애플리케이션이 작동하는 방식
> 1. 사용자가 뷰(GUI)에서 동작이나 요청 수행
2. 뷰는 사용자의 동작을 컨트롤러에게 알림
3. 컨트롤러는 사용자의 요청을 받아 모델에 쿼리(query)하여 응답 얻음
4. 모델은 컨트롤러의 쿼리를 처리하고 필요한 계산을 수행 한 뒤 결과 반환
5. 컨트롤러는 모델의 응답을 받아 뷰를 업데이트
6. 마지막으로 사용자는 뷰에서 요청된 결과를 확인

## 프로그램 짜기
### 뼈대 생성
```
#pycalc.py

import sys

from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

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

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)    # 애플리케이션 객체 생성
    window = PyCalcWindow() # 메인 화면 객체 생성
    window.show()
    sys.exit(app.exec())

```


### 실행화면
![](https://velog.velcdn.com/images/yeryoong/post/dd8f4712-e3db-4421-b357-c5160781ec10/image.png)


이렇게 뼈대를 만들었으니 비즈니스 로직 즉 계산기 애플리케이션에서는 수식을 계산할 모델이 필요하다. 또한 계산기 모델은 오류를 처리해야하므로 다음과 같은 전역 상수를 정의한다. 

```
# pycalc.py
# ...

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
# ...
```





```
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
```



```
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
```
>'_calculateResult()'메소드에서는 사용자가 계산기 디스플레이에 입력한 수식을 평가하기위해 '_evaluate()' 메소드를 활용한다. 그런 다음 결과를 디스플레이 텍스트에 업데이트하기위해 view에서 'setDisplayText()'가 호출된다.

```
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
        
```

> PyCalc 라는 클래스 내에서는 클래스의 초기화자가 정의되어있다. 이는 두 개의 인수, 즉 앱의 모델과 뷰를 가져온다. 이러한 인수는 적절한 인스턴스 속성에 저장된다. 그리고 '_connectSignalsAndSlots()' 메소드가 호출되어 신호와 슬롯 사이의 필요한 모든 연결이 설정된다. 

```
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
```

### 전체 코드

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
```


### 최종 실행 화면
![](https://velog.velcdn.com/images/yeryoong/post/e53cd645-050c-415c-b521-37d9c1f00991/image.png)

![](https://velog.velcdn.com/images/yeryoong/post/3e0bae0f-9a15-47e4-8b54-6096b5865759/image.gif)

> 터미널에서 애플리케이션을 실행하면 계산기가 뜰것이다. PyQt를 추가적으로 수정하고싶다면 Qt Designer이 있다. 이는 드래그 앤 드롭 인터페이스를 사용하여 GUI를 설계하고 구축 할 수 있다. 이번 프로젝트를 통해 익힌 내용
* Python과 PyQt를 사용하여 그래픽 사용자 인터페이스를 구축하는 방법
* 사용자의 이벤트를 앱의 논리에 연결하는 방법
* 적절한 프로젝트 레이아웃을 사용하여 PyQt 애플리케이션을 조직하는 방법
* PyQt를 사용하여 실제 GUI 애플리케이션을 만드는 방법

### 전체코드

```import sys
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
    main()```


출처 https://realpython.com/python-pyqt-gui-calculator/

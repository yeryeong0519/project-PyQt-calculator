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
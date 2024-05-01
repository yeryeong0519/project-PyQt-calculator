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
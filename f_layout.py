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
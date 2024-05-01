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
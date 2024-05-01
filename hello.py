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
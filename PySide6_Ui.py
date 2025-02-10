from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile
from PySide6.QtGui import QPixmap # QPixmap 모듈 임포트
import sys

from functools import partial

class MyFirstUi(QMainWindow): # QMainWindow를 상속 받았다.
    def __init__(self):
        super().__init__() # QMainWindow 생성자를 실행
        ui_file_path = "/home/rapa/My_Python/My_Python0113/my_fiset_ui.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader() # ui파일에 있는 내용을 읽어 객체로 반환
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close() # 메모리 누수의 원인중 하나(습관화 할것)

        # self.ui.pushButton_click.clicked.connect(partial(self.on_button_click, "월요일"))
        self.ui.pushButton_click.clicked.connect(lambda : self.on_button_click("월요일")) # lamda 사용 방법

        self.ui.lineEdit_input.textChanged.connect(self.on_changed_text)

        pixmap = QPixmap("/home/rapa/My_Python/My_Python0113/ui_images.jpeg") # 이미지 경로
        scaled_pixmap = pixmap.scaled(400, 500) # 이미지 사이즈 조절
        self.ui.labal_pic.setPixmap(scaled_pixmap) #라벨에 이미지 넣기!
        
    def on_changed_text(self):
        text = self.ui.lineEdit_input.text()
        print(text)
    
    def on_button_click(self, today):
        print("클릭되었습니다.")
        #label_my_text.setText = 내가 정의한 이름으로 작성하기
        self.ui.label_my_text.setText(f"{today} 유후___ ҉반 ҉짝 ҉ ★ 너무 행복하다~~ભય નુૂપ?")

        input_text = self.ui.lineEdit_input.text()
        print(input_text)

app = QApplication()
win = MyFirstUi()
app.exec()
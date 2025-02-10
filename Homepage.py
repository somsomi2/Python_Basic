"""
회원가입 페이지
아이디와 비밀번호와 전화번호, 이메일을 입력 받을 수 있는 회원가입페이지의 폼을 만들고,
회원가입을 누르면 딕셔너리에 저장되도록 만들기
*lineEdit의 모드를 password로 바꾸기
"""

from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile
import sys

from functools import partial
from PySide6.QtGui import QPixmap # QPixmap 모듈 임포트

import json
import os

class MyFirstUi(QMainWindow): # QMainWindow를 상속 받았다.


    def __init__(self):
        super().__init__() # QMainWindow 생성자를 실행
        ui_file_path = "/home/rapa/My_Python/My_Python0113/my_homepage.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader() # ui파일에 있는 내용을 읽어 객체로 반환
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close() # 메모리 누수의 원인중 하나(습관화 할것)

        self.ui.pushButton_sub.clicked.connect(lambda : self.on_button_click("회원가입 완료!")) # lamda 사용 방법
    
        self.json_path = "/home/rapa/My_Python/My_Python0113/Homepage.json"
        self.PersonalData_dict = self.load_json() #생산자에서 딕셔너리를 추가
        print (self.PersonalData_dict)

        pixmap = QPixmap("/home/rapa/My_Python/My_Python0113/homepage_image.jpeg") # 이미지 경로
        scaled_pixmap = pixmap.scaled(403, 227) # 이미지 사이즈 조절
        self.ui.labal_pic.setPixmap(scaled_pixmap) #라벨에 이미지 넣기!


    def load_json(self):
        """json 파일을 불러오는데, 경로에 없을 경우 빈 딕셔너리를 리턴합니다."""
        if not os.path.exists(self.json_path):
            return{}

        with open(self.json_path, "r") as file:
            data = json.load(file)
            return data
    
    def update_json(self):
        """현재 인스턴스의 사원 딕셔너리를 저장합니다."""
        with open(self.json_path, "w") as file:
            json.dump(self.PersonalData_dict, file, ensure_ascii=False, indent=4)

    def add_dict(self, id, password, phone, email):
        personal_code = self.on_changed_text()
        self.PersonalData_dict[personal_code] = {
            "ID" : id,
            "Password" : password,
            "Phonenumber" : phone,
            "Email" : email
        }
        self.update_json()

# 인풋에 따라 텍스트가 바뀌도록 만들기
    def on_changed_text(self):
        text = self.ui.lineEdit_ID.text()
        text = self.ui.lineEdit_Password.text()
        text = self.ui.lineEdit_Phone.text()
        text = self.ui.lineEdit_Email.text()
        print(text)
    
    def on_button_click(self, today):
        print("클릭되었습니다.")
        self.ui.label_my_log.setText(f"{today} 유후___ ҉반 ҉짝 ҉ ★")

        input_text = self.ui.lineEdit_ID.text()
        print(input_text)

        id = self.ui.lineEdit_ID.text()
        password = self.ui.lineEdit_Password.text()
        phone = self.ui.lineEdit_Phone.text()
        email = self.ui.lineEdit_Email.text()
        self.add_dict(id, password, phone, email)


app = QApplication()
win = MyFirstUi()
app.exec()
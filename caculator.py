from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile
import sys

from functools import partial

class MyFirstUi(QMainWindow): # QMainWindow를 상속 받았다.

    def __init__(self, result = None):
        super().__init__() # QMainWindow 생성자를 실행
        ui_file_path = "/home/rapa/My_Python/My_Python0113/calculator.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader() # ui파일에 있는 내용을 읽어 객체로 반환
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close() # 메모리 누수의 원인중 하나(습관화 할것)

        self.num_list = []
        
        self.ui.pushButton_c.clicked.connect(partial( self.on_button_click, "c")) # lamda 사용 방법
        self.ui.pushButton_plmi.clicked.connect(partial( self.on_button_click, "+/-")) # lamda 사용 방법
        self.ui.pushButton_per.clicked.connect(partial( self.on_button_click, "%")) # lamda 사용 방법
        self.ui.pushButton_div.clicked.connect(partial( self.on_button_click, "/")) # lamda 사용 방법
        self.ui.pushButton_multiy.clicked.connect(partial( self.on_button_click, "*")) # lamda 사용 방법
        self.ui.pushButton_minus.clicked.connect(partial( self.on_button_click, "-")) # lamda 사용 방법
        self.ui.pushButton_plus.clicked.connect(partial( self.on_button_click, "+")) # lamda 사용 방법
        self.ui.pushButton_equl.clicked.connect(partial( self.result, "=")) # lamda 사용 방법
        self.ui.pushButton_com.clicked.connect(partial( self.on_button_click, ".")) # lamda 사용 방법

        self.ui.pushButton_0.clicked.connect(partial( self.on_button_click, "0")) # lamda 사용 방법
        self.ui.pushButton_1.clicked.connect(partial( self.on_button_click, "1")) # lamda 사용 방법
        self.ui.pushButton_2.clicked.connect(partial( self.on_button_click, "2")) # lamda 사용 방법
        self.ui.pushButton_3.clicked.connect(partial( self.on_button_click, "3")) # lamda 사용 방법
        self.ui.pushButton_4.clicked.connect(partial( self.on_button_click, "4")) # lamda 사용 방법
        self.ui.pushButton_5.clicked.connect(partial( self.on_button_click, "5")) # lamda 사용 방법
        self.ui.pushButton_6.clicked.connect(partial( self.on_button_click, "6")) # lamda 사용 방법
        self.ui.pushButton_7.clicked.connect(partial( self.on_button_click, "7")) # lamda 사용 방법
        self.ui.pushButton_8.clicked.connect(partial( self.on_button_click, "8")) # lamda 사용 방법
        self.ui.pushButton_9.clicked.connect(partial( self.on_button_click, "9")) # lamda 사용 방법

    def on_button_click(self, Button):

        if Button == "c":

            self.num_list = [""]
            self.ui.label_typing.setText("0")
        
        else:
            self.num_list.append(Button)
            self.text = f"{''.join(self.num_list)}"
            self.ui.label_typing.setText(self.text)

    def result(self,echol):
        result_num = eval(self.text)
        result_num = float(result_num)

        if echol == "=":
            self.ui.label_typing.setText(str(result_num))

#     def add(self, num): # 5를 받아서
#         num = self.ui.lineEdit.text()
#         add += num # self.result = 5를 가산했다.
#         self.result = add
#         print(self.result)
        
#     def sub(self, num):
#         self.result -= num # self.result를 5 감산한다.
#         print(self.result)

#     def mul(self, num):
#         self.result *= num
#         print(self.result)
#         self.ui.label_typing.setText(f"{num}")
#         input_text = self.ui.lineEdit.text()
#         print(input_text)

#     def reset(self, num=None):
#         if num:
#             self.result = num
#         else:
#             self.result = 0
#         print(f"{self.result} 값으로 초기화 되었습니다.") 

# # 인풋에 따라 텍스트가 바뀌도록 만들기
#     def on_changed_text(self):
#         text = self.ui.lineEdit.text()
#         print(text)
    
    # def on_button_click(self, today):
    #     print("클릭되었습니다.")
    #     self.ui.label_typing.setText(f"{today}")
    #     input_text = self.ui.lineEdit.text()
    #     print(input_text)
    #     result = str(eval(input_text))

app = QApplication()
win = MyFirstUi()
app.exec()
"""
슬램덩크 json 파일을 불러와서, key로 저장된 선수들의 이름이 리스트 위젯에 작성되게 해주세요
리스트 위젯에서 선수 이름을 눌렀을때, 하단에 선수정보에 대한 내용이 ui에 표시되도록 해주세요.
선수를 추가할 수도 있고, 선수의 정보를 수정할수도 있어야 합니다.

# 리스트 위젯에서 선수 이름을 눌렀을때
itemClicked() -> item : 항목이 클릭되었을때 item을 반환

선수목록

윤대협
강백호
.
.
선수정보
학교 : 북산고등학교      포지션 : 가드
라벨 - 라인 에딧
"""

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtWidgets import QListWidget, QLineEdit, QSpinBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile
import os
import json

class ListWidgetTest(QMainWindow):
    def __init__(self):
        super().__init__() # 다른 클래스의 속성 및 메소드를 자동으로 불러와 해당 클래스에서 사용 가능하도록 한다.
        self.load_ui() # def load_ui를 호출한다.

        with open("/home/rapa/My_Python/My_Python0103/json/slamdunk.json", "r") as file:
            self.loaded_dict = json.load(file) # json 파일 불러오기

        self.view_item() # def view_item을 호출한다.
        # QT의 버튼을 각 이름에 따라 불러오고, 각 버튼에 메소드를 붙여준다.
        self.ui.pushButton_add.clicked.connect(self.on_add_item) # add
        self.ui.pushButton_remove.clicked.connect(self.on_remove_item) # remove
        self.ui.pushButton_edit.clicked.connect(self.on_edit_item) # edit player
        self.ui.listWidget.itemClicked.connect(self.display_player_info) # view player

    # 리스트 위젯의 항목 보여주기    
    def display_player_info(self, item): # 리스트 위젯의 아이템을 보여준다.
        current_player = item.text() # current_player는 item.text()를 갖는다. "강백호"라는 문자열을 반환
        school = (self.loaded_dict[current_player]["학교"]) # school은 item.text()가 가진 self.loaded_dict의 학교를 로드한다.
        position = (self.loaded_dict[current_player]["포지션"])
        height = (self.loaded_dict[current_player]["키"])
        char = (self.loaded_dict[current_player]["특징"])
        self.ui.lineEdit_school.setText(school) # lineEdit_school이라는 블록이 school텍스트를 가진다.
        self.ui.lineEdit_position.setText(position)
        self.ui.lineEdit_height.setText(str(height)) # 키는 숫자이기에 문자로 변환해준다.
        self.ui.lineEdit_char.setText(", ".join(char)) # 특징은 여러 항목의 리스트이기에, 병합해준다.

    def view_item(self): # 아이템을 기본적으로 보여줌
        for key, value in self.loaded_dict.items(): # 반복문으로 self.loaded_dict의 키, 벨류값을 불러온다.
            name = key # key는 이름이다.
            # print(name)
            self.ui.listWidget.addItem(name) # listWidget에 key의 값을 추가한다.
            items = self.ui.listWidget.selectedItems() # items는 selectedItems()된 것이다.
            for item in items: # 아이템이 items에 있을때 value를 출력한다.
                print(value)          

    def on_add_item(self): #
        # add
        text = self.ui.lineEdit_add.text() # lineEdit_add는 text다.
        self.ui.listWidget.addItem(text) # listWidget에 lineEdit_add의 텍스트를 추가한다.
        self.ui.lineEdit_add.clear() # lineEdit_add의 텍스트를 정리한다.

    def on_remove_item(self):
        current_row = self.ui.listWidget.currentRow() # listWidget의 해당하는 줄
        self.ui.listWidget.takeItem(current_row) # listWidget의 해당하는 줄의 아이템을 가져간다.

    def on_edit_item(self):
        player = self.ui.listWidget.currentItem().text() # player는 listWidget의 currentItem()의 text()를 가진다.
        school = self.ui.lineEdit_school.text() # lineEdit_school의 text()를 추가한다.
        position = self.ui.lineEdit_position.text()
        height = self.ui.lineEdit_height.text()
        char = self.ui.lineEdit_char.text()

        tmp = {} # 딕셔너리 선언
        tmp["학교"] = school # 딕셔너리 내부의 학교는 school
        tmp["포지션"] = position
        tmp["키"] = height
        tmp["특징"] = char
        self.loaded_dict[player] = tmp # loaded_dict[player]는 tmp
        print("수정되었습니다.")

    def load_ui(self):
        ui_file_path = "./slamdunk.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()

app = QApplication()
w = ListWidgetTest()
app.exec()
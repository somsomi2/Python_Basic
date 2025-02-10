from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtWidgets import QListWidget, QLineEdit, QSpinBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

class BasicPyside6(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_ui()

        # self.ui.label_text.setText("helloworld") # 라벨에 텍스트 수정
        # text = self.ui.label_text.text() # 라벨에 텍스트 변수 담기
        # self.ui.lineEdit_text.setText(text) # 변수에 있는 내용 라인 에딧에 담기

        # self.ui.lineEdit_text.returnPressed.connect(self.on_return_pressed) # 라인에딧에 있는 텍스트가 엔터를 누르면 입력
        self.ui.lineEdit_text.textChanged.connect(self.on_return_pressed) # 라인에딧의 텍스트가 실시간으로 입력

        # 위젯에 리스트의 항목을 넣기
        week = ["월요일", "화요일", "수요일", "목요일", "금요일"]

        self.ui.listWidget.addItems(week) # addItems는 리스트를 매개변수로 사용함

        # 연결되는 버튼
        self.ui.pushButton_move.clicked.connect(self.on_move_text)
        self.ui.pushButton_back.clicked.connect(self.on_back_text)
        self.ui.pushButton_submit.clicked.connect(self.get_data)

    # pushButton_submit을 누르면 실행되는 메서드
    def get_data(self):

        # 라디오 버튼이 눌렸는지 확인하는 방법_1
        if self.ui.radioButton_m.isChecked():
            print("성별이 남자입니다.")
        if self.ui.radioButton_fm.isChecked():
            print("성별이 여자입니다.")

        # 라디오 버튼이 눌렸는지 확인하는 방법_2(효율적)
        sex = "여자" # 기본적인 성별은 여자이다.
        if self.ui.radioButton_m.isChecked(): # 만약 남성이 선택된다면 남자
            sex = "남자"
        print(f"성별이 {sex} 입니다.")

        # 체크 박스가 클릭되면 출력된다. isChecked()--확인
        if self.ui.checkBox_1.isChecked():
            print("apple")
        if self.ui.checkBox_2.isChecked():
            print("banana")   
        if self.ui.checkBox_3.isChecked():
            print("bread><")                 

    # pushButton_move가 클릭되면 나오는 메서드
    def on_move_text(self):
        text = self.ui.listWidget.currentItem().text() # 텍스트는 listWidget.currentItem()의 문자이다.
        row = self.ui.listWidget.currentRow() # row는 리스트 위젯의 해당하는 줄이다.
        taked_item = self.ui.listWidget.takeItem(row) # taked_item은 리스트 위젯의 해당 줄을 가져간다.
        self.ui.comboBox.addItem(taked_item.text()) # comboBox에 taked_item의 텍스트를 추가한다.

        print(taked_item)
        print("눌렸다!!")
        # item = self.ui.listWidget.currentItem()
        # # 반환되는 것이 없을때 출력(조건문 처리)
        # if not item:
        #     text = ""
        # text = item.text()
        # addItem("문자열")
        # addItems("[리스트]")


    def on_back_text(self):
        # 콤보 박스에서 선택한 요소의 인덱스를 가져와 삭제
        text = self.ui.comboBox.currentText() # text는 comboBox에서 선택된 텍스트이다.
        idx = self.ui.comboBox.currentIndex() # idx는 comboBox의 선택된 인덱스이다.
        self.ui.comboBox.removeItem(idx) # 해당하는 인덱스를 삭제한다.

        week_dict = {   # 요일별 인덱스 부여
            "월요일" : 0,
            "화요일" : 1,
            "수요일" : 2,
            "목요일" : 3,
            "금요일" : 4
        }

        row = week_dict[text] # row는 week_dict의 [text]이다.
        # row = self.ui.comboBox.currentIndex()
        # print(row)
        self.ui.listWidget.insertItem(row, text) # listWidget에 row의 콤보박스 선택 text를 넣는다.
        # taked_item = self.ui.listWidget.takeItem(text)
        # self.ui.listWidget.addItem(taked_item)

    def on_return_pressed(self): # lineEdit_text와 연결
        text = self.ui.lineEdit_text.text() # 텍스트는 lineEdit_text의 문자이다.
        self.ui.label_text.setText(text) # 라벨 텍스트는 라인 에딧 텍스트로 설정된다.

    def load_ui(self):
        ui_file_path = "/home/rapa/My_Python/My_Python0116/basic_0116.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()


app = QApplication()
w = BasicPyside6()
app.exec()
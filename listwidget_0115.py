from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtWidgets import QListWidget, QLineEdit, QSpinBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile
import os

class ListWidgetTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        """
        slot : 위젯의 속성을 수정하고 싶을때 사용하는 메서드
        signal : 유저와 상호작용 이벤트시 사용하는 메서드
        """
        """
        ## 주요메서드
        addItem(item) : 리스트 위젯에 1개 항목을 가장 마지막 row에 추가함
        addItems(item list) : 리스트 위젯에 리스트 자료형을 마지막 row에 추가
        takeItem(row) : 리스트 위젯에서 입력한 row에 해당하는 아이템을 삭제하고 반환
        item(row) : row에 해당하는 요소를 반환
        insertItem(row, text) : 입력한 row에 텍스트를 추가
        clear() : 리스트 위젯의 모든 요소를 제거
        currentItem() -> item : 선택한 항목을 반환
        selectedItems() -> item list : 모든 선택한 항목을 리스트로 반환

        ##주요 시그널
        itemClicked() -> item : 항목이 클릭되었을때 item을 반환
        currentItemChanged() -> : 항목이 수정되었을때 item을 반환
        """

        # files = os.listdir ("/home/rapa/My_Python")
        # self.ui.listWidget.addItems(files)

        self.ui.pushButton_add.clicked.connect(self.on_add_item) # add
        self.ui.pushButton_insert.clicked.connect(self.on_insert_item) #insert
        self.ui.pushButton_clear.clicked.connect(self.clear_iteam) # clear
        self.ui.pushButton_print.clicked.connect(self.on_print_item) # print
        self.ui.pushButton_selected.clicked.connect(self.on_selected_item)
        self.ui.pushButton_remove.clicked.connect(self.on_remove_item) # remove
        # self.ui.pushButton_remove.clicked.connect(self.clear_iteam)

    def on_add_item(self):
        # add
        text = self.ui.lineEdit_add.text()
        self.ui.listWidget.addItem(text)
        self.ui.lineEdit_add.clear()

    def on_insert_item(self, row):
        row = self.ui.spinBox_insert.value()
        text = self.ui.lineEdit_insert.text()
        self.ui.listWidget.insertItem(row, text)
        self.ui.lineEdit_insert.clear()
    
    def on_print_item(self):
        item = self.ui.listWidget.currentItem()
        print(item.text())

    def on_selected_item(self):
        items = self.ui.listWidget.selectedItems()
        for item in items:
            print(item.text())

    def on_remove_item(self):
        row = self.ui.spinBox_insert.value()
        self.ui.listWidget.takeItem(row)

    def clear_iteam(self):
        self.ui.listWidget.clear()

    def load_ui(self):
        ui_file_path = "./listwidget.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()

app = QApplication()
w = ListWidgetTest()
app.exec()

# 학교는 라벨 초지션은 
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide6.QtWidgets import QListWidget, QLineEdit, QSpinBox
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile, Signal, Slot

class InputWindow(QWidget):

    emitter = Signal(list)

    def __init__(self):
        super().__init__()
        ui_file_path = "/home/rapa/My_Python/My_Python0117/ui/sub_tablewidget.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.subui = loader.load(ui_file)
        self.subui.show()
        ui_file.close()

        self.subui.pushButton.cli_usdcked.connect(self.make_user_info)
    
    def make_user_info(self):
        self.user_info = []

        name = self.subui.lineEdit_name.text()
        snum = self.subui.lineEdit_snum.text()
        major = self.subui.lineEdit_major.text()
        minor = self.subui.lineEdit_minor.text()
        row = self.subui.spinBox.value()

        self.user_info.append(name)
        self.user_info.append(snum)
        self.user_info.append(major)
        self.user_info.append(minor)
        self.user_info.append(row)

        self.emitter.emit(self.user_info)

        self.subui.close()

        # self.user_info["name"] = self.subui.lineEdit_name.text()
        # self.user_info["snum"] = self.subui.lineEdit_snum.text()
        # self.user_info["major"] = self.subui.lineEdit_major.text()
        # self.user_info["minor"] = self.subui.lineEdit_minor.text()
        # self.user_info["row"] = self.subui.spinBox.value()

class ListWidgetTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()

        self.ui.pushButton.clicked.connect(self.on_add_item) # add
        self.ui.pushButton_sub.clicked.connect(self.show_sub_window)

        # 테이블 치기 귀찮으니 줄여쓰기
        self.table = self.ui.tableWidget
        self.table.setRowCount(10)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["이름", "학번", "전공", "부전공"])

        item = QTableWidgetItem()
        item.setText("김준수")
        item.setTextAlignment(Qt.AlignCenter) # 중앙정렬
        self.table.setItem(0, 0, item) # 0번째 로우, 0번째 컬럼에 아이템을 넣겠다.

        item = QTableWidgetItem()
        item.setText("C202022")
        item.setTextAlignment(Qt.AlignCenter) # 중앙정렬
        self.table.setItem(0, 1, item) # 0번째 로우, 0번째 컬럼에 아이템을 넣겠다.

    # 서브 윈도우 띄우기
    def show_sub_window(self):
        self.sub_win = InputWindow() # 기다려주지 않는다.

        self.sub_win.emitter.connect(self.on_add_item)
        print(self.sub_win.user_info)

    def on_add_item(self, data_list=None):
        print(data_list)

        # 반복문 없이 출력하는 방법
        # row = self.ui.spinBox.value()
        # # 이름
        # item = QTableWidgetItem()
        # text = self.ui.lineEdit_name.text()
        # item.setText(text)
        # self.ui.lineEdit_name.clear()
        # self.table.setItem(int(row), 0, item)
        # # 학번
        # item = QTableWidgetItem()
        # text = self.ui.lineEdit_snum.text()
        # item.setText(text)
        # self.ui.lineEdit_snum.clear()
        # self.table.setItem(int(row), 1, item)
        # # 전공
        # item = QTableWidgetItem()
        # text = self.ui.lineEdit_major.text()
        # item.setText(text)
        # self.ui.lineEdit_major.clear()
        # self.table.setItem(int(row), 2, item)
        # # 부전공
        # item = QTableWidgetItem()
        # text = self.ui.lineEdit_minor.text()
        # item.setText(text)
        # self.ui.lineEdit_minor.clear()
        # self.table.setItem(int(row), 3, item)

        # for 반복문을 사용해서 출력하는 방법
        name = self.ui.lineEdit_name.text()
        snum = self.ui.lineEdit_snum.text()
        major = self.ui.lineEdit_major.text()
        minor = self.ui.lineEdit_minor.text()
        for idx, text in enumerate([name, snum, major, minor]):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(text)
            row = int(self.ui.spinBox.value()) -1
            col = idx
            self.table.setItem(row, col, item)

    def load_ui(self):
        ui_file_path = "/home/rapa/My_Python/My_Python0117/ui/tablewidget.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()

app = QApplication()
w = ListWidgetTest()
app.exec()
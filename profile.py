from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtWidgets import QListWidget, QLineEdit, QSpinBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

class BasicPyside6(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_ui()
        self.data_save_dic = {}

        # 콤보 박스에 넣는 내용
        self.ui.comboBox_year.addItems(str(year) for year in range(1990, 2007))

        # 취미 넘기는 버튼
        self.ui.pushButton_hb.clicked.connect(self.add_hb)
        self.ui.lineEdit_hb.returnPressed.connect(self.add_hb)
        self.ui.pushButton_save.clicked.connect(self.get_data)
    
    def add_hb(self):
        """ 라인 에딧에 있는 콤보박스로 보내는 함수 """
        text = self.ui.lineEdit_hb.text()
        self.ui.comboBox_hb.addItem(text)
        self.ui.lineEdit_hb.clear()

    def get_data(self):
        name = self.ui.lineEdit_name.text()
        mail = self.ui.lineEdit_mail.text()
        year = self.ui.comboBox_year.currentText()
        memo = self.ui.plainTextEdit.toPlainText()

        if name not in self.data_save_dic:
            # 이름
            self.data_save_dic[name] = {}
        sex = "여자"
        if self.ui.radioButton_m.isChecked():
            sex = "남자"
        print(f"성별이 {sex} 입니다.")

        self.data_save_dic[name]["생년월일"] = year
        self.data_save_dic[name]["메일"] = mail
        hobby_list = self.get_all_hob()
        self.data_save_dic[name]["취미"] = hobby_list
        if self.ui.checkBox_td.isChecked():
            self.data_save_dic[name]["위쉬리스트"] = "누워있기"
        if self.ui.checkBox_ex.isChecked():
            self.data_save_dic[name]["위쉬리스트"] = "뒹굴거리기"  
        if self.ui.checkBox_bk.isChecked():
            self.data_save_dic[name]["위쉬리스트"] = "과자먹기 ~!!!" 
        self.data_save_dic[name]["메모"] = memo
        print(self.data_save_dic)

    def get_all_hob(self):
        h = []
        count = self.ui.comboBox_hb.count()
        for i in range(count):
            text = self.ui.comboBox_hb.itemText(i)
            h.append(text)
        return h

    def load_ui(self):
        ui_file_path = "/home/rapa/My_Python/My_Python0116/profile.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()


app = QApplication()
w = BasicPyside6()
app.exec()
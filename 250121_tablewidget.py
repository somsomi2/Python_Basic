# Message Dialogue 클래스
# 간단한 팝업 메세지로 경고, 워닝, 정보등을 전달할 수 있는 커뮤니케이션 방법
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication
from PySide6.QtWidgets import QPushButton, QHeaderView, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile, Signal, Slot
""" 
아이콘 종류
QMessageBox.Question
QMessageBox.Information
QMessageBox.Warning
QMessageBox.Critical

프리셋 팝업 메세지
QMessageBox.warning(self, "Message Title", "Blablabla 하고 싶은 말~!")

"""

class InputWindow(QWidget):
    # 시그널은 객체 간의 통신을 가능하게 해주는 메커니즘
    emitter = Signal(list) # 시그널을 선언, list 타입의 데이터를 전달할 것임

    def __init__(self, row = None):
        super().__init__()

        self.row = int(row)

        # sub_tablewidget를 보여주는 경로 지정
        ui_file_path = "/home/rapa/My_Python/My_Python0121/ui/sub_tablewidget.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.subui = loader.load(ui_file) # self.subui라고 이름을 지정하고 파일을 불러오기
        self.subui.show() # self.subui.show 보여주기 -> sub_tablewidget을
        ui_file.close()


        self.subui.spinBox.setValue(self.row) # sub_tablewidge의 spinBox의 값을 row로 하겠다.

        self.subui.pushButton.clicked.connect(self.make_user_info) # sub_tablewidge의 버튼은 make_user_info와 연결된다.
    
    def make_user_info(self): # sub_tablewidget에 사용자 값 입력
        self.user_info = [] # 리스트 생성

        # 사용자 입력 내용
        name = self.subui.lineEdit_name.text()
        snum = self.subui.lineEdit_snum.text()
        major = self.subui.lineEdit_major.text()
        minor = self.subui.lineEdit_minor.text()
        row = self.subui.spinBox.value() # row는 spinBox의 값이다 = 그 값으로 저장하겠다.

        # 리스트 내부에 들어갈때 어펜드 시키기
        self.user_info.append(name)
        self.user_info.append(snum)
        self.user_info.append(major)
        self.user_info.append(minor)
        self.user_info.append(row)

        # 사용자 정의 시그널: 메서드를 통해 다른 클래스에서 GUI에 특정 값을 전달할 수 있다.
        self.emitter.emit(self.user_info) # user_info 리스트를 emitter 시그널을 통해 외부에 전달
        # self.subui.close()

class BasicPySide(QMainWindow): # 메인 윈도우 클래스 
    def __init__(self):
        super().__init__()

        self.load_ui() # tablewidget.ui를 로드할 것이다.

        self.table = self.ui.tableWidget # 변수에 self.ui.tableWidget을 할당 // 참조한다.

        # 참조한 위젯에 행과 열 생성
        self.table.setRowCount(10)
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(["이름", "학번", "전공", "부전공"]) # 헤더 라벨 생성

        # 마우스 우클릭시 메뉴버튼 뜨게하기
        self.table.setContextMenuPolicy(Qt.CustomContextMenu) # 우클릭 시 특정 동작을 할 수 있도록 설정할 수 있습니다.
        self.table.customContextMenuRequested.connect(self.show_context_menu) # 마우스 우클릭 이벤트가 발생했을 때 show_context_menu 호출

        # 컬럼의 모든 사이즈를 비율대로 자동으로 맞추는 명령!!!
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 버튼이 연결된 메서드
        self.ui.pushButton.clicked.connect(self.add_user_info)
        self.ui.pushButton_sub.clicked.connect(self.show_sub_window)

    # 마우스 우클릭시 불러오는 메서드
    def show_context_menu(self):
        # 모듈 불러오기
        from PySide6.QtWidgets import QMenu
        from PySide6.QtGui import QAction,QCursor

        self.table_menu = QMenu() # 변수명(self.table_menu)은 QMenu()이다.
        menu1 = self.table_menu.addAction("add row") # self.table_menu에 add row라는 것을 추가
        menu2 = self.table_menu.addAction("remove row")

        # 각 메뉴별로 메소드 연결
        menu1.triggered.connect(self.show_input_window)
        menu2.triggered.connect(self.remove_data)

        pos = QCursor.pos() # 마우스 커서의 위치값
        self.table_menu.move(pos) # 메뉴를 지정된 위치로 이동시키는 역할
        self.table_menu.show() # table_menu인 QMenu를 보여준다.

    # add row를 선택하면 나오는 메서드
    def show_input_window(self):

        """
        1. 서브 윈도우를 호출하는데
        2. 서브 윈도우에 위에서 만든 row를 매개변수로 전달한다.
        3. 서브 윈도우에 있는 spinBox에 row값으로 수정되게 한다. (spinBox.setValue(row))
        4. 테이블 위젯에 입력되게 한다.
        """  
        # add row를 선택하고 tableWidget에서 선택된 인덱스
        for index in self.table.selectedIndexes(): # 사용자가 여러개의 셀을 선택해도 사용할수있도록
            row = int(index.row()) + 1 # spinBox.value에 +1을 한다.
            print(row)

        self.sub_win = InputWindow(row) # self.sub_win은 위의 클래스의 spinBox.value를 가진다.
        self.sub_win.emitter.connect(self.add_user_info) # self.user_info의 값을 연결한다.

    def remove_data(self):
        """
        테이블 위젯에서 데이터를 삭제하는 방법
        1. removeRow(row) 메서드를 사용해 싹지운다.
        2. takeItem(row, col)을 이용해서 데이터를 지워준다.
        3. clear() 테이블 전체를 초기화한다.
        """
        for index in self.table.selectedIndexes(): # 
            row = index.row()
        # self.table.removeRow(row) # 행 자체를 지워버려서 추가해줘야함.

        for col in range(self.table.columnCount()):
            # 열의 갯수만큼 반복문으로 돌리기 위해 self.table.columnCount()을 사용
            self.table.takeItem(row, col) # 행과 열의 아이템을 가져간다.

    def show_sub_window(self):
        self.sub_win = InputWindow() # 기다려 주지 않는다. 위의 InputWindow()를 가져와서 emitter사용 가능
        self.sub_win.emitter.connect(self.add_user_info) # add_user_info와 연결되어 있는다.

    def add_user_info(self, data_list=None):

        if data_list:
            name = data_list[0]
            snum = data_list[1]
            major = data_list[2]
            minor = data_list[3]
            row = int(data_list[4]) -1
        else:                    
            name = self.ui.lineEdit_name.text()
            snum = self.ui.lineEdit_snum.text()
            major = self.ui.lineEdit_major.text()
            minor = self.ui.lineEdit_minor.text()
            row = int(self.ui.spinBox.value()) -1

        for idx, text in enumerate([name, snum, major, minor]): #인덱스(index)와 원소를 동시에 접근하면서 루프를 돌림
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(text)
            col = idx # col = idx이다.
            self.table.setItem(row, col, item)

    def load_ui(self):
        ui_file_path = "/home/rapa/My_Python/My_Python0121/ui/tablewidget.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()


app = QApplication()
w = BasicPySide()
app.exec()

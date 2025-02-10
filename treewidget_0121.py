from PySide6.QtWidgets import QWidget, QMainWindow, QApplication
from PySide6.QtWidgets import QPushButton, QHeaderView, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile, Signal, Slot

class BasicPySide(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_ui()
        from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

        self.tree = self.ui.treeWidget

        self.ui.pushButton.clicked.connect(self.get_sub_tree)

        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(["과일", "생산지", "가격"])

        parent_item = QTreeWidgetItem(self.tree)
        parent_item.setText(0, "준수 청과")

        item1 = QTreeWidgetItem(parent_item)
        item1.setText(0, "바나나")
        item1.setText(1, "베트남")
        item1.setText(2, "5500")

        item2 = QTreeWidgetItem(item1) #item1을 부모로 하겠다.
        item2.setText(0, "사과")
        item2.setText(1, "광주")
        item2.setText(2, "7000")

        item3 = QTreeWidgetItem(item2)
        item3.setText(0, "망고")
        item3.setText(1, "태국")
        item3.setText(2, "6000")
    
    # def get_sub_tree(self):
    #     current_item = self.tree.currentItem()

    #     for idx in range(current_item.childCount()):
    #         child = current_item.child(idx) # 선택한 아이템의 차일드중 0번째 차일드
    #         print(child.text(0))

    def get_sub_tree(self):
        """ 선택한 아이템을 재귀 함수를 호출하여 매개변수로 전달하는 함수"""
        current_item = self.tree.currentItem()
        result = self.recursive_items(current_item)
        print(result)

    def recursive_items(self, current_item):
        """ 차일드들을 찾아서 재귀를 하다가 찾으면 0번째 컬럼값을 리스트에 넣는 함수"""
        result = [current_item.text(0)]
        for idx in range(current_item.childCount()):
            child_item = current_item.child(idx)
            result.extend(self.recursive_items(child_item)) # 확장자 변수 사용
        return result

    def load_ui(self):
        ui_file_path = "/home/rapa/My_Python/My_Python0121/ui/treewidget.ui"
        ui_file = QFile(ui_file_path)
        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        self.ui.show()
        ui_file.close()


app = QApplication()
w = BasicPySide()
app.exec()

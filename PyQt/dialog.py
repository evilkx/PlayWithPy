from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class CustomDialog(QDialog):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('New Dialog')
        # Add button
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout = QVBoxLayout()
        layout.addWidget(buttonBox)
        self.setLayout(layout)


class MainDemo(QMainWindow):
    my_signal = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set title
        self.setWindowTitle('vilogy')
        label = QLabel('Press Button to dialog')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        # Add Button action
        button_action = QAction('New dialog', self)
        button_action.triggered.connect(self.onButtonClick)

        mb = self.menuBar()
        mb.setNativeMenuBar(False)
        file_menu = mb.addMenu('&File')
        file_menu.addAction(button_action)

    def onButtonClick(self, s):
        dlg = CustomDialog(self)
        dlg.exec_()



# 创建应用实例
# 通过sys.argv传入命令行参数
App = QApplication(sys.argv)
# 创建窗口实例
Demo = MainDemo()
# 显示窗口
Demo.show()
# 执行应用
# 进入事件循环
App.exec_()

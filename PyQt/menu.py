from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainDemo(QMainWindow):
    my_signal = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('vilogy')
        label = QLabel('Here is vilogy!')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # Add toolbox widget
        tb = QToolBar('Tools')
        tb.setIconSize(QSize(16, 16))
        self.addToolBar(tb)

        # Bool button action
        button_action = QAction(QIcon('keda_16.png'), 'Menu Button', self)
        button_action.setStatusTip('This is menu button')
        button_action.triggered.connect(self.onButtonClick)
        button_action.setCheckable(True)
        tb.addAction(button_action)
        self.setStatusBar(QStatusBar(self))

        # Add new menu
        button_action2 = QAction('PyQt5', self)
        button_action3 = QAction('Torch', self)
        button_action2.setCheckable(True)
        button_action3.setCheckable(True)
        button_action2.triggered.connect(self.onButtonClick)
        button_action3.triggered.connect(self.onButtonClick)

        # Menu & action
        mb = self.menuBar()
        mb.setNativeMenuBar(False)
        file_menu = mb.addMenu('&File')
        file_menu.addAction(button_action)

        # Add seperator
        file_menu.addSeparator()
        # Add secondary menu
        python_menu = file_menu.addMenu('Python')
        python_menu.addAction(button_action2)
        python_menu.addSeparator()
        python_menu.addAction(button_action3)

    def onButtonClick(self, s):
        print(s)


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

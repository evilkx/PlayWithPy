from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainDemo(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # slot函数绑定

        # 设置窗口标题
        self.setWindowTitle('TGAM rawdata wave')

        layout = QHBoxLayout()
        for i in range(5):
            button = QPushButton(str(i))
            button.pressed.connect(lambda x=i: self._my_func(x))
            layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def _my_func(self,n):
        print('Button %s pressed' % n)


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

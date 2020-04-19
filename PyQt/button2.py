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
        button = QPushButton('Click!')
        button.pressed.connect(self._click_button)
        self.my_signal.connect(self._my_func)
        self.setCentralWidget(button)

    def _click_button(self):
        self.my_signal.emit('click')
    def _my_func(self,s):
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

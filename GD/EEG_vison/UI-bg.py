# -*- coding: utf-8 -*-

# 导入程序运行必须模块
import sys_start
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入designer工具生成的login模块
from bg import Ui_begin_page
from help import Ui_help_page


class MyMainForm(QMainWindow, Ui_begin_page):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.ui_bg = Ui_begin_page()
        self.ui_bg.setupUi(self)
        self.ui_hp = Ui_help_page()
        self.ui_hp.setupUi(self)


if __name__ == "__main__":

    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys_start.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys_start.exit(app.exec_())

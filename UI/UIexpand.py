# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from expand import Ui_expand
from Test_eye import Ui_eyeTest
from Test_mus import Ui_musTest
from Test_heart import Ui_heartTest
from Test_com import Ui_comTest

class ExpandMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ex_ui = Ui_expand()
        self.ex_ui.setupUi(self)

class TestEyeWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.eye_ui = Ui_eyeTest()
        self.eye_ui.setupUi(self)

class TestMusWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mus_ui = Ui_musTest()
        self.mus_ui.setupUi(self)

class TestHeartWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.heart_ui = Ui_heartTest()
        self.heart_ui.setupUi(self)

class TestComWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.com_ui = Ui_comTest()
        self.com_ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    expand_window = ExpandMainWindow()
    eyetest_window = TestEyeWindow()
    mustest_window = TestMusWindow()
    hearttest_window = TestHeartWindow()
    comtest_window = TestComWindow()

    btn_eye = expand_window.ex_ui.ele_eye
    btn_mus = expand_window.ex_ui.ele_mus
    btn_heart = expand_window.ex_ui.ele_heart
    btn_com = expand_window.ex_ui.sys_com

    btn_eye.clicked.connect(eyetest_window.show)
    btn_mus.clicked.connect(mustest_window.show)
    btn_heart.clicked.connect(hearttest_window.show)
    btn_com.clicked.connect(comtest_window.show)

    expand_window.show()
    sys.exit(app.exec_())

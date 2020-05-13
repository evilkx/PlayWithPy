import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from UIexpand import ExpandMainWindow
from bg import Ui_begin_page
from eeg import Ui_eeg
from expand import Ui_expand
from eyetrack import Ui_eyetrack
from help import Ui_help_page
from sys_start import Ui_sys


class BeginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.bg_ui = Ui_begin_page()
        self.bg_ui.setupUi(self)


class EEGWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.eeg_ui = Ui_eeg()
        self.eeg_ui.setupUi(self)


class ExpandWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.expand_ui = Ui_expand()
        self.expand_ui.setupUi(self)


class SysWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.sys_ui = Ui_sys()
        self.sys_ui.setupUi(self)


class EyeTrackWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.eyeTrack_ui = Ui_eyetrack()
        self.eyeTrack_ui.setupUi(self)


class HelpWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.hp_ui = Ui_help_page()
        self.hp_ui.setupUi(self)


def onclickP():
    os.system("python UIexpand.py")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    begin_window = BeginWindow()
    help_window = HelpWindow()
    eeg_window = EEGWindow()
    # expand_window = ExpandWindow()
    eyeTrack_window = EyeTrackWindow()
    sys_window = SysWindow()

    btn_help = begin_window.bg_ui.btn_help
    btn_eeg = begin_window.bg_ui.btn_eeg
    # btn_expand = begin_window.bg_ui.btn_expand
    btn_eyeTrack = begin_window.bg_ui.btn_eyetracking
    btn_sys = begin_window.bg_ui.btn_start
    btn_exit = begin_window.bg_ui.btn_exit

    btn_help.clicked.connect(help_window.show)
    btn_eeg.clicked.connect(eeg_window.show)
    # btn_expand.clicked.connect(expand_window.show)
    btn_eyeTrack.clicked.connect(eyeTrack_window.show)
    btn_sys.clicked.connect(sys_window.show)
    btn_exit.clicked.connect(sys.exit)

    begin_window.show()
    sys.exit(app.exec_())

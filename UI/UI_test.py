import sys
from bg import Ui_begin_page
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from help import Ui_help_page


class BeginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.bg_ui = Ui_begin_page()
        self.bg_ui.setupUi(self)


class HelpWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.hp_ui = Ui_help_page()
        self.hp_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    begin_window = BeginWindow()
    help_window = HelpWindow()

    btn_help = begin_window.bg_ui.btn_help
    btn_help.clicked.connect(help_window.show)

    begin_window.show()
    sys.exit(app.exec_())

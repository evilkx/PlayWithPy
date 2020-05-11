# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expand.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from Test_eye import Ui_eyeTest

class Ui_expand(object):
    def setupUi(self, expand):
        expand.setObjectName("expand")
        expand.resize(341, 614)
        expand.setMinimumSize(QtCore.QSize(341, 614))
        expand.setMaximumSize(QtCore.QSize(341, 614))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        expand.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(expand)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 80, 201, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ele_eye = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ele_eye.setObjectName("ele_eye")
        self.verticalLayout.addWidget(self.ele_eye)
        self.ele_mus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ele_mus.setObjectName("ele_mus")
        self.verticalLayout.addWidget(self.ele_mus)
        self.ele_heart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ele_heart.setObjectName("ele_heart")
        self.verticalLayout.addWidget(self.ele_heart)
        self.sys_com = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sys_com.setObjectName("sys_com")
        self.verticalLayout.addWidget(self.sys_com)
        expand.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(expand)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        expand.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(expand)
        self.statusbar.setObjectName("statusbar")
        expand.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(expand)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(expand)
        self.actionSave.setObjectName("actionSave")
        self.actionRun = QtWidgets.QAction(expand)
        self.actionRun.setObjectName("actionRun")
        self.actionQ_A = QtWidgets.QAction(expand)
        self.actionQ_A.setObjectName("actionQ_A")
        self.actionInfo = QtWidgets.QAction(expand)
        self.actionInfo.setObjectName("actionInfo")
        self.actionAbout = QtWidgets.QAction(expand)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addSeparator()
        self.menu.addAction(self.actionRun)
        self.menu_3.addAction(self.actionQ_A)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionInfo)
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(expand)
        QtCore.QMetaObject.connectSlotsByName(expand)

    def retranslateUi(self, expand):
        _translate = QtCore.QCoreApplication.translate
        expand.setWindowTitle(_translate("expand", "拓展模块测试"))
        self.ele_eye.setText(_translate("expand", "眼电测试"))
        self.ele_mus.setText(_translate("expand", "肌电测试"))
        self.ele_heart.setText(_translate("expand", "心电心率测试"))
        self.sys_com.setText(_translate("expand", "通信测试"))
        self.menu.setTitle(_translate("expand", "文件"))
        self.menu_2.setTitle(_translate("expand", "视图"))
        self.menu_3.setTitle(_translate("expand", "帮助"))
        self.actionOpen.setText(_translate("expand", "Open"))
        self.actionSave.setText(_translate("expand", "Save"))
        self.actionRun.setText(_translate("expand", "Run"))
        self.actionQ_A.setText(_translate("expand", "Q&A"))
        self.actionInfo.setText(_translate("expand", "Info"))
        self.actionAbout.setText(_translate("expand", "About"))


class EyeTest_window():
    def __init__(self):
        QMainWindow.__init__(self)
        self.eye_ui = Ui_eyeTest()
        self.eye_ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exp_window = QtWidgets.QMainWindow()
    exp_ui = Ui_expand()
    exp_ui.setupUi(exp_window)

    # eyetest_window = EyeTest_window()
    # btn_eye = exp_ui.ele_eye
    # btn_eye.clicked.connect(eyetest_window.show)

    exp_window.show()
    sys.exit(app.exec_())

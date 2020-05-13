# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_begin_page(object):
    def setupUi(self, begin_page):
        begin_page.setObjectName("begin_page")
        begin_page.resize(341, 614)
        begin_page.setMinimumSize(QtCore.QSize(341, 614))
        begin_page.setMaximumSize(QtCore.QSize(341, 614))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        begin_page.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(begin_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 140, 201, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_eeg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_eeg.setObjectName("btn_eeg")
        self.verticalLayout.addWidget(self.btn_eeg)
        self.btn_eyetracking = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_eyetracking.setObjectName("btn_eyetracking")
        self.verticalLayout.addWidget(self.btn_eyetracking)
        self.btn_expand = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_expand.setObjectName("btn_expand")

        self.btn_expand.clicked.connect(self.show_expand)

        self.verticalLayout.addWidget(self.btn_expand)
        self.btn_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.verticalLayout.addWidget(self.btn_start)
        self.btn_help = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_help.setObjectName("btn_help")
        self.verticalLayout.addWidget(self.btn_help)
        self.btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.label = QtWidgets.QLabel(begin_page)
        self.label.setGeometry(QtCore.QRect(30, 90, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.img_logo = QtWidgets.QLabel(begin_page)
        self.img_logo.setGeometry(QtCore.QRect(140, 30, 51, 51))
        self.img_logo.setText("")
        self.img_logo.setTextFormat(QtCore.Qt.AutoText)
        self.img_logo.setPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setObjectName("img_logo")

        self.retranslateUi(begin_page)
        QtCore.QMetaObject.connectSlotsByName(begin_page)

    def retranslateUi(self, begin_page):
        _translate = QtCore.QCoreApplication.translate
        begin_page.setWindowTitle(_translate("begin_page", "启动页"))
        self.btn_eeg.setText(_translate("begin_page", "EEG数据采集测试"))
        self.btn_eyetracking.setText(_translate("begin_page", "Eye tracking测试"))
        self.btn_expand.setText(_translate("begin_page", "拓展模块测试"))
        self.btn_start.setText(_translate("begin_page", "进入系统"))
        self.btn_help.setText(_translate("begin_page", "帮助"))
        self.btn_exit.setText(_translate("begin_page", "退出"))
        self.label.setText(_translate("begin_page", "欢迎使用生物电及视觉感知系统"))

    def show_expand(self):
        os.system("UIexpand.py")

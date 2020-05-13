# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_mus.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

mus_flag = False

class Ui_musTest(object):
    def setupUi(self, musTest):
        musTest.setObjectName("musTest")
        musTest.resize(420, 321)
        musTest.setMinimumSize(QtCore.QSize(420, 321))
        musTest.setMaximumSize(QtCore.QSize(420, 321))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        musTest.setWindowIcon(icon)
        self.txt_rawdata = QtWidgets.QTextBrowser(musTest)
        self.txt_rawdata.setGeometry(QtCore.QRect(30, 40, 161, 241))
        self.txt_rawdata.setObjectName("txt_rawdata")
        self.txt_mus = QtWidgets.QTextBrowser(musTest)
        self.txt_mus.setGeometry(QtCore.QRect(250, 220, 121, 51))
        self.txt_mus.setObjectName("txt_mus")
        self.btn_exit = QtWidgets.QPushButton(musTest)
        self.btn_exit.setGeometry(QtCore.QRect(260, 160, 93, 28))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_start = QtWidgets.QPushButton(musTest)
        self.btn_start.setGeometry(QtCore.QRect(260, 60, 93, 28))
        self.btn_start.setObjectName("btn_start")
        self.btn_chart = QtWidgets.QPushButton(musTest)
        self.btn_chart.setGeometry(QtCore.QRect(260, 110, 93, 28))
        self.btn_chart.setObjectName("btn_chart")

        self.btn_exit.clicked.connect(self.sys_exit)
        self.btn_start.clicked.connect(self.start_musTest)

        self.retranslateUi(musTest)
        QtCore.QMetaObject.connectSlotsByName(musTest)

    def retranslateUi(self, musTest):
        _translate = QtCore.QCoreApplication.translate
        musTest.setWindowTitle(_translate("musTest", "肌电测试"))
        self.txt_mus.setHtml(_translate("musTest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">肌肉状态</p></body></html>"))
        self.btn_exit.setText(_translate("musTest", "退出"))
        self.btn_start.setText(_translate("musTest", "开始采集"))
        self.btn_chart.setText(_translate("musTest", "波形图"))

    def start_musTest(self):
        global mus_flag

        if mus_flag:
            self.btn_start.setText("开始采集")
            mus_flag = ~mus_flag
        else:
            self.btn_start.setText("停止采集")
            mus_flag = ~mus_flag
            portx = "COM3"
            bps = 19200
            ser = serial.Serial(portx, bps, timeout=None)
            while mus_flag:
                mus_data = str(ser.readlines(10)[0].decode('utf-8'))
                roll = mus_data
                self.txt_rawdata.append(mus_data)
                QApplication.processEvents()
            ser.close()

    def sys_exit(self):
        import sys
        sys.exit(self)
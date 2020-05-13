# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_heart.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

heart_flag = False

class Ui_heartTest(object):
    def setupUi(self, heartTest):
        heartTest.setObjectName("heartTest")
        heartTest.resize(420, 321)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        heartTest.setWindowIcon(icon)
        self.txt_rawdata = QtWidgets.QTextBrowser(heartTest)
        self.txt_rawdata.setGeometry(QtCore.QRect(40, 30, 161, 241))
        self.txt_rawdata.setObjectName("txt_rawdata")
        self.btn_start = QtWidgets.QPushButton(heartTest)
        self.btn_start.setGeometry(QtCore.QRect(270, 50, 93, 28))
        self.btn_start.setObjectName("btn_start")
        self.txt_mus = QtWidgets.QTextBrowser(heartTest)
        self.txt_mus.setGeometry(QtCore.QRect(260, 210, 121, 51))
        self.txt_mus.setObjectName("txt_mus")
        self.btn_exit = QtWidgets.QPushButton(heartTest)
        self.btn_exit.setGeometry(QtCore.QRect(270, 150, 93, 28))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_chart = QtWidgets.QPushButton(heartTest)
        self.btn_chart.setGeometry(QtCore.QRect(270, 100, 93, 28))
        self.btn_chart.setObjectName("btn_chart")

        self.btn_exit.clicked.connect(self.sys_exit)
        self.btn_start.clicked.connect(self.start_heartTest)

        self.retranslateUi(heartTest)
        QtCore.QMetaObject.connectSlotsByName(heartTest)

    def retranslateUi(self, heartTest):
        _translate = QtCore.QCoreApplication.translate
        heartTest.setWindowTitle(_translate("heartTest", "心电心率测试"))
        self.btn_start.setText(_translate("heartTest", "开始采集"))
        self.txt_mus.setHtml(_translate("heartTest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                     "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">心率心电</p></body></html>"))
        self.btn_exit.setText(_translate("heartTest", "退出"))
        self.btn_chart.setText(_translate("heartTest", "波形图"))

    def start_heartTest(self):
        global heart_flag

        if heart_flag:
            self.btn_start.setText("开始采集")
            heart_flag = ~heart_flag
        else:
            self.btn_start.setText("停止采集")
            heart_flag = ~heart_flag
            portx = "COM3"
            bps = 19200
            ser = serial.Serial(portx, bps, timeout=None)
            while heart_flag:
                mus_data = str(ser.readlines(10)[0].decode('utf-8'))
                roll = mus_data
                self.txt_rawdata.append(mus_data)
                QApplication.processEvents()
            ser.close()

    def sys_exit(self):
        import sys
        sys.exit(self)
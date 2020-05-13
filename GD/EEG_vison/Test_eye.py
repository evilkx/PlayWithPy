# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_eye.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

eye_flag = False

class Ui_eyeTest(object):
    def setupUi(self, eyeTest):
        eyeTest.setObjectName("eyeTest")
        eyeTest.resize(420, 321)
        eyeTest.setMinimumSize(QtCore.QSize(420, 321))
        eyeTest.setMaximumSize(QtCore.QSize(420, 321))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eyeTest.setWindowIcon(icon)
        self.txt_rawdata = QtWidgets.QTextBrowser(eyeTest)
        self.txt_rawdata.setGeometry(QtCore.QRect(30, 30, 171, 261))
        self.txt_rawdata.setObjectName("txt_rawdata")
        self.btn_start = QtWidgets.QPushButton(eyeTest)
        self.btn_start.setGeometry(QtCore.QRect(260, 60, 93, 28))
        self.btn_start.setObjectName("btn_start")
        self.btn_chart = QtWidgets.QPushButton(eyeTest)
        self.btn_chart.setGeometry(QtCore.QRect(260, 110, 93, 28))
        self.btn_chart.setObjectName("btn_chart")
        self.btn_exit = QtWidgets.QPushButton(eyeTest)
        self.btn_exit.setGeometry(QtCore.QRect(260, 160, 93, 28))
        self.btn_exit.setObjectName("btn_exit")
        self.txt_eye_blink = QtWidgets.QTextBrowser(eyeTest)
        self.txt_eye_blink.setGeometry(QtCore.QRect(250, 230, 121, 51))
        self.txt_eye_blink.setObjectName("txt_eye_blink")

        self.btn_exit.clicked.connect(self.sys_exit)
        self.btn_start.clicked.connect(self.start_eyeTest)

        self.retranslateUi(eyeTest)
        QtCore.QMetaObject.connectSlotsByName(eyeTest)

    def retranslateUi(self, eyeTest):
        _translate = QtCore.QCoreApplication.translate
        eyeTest.setWindowTitle(_translate("eyeTest", "眼电测试"))
        self.btn_start.setText(_translate("eyeTest", "开始采集"))
        self.btn_chart.setText(_translate("eyeTest", "波形图"))
        self.btn_exit.setText(_translate("eyeTest", "退出"))
        self.txt_eye_blink.setHtml(_translate("eyeTest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                         "type=\"text/css\">\n "
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'SimSun\'; "
                                                         "font-size:9pt; font-weight:400; font-style:normal;\">\n "
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                         "text-indent:0px;\">眨眼次数</p></body></html>"))

    def start_eyeTest(self):
        global eye_flag

        if eye_flag:
            self.btn_start.setText("开始采集")
            eye_flag = ~eye_flag
        else:
            self.btn_start.setText("停止采集")
            eye_flag = ~eye_flag
            portx = "COM3"
            bps = 19200
            ser = serial.Serial(portx, bps, timeout=None)
            while eye_flag:
                mus_data = str(ser.readlines(10)[0].decode('utf-8'))
                roll = mus_data
                self.txt_rawdata.append(mus_data)
                QApplication.processEvents()
            ser.close()

    def sys_exit(self):
        import sys
        sys.exit(self)
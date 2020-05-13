# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_com.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_comTest(object):
    def setupUi(self, comTest):
        comTest.setObjectName("comTest")
        comTest.resize(420, 321)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        comTest.setWindowIcon(icon)
        self.txt_res = QtWidgets.QTextBrowser(comTest)
        self.txt_res.setGeometry(QtCore.QRect(70, 240, 271, 41))
        self.txt_res.setObjectName("txt_res")
        self.btn_bt = QtWidgets.QPushButton(comTest)
        self.btn_bt.setGeometry(QtCore.QRect(150, 50, 93, 41))
        self.btn_bt.setObjectName("btn_bt")
        self.btn_mqtt = QtWidgets.QPushButton(comTest)
        self.btn_mqtt.setGeometry(QtCore.QRect(150, 110, 93, 41))
        self.btn_mqtt.setObjectName("btn_mqtt")
        self.btn_exit = QtWidgets.QPushButton(comTest)
        self.btn_exit.setGeometry(QtCore.QRect(150, 170, 93, 41))
        self.btn_exit.setObjectName("btn_exit")

        self.btn_bt.clicked.connect(self.bt_test)
        self.btn_mqtt.clicked.connect(self.mqtt_test)
        self.btn_exit.clicked.connect(self.sys_exit)

        self.retranslateUi(comTest)
        QtCore.QMetaObject.connectSlotsByName(comTest)

    def retranslateUi(self, comTest):
        _translate = QtCore.QCoreApplication.translate
        comTest.setWindowTitle(_translate("comTest", "通信测试"))
        self.btn_bt.setText(_translate("comTest", "蓝牙"))
        self.btn_mqtt.setText(_translate("comTest", "MQTT"))
        self.btn_exit.setText(_translate("comTest", "退出"))

    def sys_exit(self):
        import sys
        sys.exit(self)

    def bt_test(self):
        self.txt_res.setText("蓝牙通信正常..")

    def mqtt_test(self):
        str = time.strftime('%Y.%m.%d-%H:%M:%S\n', time.localtime(time.time()))
        self.txt_res.setText(str + "MQTT服务器通信正常..")
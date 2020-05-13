# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eeg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import time
import os
import webbrowser
import serial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

eeg_flag = False
output_data = []


def hexstr2int(data):
    # only for 1 bit data
    data_sum = 0
    for i in {0, 1}:
        if data[i] not in {'a', 'b', 'c', 'd', 'e', 'f'}:
            data_sum += pow(16, 1 - i) * int(data[i])
        elif data[i] == 'a':
            data_sum += pow(16, 1 - i) * 10
        elif data[i] == 'b':
            data_sum += pow(16, 1 - i) * 11
        elif data[i] == 'c':
            data_sum += pow(16, 1 - i) * 12
        elif data[i] == 'd':
            data_sum += pow(16, 1 - i) * 13
        elif data[i] == 'e':
            data_sum += pow(16, 1 - i) * 14
        elif data[i] == 'f':
            data_sum += pow(16, 1 - i) * 15
    return data_sum


def writeFile(rawdata):
    filename = 'D:\\Develop\\rawData\\raw_data-' + time.strftime('%Y_%m_%d-%H_%M_%S',
                                                                 time.localtime(time.time())) + '.txt'
    with open(filename, 'w') as f:
        for data in rawdata:
            f.write(data + "\n")
    f.close()
    webbrowser.open(filename)
    print(rawdata)


class Ui_eeg(object):
    def setupUi(self, eeg):
        eeg.setObjectName("eeg")
        eeg.setEnabled(True)
        eeg.resize(800, 600)
        eeg.setMinimumSize(QtCore.QSize(800, 600))
        eeg.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eeg.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(eeg)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_portx = QtWidgets.QComboBox(self.centralwidget)
        self.cb_portx.setGeometry(QtCore.QRect(70, 30, 87, 22))
        self.cb_portx.setObjectName("cb_portx")
        self.cb_portx.addItem("")
        self.cb_portx.addItem("")
        self.cb_portx.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 51, 16))
        self.label_2.setObjectName("label_2")
        self.cb_bps = QtWidgets.QComboBox(self.centralwidget)
        self.cb_bps.setGeometry(QtCore.QRect(240, 30, 87, 22))
        self.cb_bps.setObjectName("cb_bps")
        self.cb_bps.addItem("")
        self.cb_bps.addItem("")
        self.cb_bps.addItem("")
        self.cb_bps.addItem("")
        self.cb_bps.addItem("")
        self.cb_timex = QtWidgets.QComboBox(self.centralwidget)
        self.cb_timex.setGeometry(QtCore.QRect(400, 30, 87, 22))
        self.cb_timex.setObjectName("cb_timex")
        self.cb_timex.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 30, 41, 16))
        self.label_3.setObjectName("label_3")
        self.btn_start_EEG = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_EEG.setGeometry(QtCore.QRect(540, 20, 101, 41))
        self.btn_start_EEG.setObjectName("btn_start_EEG")
        self.status_LED = QtWidgets.QRadioButton(self.centralwidget)
        self.status_LED.setEnabled(False)
        self.status_LED.setGeometry(QtCore.QRect(670, 30, 115, 21))
        self.status_LED.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status_LED.setIcon(icon1)
        self.status_LED.setObjectName("status_LED")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_collect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_collect.setGeometry(QtCore.QRect(560, 160, 111, 41))
        self.btn_collect.setObjectName("btn_collect")
        self.btn_rawdata = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rawdata.setGeometry(QtCore.QRect(560, 220, 111, 41))
        self.btn_rawdata.setObjectName("btn_rawdata")
        self.txt_rawdata = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_rawdata.setGeometry(QtCore.QRect(40, 110, 381, 431))
        self.txt_rawdata.setObjectName("txt_rawdata")
        self.txt_TGAMdata = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_TGAMdata.setGeometry(QtCore.QRect(480, 300, 271, 241))
        self.txt_TGAMdata.setObjectName("txt_TGAMdata")
        eeg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(eeg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        eeg.setMenuBar(self.menubar)
        self.actionopen = QtWidgets.QAction(eeg)
        self.actionopen.setObjectName("actionopen")
        self.actionQ_A = QtWidgets.QAction(eeg)
        self.actionQ_A.setObjectName("actionQ_A")
        self.actionInfo = QtWidgets.QAction(eeg)
        self.actionInfo.setObjectName("actionInfo")
        self.actionAbout = QtWidgets.QAction(eeg)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(eeg)
        self.actionSave.setObjectName("actionSave")
        self.actionRun = QtWidgets.QAction(eeg)
        self.actionRun.setObjectName("actionRun")
        self.menu_2.addAction(self.actionQ_A)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionInfo)
        self.menu_2.addAction(self.actionAbout)
        self.menu_3.addAction(self.actionopen)
        self.menu_3.addAction(self.actionSave)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionRun)
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.btn_start_EEG.clicked.connect(self.start_EEG)
        self.btn_rawdata.clicked.connect(self.draw_rawdata)
        self.btn_collect.clicked.connect(self.seek_data)

        self.retranslateUi(eeg)
        QtCore.QMetaObject.connectSlotsByName(eeg)

    def retranslateUi(self, eeg):
        _translate = QtCore.QCoreApplication.translate
        eeg.setWindowTitle(_translate("eeg", "EEG数据采集测试"))
        eeg.setWhatsThis(_translate("eeg", "<html><head/><body><p>EEG数据采集窗口</p><p><br/></p></body></html>"))
        self.cb_portx.setItemText(0, _translate("eeg", "COM6"))
        self.cb_portx.setItemText(1, _translate("eeg", "COM5"))
        self.cb_portx.setItemText(2, _translate("eeg", "COM10"))
        self.label.setText(_translate("eeg", "串口"))
        self.label_2.setText(_translate("eeg", "波特率"))
        self.cb_bps.setItemText(0, _translate("eeg", "57600"))
        self.cb_bps.setItemText(1, _translate("eeg", "19200"))
        self.cb_bps.setItemText(2, _translate("eeg", "38400"))
        self.cb_bps.setItemText(3, _translate("eeg", "59600"))
        self.cb_bps.setItemText(4, _translate("eeg", "115200"))
        self.cb_timex.setItemText(0, _translate("eeg", "None"))
        self.label_3.setText(_translate("eeg", "超时"))
        self.btn_start_EEG.setText(_translate("eeg", "开始采集"))
        self.btn_collect.setText(_translate("eeg", "采集数据"))
        self.btn_rawdata.setText(_translate("eeg", "RawData波形图"))
        self.menu.setTitle(_translate("eeg", "视图"))
        self.menu_2.setTitle(_translate("eeg", "帮助"))
        self.menu_3.setTitle(_translate("eeg", "文件"))
        self.actionopen.setText(_translate("eeg", "Open"))
        self.actionQ_A.setText(_translate("eeg", "Q&A"))
        self.actionInfo.setText(_translate("eeg", "Info"))
        self.actionAbout.setText(_translate("eeg", "About"))
        self.actionSave.setText(_translate("eeg", "Save"))
        self.actionRun.setText(_translate("eeg", "Run"))

    def start_EEG(self):
        global eeg_flag
        global output_data
        if eeg_flag:
            eeg_flag = ~eeg_flag
            self.status_LED.setChecked(False)
            self.status_LED.setEnabled(False)
            self.cb_portx.setEnabled(True)
            self.cb_bps.setEnabled(True)
            self.cb_timex.setEnabled(True)
            self.btn_start_EEG.setText("开始采集")
            writeFile(output_data)
            self.txt_rawdata.moveCursor(QtGui.QTextCursor.End)
            # self.txt_rawdata.moveCursor(QtGui.QTextCursor.atEnd())

        else:
            eeg_flag = ~eeg_flag
            self.status_LED.setEnabled(True)
            self.status_LED.setChecked(True)
            self.cb_portx.setEnabled(False)
            self.cb_bps.setEnabled(False)
            self.cb_timex.setEnabled(False)
            self.btn_start_EEG.setText("停止采集")

            self.txt_rawdata.moveCursor(QtGui.QTextCursor.End)

            portx = self.cb_portx.currentText()
            bps = self.cb_bps.currentText()
            timex = self.cb_timex.currentText()
            now_t = time.strftime('%Y.%m.%d-%H:%M:%S\n', time.localtime(time.time()))
            str_submit = now_t + "[串口号] " + portx + " [波特率] " + bps + " [超时] " + timex
            self.txt_rawdata.append(str_submit)

            # while eeg_flag:
            #     self.txt_rawdata.append(f.readline())
            #     QApplication.processEvents()    # 关键！！

            ser = serial.Serial(portx, int(bps), timeout=None)
            self.txt_rawdata.append(str(ser))

            # while eeg_flag:
            #     rawdata = str(get_rawdata(ser))
            #     if rawdata != 'None':
            #         self.txt_rawdata.append(str(get_rawdata(ser)))
            #         QApplication.processEvents()

            while eeg_flag:
                if hexstr2int(ser.read().hex()) == 0xAA:
                    if hexstr2int(ser.read().hex()) == 0xAA:
                        temp = hexstr2int(ser.read().hex())
                        if temp == 0x04:
                            # small packet
                            check1 = hexstr2int(ser.read().hex())  # guess 0x80
                            check2 = hexstr2int(ser.read().hex())  # guess 0x02
                            s_high = hexstr2int(ser.read().hex())  # raw data HighBit
                            s_low = hexstr2int(ser.read().hex())  # raw data LowBit
                            s_checksum = hexstr2int(ser.read().hex())  # checksum to check
                            s_sum = ~(check1 + check2 + s_high + s_low) & 255  # FFFFFFFF = 4294967295     FF = 255
                            if s_sum == s_checksum:
                                rawdata = (s_high << 8) | s_low
                                if (rawdata > 32768):
                                    rawdata -= 65536
                                    output_data.append(str(rawdata))
                                    # print(output_data)
                                    # writeFile(output_data)
                                    self.txt_rawdata.append(str(rawdata))
                                    QApplication.processEvents()  # kernel

            # while eeg_flag:
            #     rawdata = self.get_rawdata()
            #     self.txt_rawdata.append(rawdata)
            # time.sleep(1000)
            # self.txt_rawdata.append("world")

    def draw_rawdata(self):
        # fileName, filetype = QFileDialog.getOpenFileName(self,
        #                                                  "选取文件",
        #                                                  "./",
        #                                                  "Text Files (*.txt);;All Files (*)")  # 设置文件扩展名过滤,注意用双分号间隔
        # print(fileName, filetype)
        # QApplication.processEvents()
        os.system("python pygraph.py")

    def writeFile(self):
        global output_data
        # filename = 'D:\\Develop\\rawData\\raw_data-' + time.strftime('%Y_%m_%d-%H_%M_%S', time.localtime(time.time())) + '.txt'
        # with open(filename, 'w') as f:
        #     for data in rawdata:
        #         f.write(data + "\n")
        # f.close()
        # webbrowser.open(filename)
        print(output_data)

    def seek_data(self):
        # global output_data
        # with open(filename, 'w') as f:
        #     f.write(output_data)
        #     QApplication.processEvents()
        webbrowser.open("D:\\Develop\\rawData")

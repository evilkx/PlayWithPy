# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sys_start.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import webbrowser
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

start_flag = False

class Ui_sys(object):
    def setupUi(self, sys):
        sys.setObjectName("sys")
        sys.resize(980, 616)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sys.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(sys)
        self.centralwidget.setObjectName("centralwidget")
        self.label_eye_tracking = QtWidgets.QLabel(self.centralwidget)
        self.label_eye_tracking.setGeometry(QtCore.QRect(700, 50, 241, 161))
        self.label_eye_tracking.setAutoFillBackground(True)
        self.label_eye_tracking.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eye_tracking.setObjectName("label_eye_tracking")
        self.dial_eye_direction = QtWidgets.QDial(self.centralwidget)
        self.dial_eye_direction.setGeometry(QtCore.QRect(760, 310, 121, 111))
        self.dial_eye_direction.setObjectName("dial_eye_direction")
        self.Slider_eye_distance = QtWidgets.QSlider(self.centralwidget)
        self.Slider_eye_distance.setGeometry(QtCore.QRect(710, 260, 221, 22))
        self.Slider_eye_distance.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_eye_distance.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Slider_eye_distance.setObjectName("Slider_eye_distance")
        self.btn_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_set.setGeometry(QtCore.QRect(770, 460, 101, 41))
        self.btn_set.setObjectName("btn_set")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(640, 10, 16, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(770, 510, 101, 41))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_openSSVEP = QtWidgets.QPushButton(self.centralwidget)
        self.btn_openSSVEP.setGeometry(QtCore.QRect(100, 510, 111, 41))
        self.btn_openSSVEP.setObjectName("btn_openSSVEP")
        self.btn_chart = QtWidgets.QPushButton(self.centralwidget)
        self.btn_chart.setGeometry(QtCore.QRect(230, 510, 111, 41))
        self.btn_chart.setObjectName("btn_chart")
        self.txt_rawdata = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_rawdata.setGeometry(QtCore.QRect(50, 50, 341, 431))
        self.txt_rawdata.setObjectName("txt_rawdata")
        self.txt_command = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_command.setGeometry(QtCore.QRect(430, 50, 141, 431))
        self.txt_command.setObjectName("txt_command")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(450, 510, 101, 41))
        self.btn_start.setObjectName("btn_start")
        self.label_rawdata = QtWidgets.QLabel(self.centralwidget)
        self.label_rawdata.setGeometry(QtCore.QRect(180, 20, 101, 16))
        self.label_rawdata.setObjectName("label_rawdata")
        self.label_commands = QtWidgets.QLabel(self.centralwidget)
        self.label_commands.setGeometry(QtCore.QRect(470, 20, 71, 16))
        self.label_commands.setObjectName("label_commands")
        sys.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sys)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        sys.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(sys)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(sys)
        self.actionSave.setObjectName("actionSave")
        self.actionRun = QtWidgets.QAction(sys)
        self.actionRun.setObjectName("actionRun")
        self.actionQ_A = QtWidgets.QAction(sys)
        self.actionQ_A.setObjectName("actionQ_A")
        self.actionInfo = QtWidgets.QAction(sys)
        self.actionInfo.setObjectName("actionInfo")
        self.actionAbout = QtWidgets.QAction(sys)
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

        self.btn_start.clicked.connect(self.show_rawdata)
        self.btn_openSSVEP.clicked.connect(self.open_ssvep)
        self.btn_exit.clicked.connect(self.sys_exit)

        self.retranslateUi(sys)
        QtCore.QMetaObject.connectSlotsByName(sys)

    def retranslateUi(self, sys):
        _translate = QtCore.QCoreApplication.translate
        sys.setWindowTitle(_translate("sys", "生物电及视觉感知系统"))
        self.label_eye_tracking.setText(_translate("sys", "eye_tracking"))
        self.btn_set.setText(_translate("sys", "设置"))
        self.btn_exit.setText(_translate("sys", "退出"))
        self.btn_openSSVEP.setText(_translate("sys", "SSVEP刺激器"))
        self.btn_chart.setText(_translate("sys", "波形图"))
        self.btn_start.setText(_translate("sys", "开始采集"))
        self.label_rawdata.setText(_translate("sys", "原始数据记录"))
        self.label_commands.setText(_translate("sys", "交互指令"))
        self.menu.setTitle(_translate("sys", "文件"))
        self.menu_2.setTitle(_translate("sys", "视图"))
        self.menu_3.setTitle(_translate("sys", "帮助"))
        self.actionOpen.setText(_translate("sys", "Open"))
        self.actionSave.setText(_translate("sys", "Save"))
        self.actionRun.setText(_translate("sys", "Run"))
        self.actionQ_A.setText(_translate("sys", "Q&A"))
        self.actionInfo.setText(_translate("sys", "Info"))
        self.actionAbout.setText(_translate("sys", "About"))

    def open_ssvep(self):
        webbrowser.open("https://omids.github.io/quickssvep/?setup=%257B%2522ver%2522%253A1%252C%2522boxes%2522%253A"
                        "%255B%257B%2522f%2522%253A%25227%2522%252C%2522text%2522%253A%2522A%2522%257D%252C%257B"
                        "%2522f%2522%253A%25228%2522%252C%2522text%2522%253A%2522B%2522%257D%252C%257B%2522f%2522"
                        "%253A%25229%2522%252C%2522text%2522%253A%2522C%2522%257D%252C%257B%2522f%2522%253A%252210"
                        "%2522%252C%2522text%2522%253A%2522D%2522%257D%252C%257B%2522f%2522%253A%252211%2522%252C"
                        "%2522text%2522%253A%2522E%2522%257D%252C%257B%2522f%2522%253A%252212%2522%252C%2522text%2522"
                        "%253A%2522F%2522%257D%252C%257B%2522f%2522%253A%252213%2522%252C%2522text%2522%253A%2522G"
                        "%2522%257D%252C%257B%2522f%2522%253A%252214%2522%252C%2522text%2522%253A%2522H%2522%257D"
                        "%252C%257B%2522f%2522%253A%252215%2522%252C%2522text%2522%253A%2522I%2522%257D%252C%257B"
                        "%2522f%2522%253A%252216%2522%252C%2522text%2522%253A%2522J%2522%257D%252C%257B%2522f%2522"
                        "%253A%252217%2522%252C%2522text%2522%253A%2522K%2522%257D%252C%257B%2522f%2522%253A%252218"
                        "%2522%252C%2522text%2522%253A%2522L%2522%257D%255D%252C%2522boxOpts%2522%253A%257B"
                        "%2522showInfo%2522%253Atrue%252C%2522showEdit%2522%253Afalse%252C%2522flickerText%2522"
                        "%253Afalse%252C%2522fBackLoop%2522%253Afalse%252C%2522infos%2522%253A%257B%2522curF%2522"
                        "%253Atrue%252C%2522avgF%2522%253Atrue%252C%2522rangeF%2522%253Afalse%252C%2522curPer%2522"
                        "%253Afalse%252C%2522curDuty%2522%253Afalse%257D%257D%252C%2522options%2522%253A%257B"
                        "%2522cols%2522%253A4%252C%2522fontS%2522%253A1%252C%2522fontB%2522%253Atrue%252C"
                        "%2522duration%2522%253Anull%257D%257D")

    def show_rawdata(self):
        global start_flag

        if start_flag:
            self.btn_start.setText("开始采集")
            start_flag = ~start_flag
        else:
            self.btn_start.setText("停止采集")
            start_flag = ~start_flag
            self.label_eye_tracking.setPixmap(QtGui.QPixmap("D:\\Develop\\4C-res\\img_eye_sys.png"))
            self.txt_rawdata.append("脑电模块连接正常...")
            self.txt_rawdata.append("拓展-心电模块连接正常...")
            self.txt_rawdata.append("拓展-肌电模块连接正常...")
            self.txt_rawdata.append("拓展-眼电模块连接正常...")
            self.txt_rawdata.append("摄像头(cam0)连接正常...")
            self.txt_rawdata.append("蓝牙模块连接正常...")

            self.txt_command.append("眨眼\\n眨眼\\n置位\\n眼动-左\\")

            portx = "COM3"
            bps = 19200
            ser = serial.Serial(portx, bps, timeout=None)
            while start_flag:
                imu_data = str(ser.readlines(10)[0].decode('utf-8'))
                roll = imu_data
                self.txt_rawdata.append(imu_data)
                QApplication.processEvents()

    def sys_exit(self):
        import sys
        sys.exit(self)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eyetrack.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import cv2


class Ui_eyetrack(object):
    # def __init__(self, parent=None):
    #     super(Ui_eyetrack, self).__init__(parent)
    #
    #     self.timer_camera = QtCore.QTimer()  # 初始化定时器
    #     self.cap = cv2.VideoCapture()  # 初始化摄像头
    #     self.CAM_NUM = 0
    #     self.setupUi()
    #     self.slot_init()
    #     self.__flag_work = 0
    #     self.x = 0
    #     self.count = 0

    def setupUi(self, eyetrack):
        eyetrack.setObjectName("eyetrack")
        eyetrack.resize(800, 610)
        eyetrack.setMinimumSize(QtCore.QSize(800, 610))
        eyetrack.setMaximumSize(QtCore.QSize(800, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eyetrack.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(eyetrack)
        self.centralwidget.setObjectName("centralwidget")
        self.img_threshold = QtWidgets.QLabel(self.centralwidget)
        self.img_threshold.setGeometry(QtCore.QRect(130, 50, 211, 171))
        self.img_threshold.setAutoFillBackground(True)
        self.img_threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.img_threshold.setObjectName("img_threshold")
        self.img_track = QtWidgets.QLabel(self.centralwidget)
        self.img_track.setGeometry(QtCore.QRect(460, 50, 211, 171))
        self.img_track.setAutoFillBackground(True)
        self.img_track.setAlignment(QtCore.Qt.AlignCenter)
        self.img_track.setObjectName("img_track")
        self.sld_Threshold = QtWidgets.QSlider(self.centralwidget)
        self.sld_Threshold.setGeometry(QtCore.QRect(210, 320, 371, 22))
        self.sld_Threshold.setAutoFillBackground(True)
        self.sld_Threshold.setOrientation(QtCore.Qt.Horizontal)
        self.sld_Threshold.setObjectName("sld_Threshold")
        self.label_bar = QtWidgets.QLabel(self.centralwidget)
        self.label_bar.setGeometry(QtCore.QRect(380, 290, 81, 16))
        self.label_bar.setObjectName("label_bar")
        self.btn_opencam = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opencam.setGeometry(QtCore.QRect(202, 490, 111, 41))
        self.btn_opencam.setObjectName("btn_opencam")
        self.btn_save_threshold = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_threshold.setGeometry(QtCore.QRect(350, 490, 111, 41))
        self.btn_save_threshold.setObjectName("btn_save_threshold")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(500, 490, 111, 41))
        self.btn_exit.setObjectName("exit")
        eyetrack.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(eyetrack)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        eyetrack.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(eyetrack)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(eyetrack)
        self.actionSave.setObjectName("actionSave")
        self.actionRun = QtWidgets.QAction(eyetrack)
        self.actionRun.setObjectName("actionRun")
        self.actionQA = QtWidgets.QAction(eyetrack)
        self.actionQA.setObjectName("actionQA")
        self.actionInfo = QtWidgets.QAction(eyetrack)
        self.actionInfo.setObjectName("actionInfo")
        self.actionAbout = QtWidgets.QAction(eyetrack)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addSeparator()
        self.menu.addAction(self.actionRun)
        self.menu_3.addAction(self.actionQA)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionInfo)
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.btn_exit.clicked.connect(self.sys_exit)
        self.btn_opencam.clicked.connect(self.open_cam)
        # self.btn_save_threshold.clicked.connect()
        self.sld_Threshold.valueChanged.connect(self.slider_change)

        self.retranslateUi(eyetrack)
        QtCore.QMetaObject.connectSlotsByName(eyetrack)

    def retranslateUi(self, eyetrack):
        _translate = QtCore.QCoreApplication.translate
        eyetrack.setWindowTitle(_translate("eyetrack", "Eye Tracking测试"))
        self.img_threshold.setText(_translate("eyetrack", "gray_image"))
        self.img_track.setText(_translate("eyetrack", "eye_track"))
        self.label_bar.setText(_translate("eyetrack", "阈值"))
        self.btn_opencam.setText(_translate("eyetrack", "打开相机"))
        self.btn_save_threshold.setText(_translate("eyetrack", "保存阈值"))
        self.btn_exit.setText(_translate("eyetrack", "退出"))
        self.menu.setTitle(_translate("eyetrack", "文件"))
        self.menu_2.setTitle(_translate("eyetrack", "视图"))
        self.menu_3.setTitle(_translate("eyetrack", "帮助"))
        self.actionOpen.setText(_translate("eyetrack", "Open"))
        self.actionSave.setText(_translate("eyetrack", "Save"))
        self.actionRun.setText(_translate("eyetrack", "Run"))
        self.actionQA.setText(_translate("eyetrack", "Q&A"))
        self.actionInfo.setText(_translate("eyetrack", "Info"))
        self.actionAbout.setText(_translate("eyetrack", "About"))

    # def slot_init(self):  # 建立通信连接
    #     self.button_open_camera.clicked.connect(self.button_open_camera_click)
    #     self.timer_camera.timeout.connect(self.show_camera)
    #     self.button_close.clicked.connect(self.close)
    #
    # def button_open_camera_click(self):
    #     if self.timer_camera.isActive() == False:
    #         flag = self.cap.open(self.CAM_NUM)
    #         if flag == False:
    #             msg = QtWidgets.QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
    #                                                 buttons=QtWidgets.QMessageBox.Ok,
    #                                                 defaultButton=QtWidgets.QMessageBox.Ok)
    #             # if msg==QtGui.QMessageBox.Cancel:
    #             #                     pass
    #         else:
    #             self.timer_camera.start(30)
    #             self.btn_opencam.setText(u'关闭相机')
    #     else:
    #         self.timer_camera.stop()
    #         self.cap.release()
    #         self.img_threshold.clear()
    #         self.btn_opencam.setText(u'打开相机')
    #
    # def show_camera(self):
    #     flag, self.image = self.cap.read()
    #     show = cv2.resize(self.image, (640, 480))
    #     show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
    #     showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
    #     self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    # def closeEvent(self):
    #     ok = QtWidgets.QPushButton()
    #     cancel = QtWidgets.QPushButton()
    #     msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'关闭', u'是否关闭！')
    #     msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
    #     msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
    #     ok.setText(u'确定')
    #     cancel.setText(u'取消')
    #     if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
    #         self.ignore()
    #     else:
    #         self.accept()
    #     QApplication.processEvents()

    def slider_change(self):
        var = self.sld_Threshold.value()
        self.label_bar.setText("阈值: " + str(var))

    def open_cam(self):
        self.img_threshold.setPixmap(QtGui.QPixmap("D:\\Develop\\4C-res\\img_gray.png"))
        self.img_track.setPixmap(QtGui.QPixmap("D:\\Develop\\4C-res\\img_track.png"))

    def sys_exit(self):
        import sys
        sys.exit(self)
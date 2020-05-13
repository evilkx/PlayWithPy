# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_page(object):
    def setupUi(self, help_page):
        help_page.setObjectName("help_page")
        help_page.resize(800, 600)
        help_page.setMinimumSize(QtCore.QSize(800, 600))
        help_page.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MI/Downloads/brain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        help_page.setWindowIcon(icon)
        self.txt_help = QtWidgets.QTextBrowser(help_page)
        self.txt_help.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.txt_help.setOpenExternalLinks(True)
        self.txt_help.setOpenLinks(True)
        self.txt_help.setObjectName("txt_help")

        self.retranslateUi(help_page)
        QtCore.QMetaObject.connectSlotsByName(help_page)

    def retranslateUi(self, help_page):
        _translate = QtCore.QCoreApplication.translate
        help_page.setWindowTitle(_translate("help_page", "帮助文档"))
        self.txt_help.setHtml(_translate("help_page", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>Readme</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"write\"></a><span style=\" font-size:x-large; font-weight:600;\">e</span><span style=\" font-size:x-large; font-weight:600;\">yeLike</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An OpenCV based webcam gaze tracker based on a simple image gradient-based eye center algorithm by Fabian Timm.</p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"disclaimer\"></a><span style=\" font-size:x-large; font-weight:600;\">D</span><span style=\" font-size:x-large; font-weight:600;\">ISCLAIMER</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">This does not track gaze yet.</span> It is basically just a developer reference implementation of Fabian Timm\'s algorithm that shows some debugging windows with points on your pupils.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want cheap gaze tracking and don\'t mind hardware check out <a href=\"https://theeyetribe.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">The Eye Tribe</span></a>. If you want webcam-based eye tracking contact <a href=\"http://xlabsgaze.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Xlabs</span></a> or use their chrome plugin and SDK. If you\'re looking for open source your only real bet is <a href=\"http://pupil-labs.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Pupil</span></a> but that requires an expensive hardware headset.</p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"status\"></a><span style=\" font-size:x-large; font-weight:600;\">S</span><span style=\" font-size:x-large; font-weight:600;\">tatus</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The eye center tracking works well but I don\'t have a reference point like eye corner yet so it can\'t actually track where the user is looking.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If anyone with more experience than me has ideas on how to effectively track a reference point or head pose so that the gaze point on the screen can be calculated contact me.</p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"building\"></a><span style=\" font-size:x-large; font-weight:600;\">B</span><span style=\" font-size:x-large; font-weight:600;\">uilding</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CMake is required to build eyeLike.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"osx-or-linux-with-make\"></a><span style=\" font-size:large; font-weight:600;\">O</span><span style=\" font-size:large; font-weight:600;\">SX or Linux with Make</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\"># do things in the build directory so that we don\'t clog up the main directory</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">mkdir build</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">cd build</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">cmake ../</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">make</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">./bin/eyeLike # the executable file</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"on-osx-with-xcode\"></a><span style=\" font-size:large; font-weight:600;\">O</span><span style=\" font-size:large; font-weight:600;\">n OSX with XCode</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">xxxxxxxxxx</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">mkdir build</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\';\">./cmakeBuild.sh</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">then open the XCode project in the build folder and run from there.</p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"on-windows\"></a><span style=\" font-size:large; font-weight:600;\">O</span><span style=\" font-size:large; font-weight:600;\">n Windows</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There is some way to use CMake on Windows but I am not familiar with it.</p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"blog-article\"></a><span style=\" font-size:x-large; font-weight:600;\">B</span><span style=\" font-size:x-large; font-weight:600;\">log Article:</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://thume.ca/projects/2012/11/04/simple-accurate-eye-center-tracking-in-opencv/\"><span style=\" text-decoration: underline; color:#0000ff;\">Using Fabian Timm\'s Algorithm</span></a></li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"paper\"></a><span style=\" font-size:x-large; font-weight:600;\">P</span><span style=\" font-size:x-large; font-weight:600;\">aper:</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Timm and Barth. Accurate eye centre localisation by means of gradients. In Proceedings of the Int. Conference on Computer Theory and Applications (VISAPP), volume 1, pages 125-130, Algarve, Portugal,</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">INSTICC.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(also see youtube video at <a href=\"http://www.youtube.com/watch?feature=player_embedded&amp;amp;v=aGmGyFLQAFM\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.youtube.com/watch?feature=player_embedded&amp;v=aGmGyFLQAFM</span></a>)</p></body></html>"))

# -*- coding: utf-8 -*- #
# import pyqtgraph.examples as pge
# pge.run()
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import serial  # pyserial
import pyqtgraph as pg
import numpy as np
import array


app = pg.mkQApp()

data = array.array('d')
N = 200
win = pg.GraphicsWindow()
win.setWindowTitle('EEG Raw Data')
# win.resize(500, 300)
win.resize(1280, 720)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0, N-1], yRange=[-500, 1500], padding=0)
p.setLabels(left='y / rawdata', bottom='x / point', title='EEG RawData 采集')

curve = p.plot(pen='g')
idx = 0
rawdata = 0


def open_file_dialog():
    fileName, fileType = QFileDialog.getOpenFileName(0,
                                                     "选取文件",
                                                     r"F:\autoTest\20181015_Cases",
                                                     "Text Files (*.txt);;Text Files (*.xlsx;*.xls);;")  # 设置文件扩展名过滤

    fileName = fileName.replace('/', '\\')  # windows下需要进行文件分隔符转换
    return (fileName)

# filename = open_file_dialog()
# file = open(filename)
file = open('D:\\Develop\\rawData\\raw_data-2020_05_10-10_34_32.txt')


def plotData():
    global idx
    global file
    line = file.readline()
    tmp = int(line)+1024
    # tmp = np.sin(np.pi / 50 * idx)      # y
    if len(data) < N:
        data.append(tmp)
    else:
        data[:-1] = data[1:]
        data[-1] = tmp

    curve.setData(data)
    idx += 1


timer = pg.QtCore.QTimer()
timer.timeout.connect(plotData)
timer.start(30)

app.exec_()
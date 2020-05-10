# -*- coding: utf-8 -*- #
# import pyqtgraph.examples as pge
# pge.run()

import pyqtgraph as pg
import numpy as np
import array


app = pg.mkQApp()

data = array.array('d')
N = 200
win = pg.GraphicsWindow()
win.setWindowTitle('EEG Raw Data')
win.resize(500, 300)
# win.resize(1280, 720)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0, N-1], yRange=[-500, 1500], padding=0)
p.setLabels(left='y / V', bottom='x / point', title='EEG RawData 采集')

curve = p.plot(pen='y')
idx = 0
file = open('self\\rawdata.txt')

def plotData():
    global idx
    global file
    line = file.readline()
    tmp = int(line)+1024
    # tmp = np.sin(np.pi / 50 * idx)      # y
    if len(data)<N:
        data.append(tmp)
    else:
        data[:-1] = data[1:]
        data[-1] = tmp

    curve.setData(data)
    idx += 1

timer = pg.QtCore.QTimer()
timer.timeout.connect(plotData)
timer.start(5)

app.exec_()

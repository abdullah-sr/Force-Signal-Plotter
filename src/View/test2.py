# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from __future__ import unicode_literals
import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from numpy import arange, sin, pi
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    # def compute_initial_figure(self):
    #     pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]

        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setLineWidth(1)
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(8)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # #self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        #self.actionQuit.setShortcut("q")


        # l = QtWidgets.QVBoxLayout(self.centralwidget)
        # sc = MyStaticMplCanvas(self.centralwidget, width=5, height=4, dpi=100)
        # dc = MyDynamicMplCanvas(self.centralwidget, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        # l.addWidget(dc)

        #self.centralwidget.setFocus()
        #self.setCentralWidget(self.centralwidget)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.actionExit = QtGui.QAction(TalkWindow)
        # self.actionExit.setObjectName("actionExit")
        # self.menuFile.addAction(self.actionExit)
        # self.exitAct = QtWidgets.QAction(self.tr("E&xit;"), self)
        # self.exitAct.setShortcut(self.tr("Ctrl+Q"))
        # self.exitAct.setStatusTip(self.tr("Exit the application"))


        # self.connectNotify(self.actionQuit, QtWidgets.SIGNAL("triggered()"), self, self.actionQuit)
        # self.connect(self.exitAct, SIGNAL("triggered()"), self, SLOT("close()"))
        self.actionQuit.triggered.connect(self.fileQuit)

        #self.actionAbout.triggered.connect(())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "Treadmill"))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "1"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "2"))
        # item = self.tableWidget.verticalHeaderItem(2)
        # item.setText(_translate("MainWindow", "3"))
        # item = self.tableWidget.verticalHeaderItem(3)
        # item.setText(_translate("MainWindow", "5"))
        # item = self.tableWidget.verticalHeaderItem(4)
        # item.setText(_translate("MainWindow", "6"))
        # item = self.tableWidget.verticalHeaderItem(5)
        # item.setText(_translate("MainWindow", "7"))
        # item = self.tableWidget.verticalHeaderItem(6)
        # item.setText(_translate("MainWindow", "8"))
        # item = self.tableWidget.verticalHeaderItem(7)
        # item.setText(_translate("MainWindow", "10"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "Time"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "x"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("MainWindow", "y"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("MainWindow", "z"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

        #self.actionQuit.







        # self.actionQuit = QtGui.QAction(self)
        # self.actionQuit.setObjectName("actionExit")
        # self.menuFile.addAction(self.actionQuit)
        # self.menubar.addAction(self.menuFile.menuAction())

        #QtCore.QObject.connectNotify(self.actionQuit, QtCore.pyqtBoundSignal("activated()"), self.close)
       # self.actionQuit.setText(QtGui.QApplication.translate("TalkWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))


    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Q:
            self.close
            self.fileQuit



    def fileQuit(self):
        self.closeEvent()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

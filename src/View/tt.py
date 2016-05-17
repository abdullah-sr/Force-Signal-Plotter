from PyQt5 import QtCore, QtGui, QtWidgets
import random

import operator
import threading
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time

class MyWindow(QtWidgets.QWidget):
    def __init__(self, data_list, header, *args):
        QtWidgets.QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("Click on column title to sort")
        table_model = MyTableModel(self, data_list, header)
        table_view = QtWidgets.QTableView()
        table_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 14)
        table_view.setFont(font)
        # set column width to fit contents (set font first!)
        table_view.resizeColumnsToContents()
        # enable sorting
        #table_view.setSortingEnabled(True)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        self.count = 0
        self.timer = QTimer()
        #self.timer.setInterval(1)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timerHit)
        threading._start_new_thread(self.updateData, ())

    def timerHit(self):
        #print(QTime.currentTime().toString())
        topLeft = self.createIndex(0,0)
        bottomRight = self.createIndex(self.rowCount(self),self.rowCount(self))
        self.dataChanged.emit(topLeft,bottomRight)

    def rowCount(self, parent):
        return 10
    def columnCount(self, parent):
        return len(self.mylist[0])



    def data(self, index, role):
        self.count +=1
        #print(self.count)
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        elif index.row() >= len(self.mylist):
            return None
        return self.mylist[index.row()][index.column()]

    # reterns the headers specified in header[]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None


    def updateData(self):
        while True:
            time.sleep(5)
            self.mylist.append(('n', 50))
            print("added")



header = ['Time', 'Force']
    # use numbers for numeric data to sort properly
data_list = [
    ('ACETIC ACID', 50)
    ]




if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    win = MyWindow(data_list, header)
    win.show()
    app.exec_()
_())
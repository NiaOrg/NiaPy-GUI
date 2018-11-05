# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, uic, QtWidgets
from NiaPy.algorithms.basic import *
from NiaPy.benchmarks import *
#from Settings import _Settings

Ui_MainWindow, QtBaseClass = uic.loadUiType('ui/main.ui')

ALGORITHMS = []
BENCHMARKS = []

for item in dir():
    if "Algorithm" in item:
        ALGORITHMS.append(item)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        for algorithm in ALGORITHMS:
            self.comboBoxAlgorithms.addItem(algorithm)

        for benchmark in BENCHMARKS:
            self.comboBoxBenchmarks.addItem(benchmark)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

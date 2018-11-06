# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys, inspect, re
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from NiaPy.algorithms.basic import *
from NiaPy.benchmarks import *

#from Settings import _Settings

Ui_MainWindow, QtBaseClass = uic.loadUiType('ui/main.ui')

ALGORITHMS = []
BENCHMARKS = []

for item in inspect.getmembers(sys.modules['NiaPy.algorithms.basic'], inspect.isclass):
    ALGORITHMS.append(re.sub(r'\B([A-Z])', r' \1', item[0]))

for item in inspect.getmembers(sys.modules['NiaPy.algorithms.modified'], inspect.isclass):
    ALGORITHMS.append(re.sub(r'\B([A-Z])', r' \1', item[0]))

for item in inspect.getmembers(sys.modules['NiaPy.benchmarks'], inspect.isclass):
    BENCHMARKS.append(re.sub(r'\B([A-Z])', r' \1', item[0]))


class NiaPyGUI(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        for algorithm in ALGORITHMS:
            self.comboBoxAlgorithms.addItem(algorithm)

        for benchmark in BENCHMARKS:
            self.comboBoxBenchmarks.addItem(benchmark)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NiaPyGUI()
    window.show()

    # enable killing the app with ctrl-c keypress
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    sys.exit(app.exec_())

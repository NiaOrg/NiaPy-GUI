# -*- coding: utf-8 -*-
import importlib
import io
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import niapy
from niapy.algorithms.basic import *
from niapy.algorithms.modified import *
from niapy.task import Task
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import matplotlib
matplotlib.use('Agg')

Ui_MainWindow, QtBaseClass = uic.loadUiType('uis/main.ui')

ALGOCLASSES = niapy.algorithms.Algorithm.__subclasses__()
BENCHCLASSES = niapy.problems.Problem.__subclasses__()

def show_benchmark_function(latex_code):
    buf = io.BytesIO()
    plt.rc('text.latex', preamble = r'\usepackage{amsmath}')
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0.05, 0.5, latex_code.replace('\n',''), size=10)
    plt.savefig(buf, format='png')
    plt.close()

    back = (255, 255, 255, 255)

    im = Image.open(buf)
    bg = Image.new(im.mode, im.size, back)
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    return im.crop(bbox)

class NiaPyGUI(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        for algo in ALGOCLASSES:
            self.comboBoxAlgorithms.addItem(algo.Name[0] + ' (' + algo.Name[1] + ')', algo)
        for bench in BENCHCLASSES:
            self.comboBoxBenchmarks.addItem(bench.__name__, bench.__name__)
        self.pushButton.clicked.connect(self.run_algorithm)
        self.comboBoxBenchmarks.currentIndexChanged.connect(self.selection_change)

    def selection_change(self, i):
        bench = self.comboBoxBenchmarks.itemData(
            self.comboBoxBenchmarks.currentIndex())
        show_benchmark_function(bench.latex_code()).save("benchmark_function.png")
        self.label.setPixmap(QtGui.QPixmap("benchmark_function.png"))

    @pyqtSlot()
    def run_algorithm(self):
        algo = self.comboBoxAlgorithms.itemData(
            self.comboBoxAlgorithms.currentIndex())
        bench = self.comboBoxBenchmarks.itemData(
            self.comboBoxBenchmarks.currentIndex())
        task = Task(D=10, nFES=1000, benchmark=bench())
        best = algo().run(task=task)
        self.label_4.setText(str(best))

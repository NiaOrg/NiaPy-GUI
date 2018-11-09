# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')

from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from NiaPy.algorithms.basic import *
from NiaPy.benchmarks import *
import matplotlib.pyplot as plt
from PIL import Image, ImageChops
import io
import importlib

Ui_MainWindow, QtBaseClass = uic.loadUiType('ui/main.ui')

ALGORITHMS = []
BENCHMARKS = sorted(['Rastrigin', 'Rosenbrock', 'Griewank', 'ExpandedGriewankPlusRosenbrock', 'Sphere', 'Ackley', 'Schwefel', 'Schwefel221', 'Schwefel222', 'ModifiedSchwefel', 'Whitley', 'Alpine1', 'Alpine2', 'HappyCat', 'Ridge', 'ChungReynolds', 'Csendes', 'Pinter','Qing', 'Quintic', 'Salomon', 'SchumerSteiglitz', 'Step', 'Step2','Step3', 'Stepint', 'SumSquares', 'StyblinskiTang', 'BentCigar', 'Weierstrass', 'HGBat', 'Katsuura','Elliptic','Discus','Michalewichz','Levy','Sphere','Sphere2','Sphere3','Trid','Perm','Zakharov','DixonPrice','Powell','CosineMixture','ExpandedSchaffer','SchafferN2','SchafferN4'])
    
for item in dir():
    if "Algorithm" in item:
        ALGORITHMS.append(item)
        
def show_benchmark_function(latex_code):
        buf = io.BytesIO()
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.axis('off')
        plt.text(0.05, 0.5, latex_code, size=10)
        plt.savefig(buf, format='png')
        plt.close()
        
        back = (255, 255, 255, 255)
        
        im = Image.open(buf)
        bg = Image.new(im.mode, im.size, back)
        diff = ImageChops.difference(im, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        return im.crop(bbox)
    
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        for algorithm in ALGORITHMS:
            self.comboBoxAlgorithms.addItem(algorithm)

        for benchmark in BENCHMARKS:
            self.comboBoxBenchmarks.addItem(benchmark)
        
        self.pushButton.clicked.connect(self.run_algorithm)
        
	self.comboBoxBenchmarks.currentIndexChanged.connect(self.selectionchange)
    
    def selectionchange(self,i):
        if self.comboBoxBenchmarks.currentText() == "Ackley":
            ackley = Ackley.latex_code().replace("\n", "")
            show_benchmark_function(ackley).save("benchmark_function.png")
            self.label.setPixmap(QtGui.QPixmap("benchmark_function.png"))
        elif self.comboBoxBenchmarks.currentText() == "Alpine1":
            alpine = Alpine1.latex_code().replace("\n", "")
            show_benchmark_function(alpine).save("benchmark_function.png")
            self.label.setPixmap(QtGui.QPixmap("benchmark_function.png"))

    @pyqtSlot()
    def run_algorithm(self):
        print "running"
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

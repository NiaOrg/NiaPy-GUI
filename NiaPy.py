# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Settings import _Settings

#settings
SETTINGS = _Settings()
ALGORITHMS = SETTINGS.ALGORITHMS
BENCHMARKS = SETTINGS.BENCHMARKS

class Ui_NiaPy(object):
    def setupUi(self, NiaPy):
        NiaPy.setObjectName("NiaPy")
        NiaPy.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NiaPy)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 281, 201))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 18))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(120, 40, 100, 34))
        self.comboBox.setObjectName("comboBox")
        for i in range(len(ALGORITHMS)):
            self.comboBox.addItem(ALGORITHMS[i])
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 100, 100, 34))
        self.comboBox_2.setObjectName("comboBox_2")
        for i in range(len(BENCHMARKS)):
            self.comboBox_2.addItem(BENCHMARKS[i])
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 100, 34))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(470, 10, 251, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 240, 721, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        NiaPy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NiaPy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        NiaPy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NiaPy)
        self.statusbar.setObjectName("statusbar")
        NiaPy.setStatusBar(self.statusbar)

        self.retranslateUi(NiaPy)
        QtCore.QMetaObject.connectSlotsByName(NiaPy)

    def retranslateUi(self, NiaPy):
        _translate = QtCore.QCoreApplication.translate
        NiaPy.setWindowTitle(_translate("NiaPy", "NiaPy"))
        self.groupBox.setTitle(_translate("NiaPy", "Settings"))
        self.label.setText(_translate("NiaPy", "Algorithm"))
        self.label_2.setText(_translate("NiaPy", "Benchmark"))
        self.pushButton.setText(_translate("NiaPy", "Run"))
        self.groupBox_2.setTitle(_translate("NiaPy", "Benchmark function information"))
        self.groupBox_3.setTitle(_translate("NiaPy", "Results of optimization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NiaPy = QtWidgets.QMainWindow()
    ui = Ui_NiaPy()
    ui.setupUi(NiaPy)
    NiaPy.show()
    sys.exit(app.exec_())


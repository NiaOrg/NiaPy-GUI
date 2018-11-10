from PyQt5.QtWidgets import QMainWindow, QAbstractItemView
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QTextCursor
import NiaPy.algorithms.basic # noqa

from . MainWindow_ui import Ui_MainWindow
from inspect import getmembers, isclass
from sys import stdout, modules # noqa
import re


class PrintStream(QObject):

    # This defines a signal called 'message' that takesone string argument
    message = pyqtSignal(str)

    def write(self, message):
        self.message.emit(str(message))


class NiapyListLoader:

    @staticmethod
    def get_niapy_algorithms():
        print('NiapyListLoader.get_niapy_algorithms')
        algorithms = []
        for item in getmembers(modules['NiaPy.algorithms.basic'], isclass):
            algorithm = re.sub(r'\B([A-Z])', r' \1', item[0])
            print(algorithm)
            algorithms.append(algorithm)

        for item in getmembers(modules['NiaPy.algorithms.modified'], isclass):
            algorithm = re.sub(r'\B([A-Z])', r' \1', item[0])
            print(algorithm)
            algorithms.append(algorithm)

        for item in getmembers(modules['NiaPy.algorithms.other'], isclass):
            algorithm = re.sub(r'\B([A-Z])', r' \1', item[0])
            print(algorithm)
            algorithms.append(algorithm)
        return algorithms

    @staticmethod
    def get_niapy_benchmarks():
        print('NiapyListLoader.get_niapy_benchmarks')
        benchmarks = []
        for item in getmembers(modules['NiaPy.benchmarks'], isclass):
            benchmark = re.sub(r'\B([A-Z])', r' \1', item[0])
            print(benchmark)
            benchmarks.append(benchmark)
        return benchmarks


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        myStream = PrintStream()
        myStream.message.connect(self.on_printStream_message)

        stdout = myStream # noqa

        print('initialization of main window...')

        print('populate listWidgetAlgorithms...')
        self.listWidgetAlgorithms.addItems(
            NiapyListLoader().get_niapy_algorithms())
        self.listWidgetAlgorithms.setSelectionMode(
            QAbstractItemView.MultiSelection)

        print('populate listWidgetBenchmarks...')
        self.listWidgetBenchmarks.addItems(
            NiapyListLoader().get_niapy_benchmarks())
        self.listWidgetBenchmarks.setSelectionMode(
            QAbstractItemView.MultiSelection)

    @pyqtSlot(str)
    def on_printStream_message(self, messsage):
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(messsage)

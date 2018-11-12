import sys
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QTextCursor
import qtawesome as qta

from . MainWindow_ui import Ui_MainWindow
from .. helpers.streams import PrintStream


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self, splash):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # initialize print streaming into textEditOutput widget
        print_stream = PrintStream()
        print_stream.message.connect(self.on_print_stream_message)
        sys.stdout = print_stream # noqa

        self.algorithms = []
        self.splash = splash
        self.splash.list_loader.connect(self.list_receiver)

        # add actions to main toolbar
        self.mainToolBar.addAction(qta.icon('fa5.file'), 'New Experiment')
        self.mainToolBar.addAction(qta.icon('fa5.save'), 'Save Experiment')
        self.mainToolBar.addAction(
            qta.icon('fa5.play-circle'), 'Run Experiment')
        self.mainToolBar.addAction(
            qta.icon('fa5.stop-circle'), 'Stop Experiment')

        # config the output textedit
        self.textEditOutput.setReadOnly(True)

        print('initialization of main window...')

        print('populate listWidgetAlgorithms...')

        self.listWidgetAlgorithms.setSelectionMode(
            QAbstractItemView.MultiSelection)

        print('populate listWidgetBenchmarks...')
        self.listWidgetBenchmarks.addItems(self.algorithms)
        self.listWidgetBenchmarks.setSelectionMode(
            QAbstractItemView.MultiSelection)

    @pyqtSlot(list)
    def list_receiver(self, list):
        self.algorithms = list
        self.listWidgetAlgorithms.addItems(self.algorithms)
        self.show()
        self.splash.finish(self)

    @pyqtSlot(str)
    def on_print_stream_message(self, messsage):
        self.textEditOutput.moveCursor(QTextCursor.End)
        self.textEditOutput.insertPlainText(messsage)

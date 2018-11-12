import sys

from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap
from PyQt5.QtCore import QFile, QTextStream, QTranslator
from PyQt5.QtCore import QLocale, QTimer, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QSplashScreen
from NiaPy.algorithms import basic, modified, other # noqa

from . views.MainWindow import MainWindow
from . helpers.loaders import NiaPyListLoader

from . import resources_rc # noqa

import time


class NiaPyListLoaderProcess(QThread):

    list_loader = pyqtSignal(list)

    def __init__(self, thing):
        super(NiaPyListLoaderProcess, self).__init__()
        self.thing = thing

    def run(self):
        print('NiaPyListLoaderProcess run...')
        time.sleep(5)
        self.list_loader.emit(NiaPyListLoader.get_niapy_algorithms())


class NiaPySplash(QSplashScreen):

    list_loader = pyqtSignal(list)

    def __init__(self):
        splash_pix = QPixmap(':/icons/niapy-gui-logo.png')
        super(NiaPySplash, self).__init__(splash_pix, Qt.WindowStaysOnTopHint)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.show()

        self.niapy_loader = NiaPyListLoaderProcess('algorithm')
        self.niapy_loader.start()
        self.niapy_loader.list_loader.connect(self.list_receiver)
        self.niapy_loader.finished.connect(self.hide)

    @pyqtSlot(list)
    def list_receiver(self, msg):
        print('NiaPySplash list_receiver: ', msg)
        self.list_loader.emit(msg)


def main():
    print('main')
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(':/icons/niapy-gui-logo.png'))  # change to png!

    fontDB = QFontDatabase()
    fontDB.addApplicationFont(':/fonts/Roboto-Regular.ttf')
    app.setFont(QFont('Roboto'))

    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    translator.load(':/translations/' + QLocale.system().name() + '.qm')
    app.installTranslator(translator)

    splash = NiaPySplash() # noqa

    main_window = MainWindow(splash)  # noqa
    # main_window.show()

    # enable terminating the app using Ctrl-C
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

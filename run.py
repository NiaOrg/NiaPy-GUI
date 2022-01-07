from PyQt5 import QtWidgets
from niapygui.gui import NiaPyGUI
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NiaPyGUI()
    window.show()
    sys.exit(app.exec_())

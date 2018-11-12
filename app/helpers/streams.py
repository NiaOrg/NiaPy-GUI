from PyQt5.QtCore import QObject, pyqtSignal

__all__ = ['PrintStream']


class PrintStream(QObject):

    # This defines a signal called 'message' that takesone string argument
    message = pyqtSignal(str)

    def write(self, message):
        self.message.emit(str(message))

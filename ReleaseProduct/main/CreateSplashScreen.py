#encoding=utf-8
'''
Created on Feb 28, 2021

@author: motein
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Form(QtWidgets.QDialog):
    """ Just a simple dialog with a couple of widgets
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.console = QtWidgets.QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.inputLine = QtWidgets.QLineEdit("Write something and press Enter")
        self.inputLine.selectAll()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.console)
        layout.addWidget(self.inputLine)
        self.setLayout(layout)
        self.inputLine.setFocus()
        self.inputLine.returnPressed.connect(self.update_ui)

    def update_ui(self):
        self.console.append(self.inputLine.text())


if __name__ == "__main__":
    import sys, time

    app = QtWidgets.QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QtGui.QPixmap('splash_window.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    form = Form()
    form.show()
    splash.finish(form)
    app.exec_()
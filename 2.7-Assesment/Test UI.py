import sys
from PyQt5 import QtWidgets

class PegGameWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
    def setup(self):
        self.setGeometry(0, 0, 1700, 800)
        self.setWindowTitle('Test UI')
        self.Foods = QtWidgets.QPushButton("Foods", self)
        self.Foods
        self.Foods.move(500, 500)
        self.show()
if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 main_window = PegGameWindow()
 app.exec_()



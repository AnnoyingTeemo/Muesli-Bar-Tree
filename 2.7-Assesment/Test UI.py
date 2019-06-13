import sys
from PyQt5 import QtWidgets
#fruits, vegies, milk products, nuts, jams, juices
class PegGameWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
    def setup(self):
        self.setGeometry(0, 0, 1700, 800)
        self.setWindowTitle('Test UI')
        #Buttons code goes here
        self.Fruits = QtWidgets.QPushButton("Fruits", self)
        self.Fruits.setMinimumSize(100,100)
        self.Fruits.move(10, 10)

        self.Vegetables = QtWidgets.QPushButton("Vegetables", self)
        self.Vegetables.setMinimumSize(100,100)
        self.Vegetables.move(160, 10)

        self.MilkProducts = QtWidgets.QPushButton("Milk Products", self)
        self.MilkProducts.setMinimumSize(100,100)
        self.MilkProducts.move(310, 10)

        self.Nuts = QtWidgets.QPushButton("Nuts", self)
        self.Nuts.setMinimumSize(100,100)
        self.Nuts.move(460, 10)

        self.Jams = QtWidgets.QPushButton("Jams", self)
        self.Jams.setMinimumSize(100,100)
        self.Jams.move(610, 10)

        self.Juices = QtWidgets.QPushButton("Juices", self)
        self.Juices.setMinimumSize(100,100)
        self.Juices.move(760, 10)


        self.show()
if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 main_window = PegGameWindow()
 app.exec_()



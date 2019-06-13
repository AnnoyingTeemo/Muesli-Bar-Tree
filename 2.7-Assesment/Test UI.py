import sys
from PyQt5 import QtWidgets
#fruits, vegies, milk products, nuts, jams, juices
class PegGameWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
    def setup(self):
        self.setGeometry(0, 0, 1500, 850)
        self.setWindowTitle('Test UI')
        #Buttons code goes here
        self.Fruits = QtWidgets.QPushButton("Fruits", self)
        self.Fruits.setMinimumSize(130,130)
        self.Fruits.move(30, 10)

        self.Vegetables = QtWidgets.QPushButton("Vegetables", self)
        self.Vegetables.setMinimumSize(130,130)
        self.Vegetables.move(190, 10)

        self.MilkProducts = QtWidgets.QPushButton("Milk Products", self)
        self.MilkProducts.setMinimumSize(130,130)
        self.MilkProducts.move(350, 10)

        self.Nuts = QtWidgets.QPushButton("Nuts", self)
        self.Nuts.setMinimumSize(130,130)
        self.Nuts.move(510, 10)

        self.Jams = QtWidgets.QPushButton("Jams", self)
        self.Jams.setMinimumSize(130,130)
        self.Jams.move(670, 10)

        self.Juices = QtWidgets.QPushButton("Juices", self)
        self.Juices.setMinimumSize(130,130)
        self.Juices.move(830, 10)

        #Checkout Code
        self.Cart = QtWidgets.QTextBrowser(self)
        self.Cart.append("Test")
        self.Cart.append("Test2")
        self.Cart.setMinimumSize(450,650)
        self.Cart.move(1000,10)

        self.Checkout = QtWidgets.QPushButton("Checkout", self)
        self.Checkout.setMinimumSize(220,130)
        self.Checkout.move(1230,670)

        self.Clear = QtWidgets.QPushButton("Clear Cart", self)
        self.Clear.setMinimumSize(220,130)
        self.Clear.move(1000,670)

        self.show()
if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 main_window = PegGameWindow()
 app.exec_()

# 150, ~, 1150
# the wooden one with glass windows

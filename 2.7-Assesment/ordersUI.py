#with open("Orders.json", "r") as f: Orders = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices
import sys, random, json
from collections import Counter
from PyQt5 import QtWidgets

with open("Orders.json", "r") as f: orders = f.read()
orders = json.loads(orders)
currentOrders = []
print(orders)

for order in orders['orders']:
    print(order)
    currentOrders.append(order)

class TestUI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
    def setup(self):
        self.setGeometry(0, 0, 1500, 850)
        self.setWindowTitle('Test UI')


        #Buttons go here
        self.AddFood = QtWidgets.QPushButton("Add Food", self)
        self.AddFood.setMinimumSize(130,130)
        self.AddFood.move(500,10)

        self.Orders = QtWidgets.QPushButton("Orders", self)
        self.Orders.setMinimumSize(130,130)
        self.Orders.move(30, 10)
        #self.Orders.clicked.connect(self.Orders_Clicked)


        self.OrdersList = QtWidgets.QTextBrowser(self)
        self.OrdersList.setMinimumSize(450,600)
        self.OrdersList.move(1000,10)
        self.AllOrders = ""
        for item in currentOrders:
            for food in item:
                self.AllOrders += f"{(food.split()[0].replace(':', ''))} "
            self.AllOrders += "\n"
        self.OrdersList.setText(self.AllOrders)

        #make this first one a drop down menu
        self.FoodTypetext = QtWidgets.QComboBox(self)
        #self.FoodTypetext = QtWidgets.QLineEdit(self)
        self.FoodTypetext.move(500,500)
        self.FoodTypetext.resize(300,50)

        self.FoodNametext = QtWidgets.QLineEdit(self)
        self.FoodNametext.move(500,560)
        self.FoodNametext.resize(300,50)

        self.FoodPricetext = QtWidgets.QLineEdit(self)
        self.FoodPricetext.move(500,620)
        self.FoodPricetext.resize(300,50)

        self.InputNewFood = QtWidgets.QPushButton("Input", self)
        self.InputNewFood.move(550,680)
        self.InputNewFood.setMinimumSize(200,50)

        self.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()
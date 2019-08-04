import sys, random, json
from collections import Counter
from functools import partial
from PyQt5 import QtWidgets

with open("pickups.json", "r") as f: pickups = f.read()
pickups = json.loads(pickups)
f.close()

with open("deliveries.json", "r") as f: deliveries = f.read()
deliveries = json.loads(deliveries)
f.close()


def refreshPickups():
    with open("pickups.json", "r") as f: pickups = f.read()
    pickups = json.loads(pickups)
    newcurrentOrders = []
    for order in pickups['pickups']:
        newcurrentOrders.append(order)
    print(newcurrentOrders)
    return newcurrentOrders
def refreshDeliveries():
    with open("deliveries.json", "r") as f: deliveries = f.read()
    deliveries = json.loads(deliveries)
    newcurrentOrders = []
    for order in deliveries['deliveries']:
        newcurrentOrders.append(order)
    print(newcurrentOrders)
    return newcurrentOrders

currentPickups = refreshPickups()
currentDeliveries = refreshDeliveries()

class TestUI(QtWidgets.QWidget):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.setup()
    def setup(self):
        self.setGeometry(0, 0, 1500, 850)
        self.setWindowTitle('Test UI')

        self.Order0 = QtWidgets.QPushButton("Order0", self)
        self.Order1 = QtWidgets.QPushButton("Order1", self)
        self.Order2 = QtWidgets.QPushButton("Order2", self)
        self.Order3 = QtWidgets.QPushButton("Order3", self)
        self.Order4 = QtWidgets.QPushButton("Order4", self)
        self.Order5 = QtWidgets.QPushButton("Order5", self)
        self.Order6 = QtWidgets.QPushButton("Order6", self)
        self.Order7 = QtWidgets.QPushButton("Order7", self)
        self.Order8 = QtWidgets.QPushButton("Order8", self)
        self.Order9 = QtWidgets.QPushButton("Order9", self)
        self.Order10 = QtWidgets.QPushButton("Order10", self)
        self.Order11 = QtWidgets.QPushButton("Order11", self)
        self.Order12 = QtWidgets.QPushButton("Order12", self)
        self.Order13 = QtWidgets.QPushButton("Order13", self)
        self.Order14 = QtWidgets.QPushButton("Order14", self)
        self.Order15 = QtWidgets.QPushButton("Order15", self)
        self.Order16 = QtWidgets.QPushButton("Order16", self)
        self.Order17 = QtWidgets.QPushButton("Order17", self)

        self.buttons = [self.Order0, self.Order1, self.Order2, self.Order3, self.Order4, self.Order5, self.Order6, self.Order7, self.Order8, self.Order9, self.Order10, self.Order11, self.Order12, self.Order13, self.Order14, self.Order15, self.Order16, self.Order17]

        i = 0
        x = 30
        y= 200
        for Button in self.buttons:
            Button.setMinimumSize(130,130)
            Button.setObjectName(f"Order {i}")
            Button.setText(f"Order {i+1}")
            Button.move(x,y)
            #Button.clicked.connect(partial(self.buttonclicked, i))
            x += 160
            if x > 830:
                x = 30
                y += 130
            i += 1
            print(i,x,y)
            #Button.hide()

        self.PickupsList = QtWidgets.QTextBrowser(self)
        self.PickupsList.setMinimumSize(450,600)
        self.PickupsList.move(1000,10)
        self.AllPickups = ""
        #code to show orders
        for item in currentPickups:
            for food in item[2:]:
                #self.AllOrders += f"{food}"
                self.AllPickups += f"{(food.rsplit(' ', 1)[0].replace(':', ''))} "
            self.AllPickups += "\n"
        self.PickupsList.setText(self.AllPickups)

        #add stuff for currentDeliveries aswell. make 2 uis one for each.

        self.DeliveriesList = QtWidgets.QTextBrowser(self)
        self.DeliveriesList.setMinimumSize(450,600)
        self.DeliveriesList.move(1000,10)
        self.AllDeliveries = ""
        #code to show orders
        for item in currentDeliveries:
            for food in item[2:]:
                #self.AllOrders += f"{food}"
                self.AllDeliveries += f"{(food.rsplit(' ', 1)[0].replace(':', ''))} "
            self.AllDeliveries += "\n"
        self.DeliveriesList.setText(self.AllDeliveries)

        self.DeliveriesList.hide()
        self.PickupsList.hide()
        for object in self.buttons:
            object.hide()
        self.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()
    #sys.exit(app.exec_())

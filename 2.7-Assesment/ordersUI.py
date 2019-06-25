#with open("Orders.json", "r") as f: Orders = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices
import sys, random, json
from collections import Counter
from PyQt5 import QtWidgets

with open("Orders.json", "r") as f: orders = f.read()
orders = json.loads(orders)



# with open("Foods.json", "a") as f: foods = f.read()
# foods = json.loads(foods)

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
                self.AllOrders += f"{(food.rsplit(' ', 1)[0].replace(':', ''))} "
            self.AllOrders += "\n"
        self.OrdersList.setText(self.AllOrders)

        #make this first one a drop down menu
        self.FoodTypetext = QtWidgets.QComboBox(self)
        #self.FoodTypetext = QtWidgets.QLineEdit(self)

        #fix the names of these later
        self.FoodTypetext.addItem("Vegetables")
        self.FoodTypetext.addItem("Fruit")
        self.FoodTypetext.addItem("Milk")
        self.FoodTypetext.addItem("Nuts")
        self.FoodTypetext.addItem("Juices")
        self.FoodTypetext.addItem("Jams")

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
        self.InputNewFood.clicked.connect(self.InputNewFoodPressed)

        #Test delete button, this will be changed
        self.DeleteFoodName = QtWidgets.QComboBox(self)
        self.DeleteFoodName.move(100,500)
        self.DeleteFoodName.resize(300,50)

        self.DeleteFoodButton = QtWidgets.QPushButton("Delete", self)
        self.DeleteFoodButton.move(150,680)
        self.DeleteFoodButton.setMinimumSize(200,50)
        self.DeleteFoodButton.clicked.connect(self.DeletePressed)


        with open("Foods.json", "r") as z: Foods = z.read()
        Foods = json.loads(Foods)
        FoodTypesList = ['Fruit', 'Vegetables', 'Milk', 'Nuts', 'Jams', 'Juices']

        for item in FoodTypesList:
            for Food in Foods[item]:
                self.DeleteFoodName.addItem(f"{item} {Food}")

        self.show()
    def DeletePressed(self):
        with open('Foods.json', 'r') as f:
                fr = json.load(f)
                print(fr)
                del (fr[self.DeleteFoodName.currentText().split()[0]][self.DeleteFoodName.currentText().split(' ', 1)[1]])
        with open('Foods.json', 'w') as fw: json.dump(fr, fw)
        self.DeleteFoodName.clear()
        with open("Foods.json", "r") as z: Foods = z.read()
        Foods = json.loads(Foods)
        FoodTypesList = ['Fruit', 'Vegetables', 'Milk', 'Nuts', 'Jams', 'Juices']

        for item in FoodTypesList:
            for Food in Foods[item]:
                self.DeleteFoodName.addItem(f"{item} {Food}")


    def InputNewFoodPressed(self):
        fr = None
        if len(self.FoodNametext.text()) > 0 and len(self.FoodPricetext.text()) > 0:
            NewFood = {
                "Name": self.FoodNametext.text(),
                "Price": self.FoodPricetext.text()
            }
            NewFoodDict = {
                NewFood["Name"]: {
                    "Price": float(NewFood["Price"])
                }
            }
            with open('Foods.json', 'r') as f:
                    fr = json.load(f)
                    print(fr)
                    fr[self.FoodTypetext.currentText()][NewFood["Name"]] = (NewFoodDict[NewFood["Name"]])
            with open('Foods.json', 'w') as fw: json.dump(fr, fw)
        else:
            print("Please enter some things into the box")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()

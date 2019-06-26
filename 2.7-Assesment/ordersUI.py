#with open("Orders.json", "r") as f: Orders = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices
import sys, random, json
from collections import Counter
from functools import partial
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

        self.selectedOrder = None
        #Buttons go here
        self.AddFood = QtWidgets.QPushButton("Add Food", self)
        self.AddFood.setMinimumSize(130,130)
        self.AddFood.move(500,10)
        self.AddFood.clicked.connect(self.Foods_Clicked)

        self.Orders = QtWidgets.QPushButton("Orders", self)
        self.Orders.setMinimumSize(130,130)
        self.Orders.move(30, 10)
        self.Orders.clicked.connect(self.Orders_Clicked)


        self.OrdersList = QtWidgets.QTextBrowser(self)
        self.OrdersList.setMinimumSize(450,600)
        self.OrdersList.move(1000,10)
        self.AllOrders = ""
        #code to show orders
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


        #Buttons Code is here
        self.Food0 = QtWidgets.QPushButton("Food0", self)
        self.Food1 = QtWidgets.QPushButton("Food1", self)
        self.Food2 = QtWidgets.QPushButton("Food2", self)
        self.Food3 = QtWidgets.QPushButton("Food3", self)
        self.Food4 = QtWidgets.QPushButton("Food4", self)
        self.Food5 = QtWidgets.QPushButton("Food5", self)
        self.Food6 = QtWidgets.QPushButton("Food6", self)
        self.Food7 = QtWidgets.QPushButton("Food7", self)
        self.Food8 = QtWidgets.QPushButton("Food8", self)
        self.Food9 = QtWidgets.QPushButton("Food9", self)
        self.Food10 = QtWidgets.QPushButton("Food10", self)
        self.Food11 = QtWidgets.QPushButton("Food11", self)
        self.Food12 = QtWidgets.QPushButton("Food12", self)
        self.Food13 = QtWidgets.QPushButton("Food13", self)
        self.Food14 = QtWidgets.QPushButton("Food14", self)
        self.Food15 = QtWidgets.QPushButton("Food15", self)
        self.Food16 = QtWidgets.QPushButton("Food16", self)
        self.Food17 = QtWidgets.QPushButton("Food17", self)

        self.buttons = [self.Food0, self.Food1, self.Food2, self.Food3, self.Food4, self.Food5, self.Food6, self.Food7, self.Food8, self.Food9, self.Food10, self.Food11, self.Food12, self.Food13, self.Food14, self.Food15, self.Food16, self.Food17]

        i = 0
        x = 30
        y= 200
        for Button in self.buttons:
            Button.setMinimumSize(130,130)
            Button.setObjectName(f"Order {i}")
            Button.setText(f"Order {i+1}")
            Button.move(x,y)
            Button.clicked.connect(partial(self.buttonclicked, i))
            x += 160
            if x > 830:
                x = 30
                y += 130
            i += 1
            print(i,x,y)
            Button.hide()
        #self.Food0.setMinimumSize(130,130)
        #self.Food0.move(30,200)
        #self.Food0.setObjectName("Food 0")
        #self.Food0.hide()
        #self.Food0.clicked.connect(self.Food0Clicked)

        self.completeOrder = QtWidgets.QPushButton("Complete Order", self)
        self.completeOrder.setMinimumSize(220,130)
        self.completeOrder.move(1230,670)

        self.cancelOrder = QtWidgets.QPushButton("Cancel Order", self)
        self.cancelOrder.setMinimumSize(220,130)
        self.cancelOrder.move(1000,670)
        self.cancelOrder.clicked.connect(self.cancel_order)

        self.hideButtons()
        self.hideOrders()
        self.hideFoods()

        self.show()

    def cancel_order(self):
        with open('Orders.json', 'r') as f:
                    fr = json.load(f)
                    print(fr)
                    del[fr[self.selectedOrder]]
        with open('Orders.json', 'w') as fw: json.dump(fr, fw)
    def buttonclicked(self, i):
        self.OrdersList.clear()
        self.selectedOrder = i
        for item in currentOrders[i]:
            self.OrdersList.append(item)

    def DeletePressed(self):
        with open('Foods.json', 'r') as f:
                fr = json.load(f)
                print(fr)
                del (fr[self.DeleteFoodName.currentText().split()[0]][self.DeleteFoodName.currentText().split(' ', 1)[1]])
        with open('Foods.json', 'w') as fw: json.dump(fr, fw)

        self.RefreshDeleteTab()
    def RefreshDeleteTab(self):
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

        self.FoodNametext.clear()
        self.FoodPricetext.clear()

        self.RefreshDeleteTab()
    def Orders_Clicked(self):
        self.hideFoods()
        self.showOrders()
        self.showButtons()
    def Foods_Clicked(self):
        self.hideOrders()
        self.showFoods()
        self.hideButtons()
    def hideFoods(self):
        self.DeleteFoodName.hide()
        self.DeleteFoodButton.hide()
        self.InputNewFood.hide()
        self.FoodPricetext.hide()
        self.FoodNametext.hide()
        self.FoodTypetext.hide()
    def showFoods(self):
        self.DeleteFoodName.show()
        self.DeleteFoodButton.show()
        self.InputNewFood.show()
        self.FoodPricetext.show()
        self.FoodNametext.show()
        self.FoodTypetext.show()
    def showOrders(self):
        self.OrdersList.show()
        self.cancelOrder.show()
        self.completeOrder.show()
    def hideOrders(self):
        self.cancelOrder.hide()
        self.completeOrder.hide()
        self.OrdersList.hide()
    def showButtons(self):
        # for button in self.buttons:
        #     button.show()
        #print(len(currentOrders))
        if len(currentOrders) <= 18:
            for i in range(len(currentOrders)):
                self.buttons[i].show()
        else:
            for i in range(18):
                self.buttons[i].show()
        #for item in currentOrders:


            #for food in item:

                #self.AllOrders += f"{(food.rsplit(' ', 1)[0].replace(':', ''))} "
            #self.AllOrders += "\n"

    def hideButtons(self):
        for button in self.buttons:
            button.hide()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()
    #sys.exit(app.exec_())

# with open("Foods.txt", "r") as f: foods = f.readlines()


#fruits, vegies, milk products, nuts, jams, juices
import sys, random, json, datetime, calendar
from collections import Counter
from PyQt5 import QtWidgets

with open("Foods.json", "r") as f: foods = f.read()
foods = json.loads(foods)
#fruits, vegies, milk products, nuts, jams, juices
def cint(codeinfo): return "{:,}".format(codeinfo)
#Stuff for Setup
FoodTypesList = ['fruits', 'vegies', 'milk_products', 'nuts', 'jams', 'juices']
testDictionary = {
    "Fruit": {},
    "Vegetables": {},
    "Milk": {},
    "Nuts": {},
    "Jams": {},
    "Juices": {}
}
FruitsList = []
VegiesList = []
MilkProductsList = []
NutsList = []
JamsList = []
JuicesList = []
amountOfWords = 0

#current order list
currentOrders = []
checkoutCart = None

def transferData(currentCart):
    return currentCart

listOfFoodTypes = ["Vegetables", "Fruit", "Milk", "Nuts","Jams", "Juices"]
for i in range(len(listOfFoodTypes)):
    e = 0
    for word in foods[listOfFoodTypes[i]]:
        food = {
            "Name": word,
            "Type of food": listOfFoodTypes[i],
            "Price": foods[listOfFoodTypes[i]][word]["Price"],
            "ObjectName": f"Food {e}",
            "RawPrice": foods[listOfFoodTypes[i]][word]["Price"]

            #
            # "Name": word.strip().split()[0].replace('_', ' '),
            # "Type of food": word.strip().split()[1].replace('_', ' '),
            # #"Price": '${}'.format(word.strip().split()[2]),
            # "Price": f'${word.strip().split()[2]}',
            # "Per Kg or Each": word.strip().split()[3].replace('_', ' '),
            # "ObjectName": f"Food {i}",
            # "RawPrice": float(word.strip().split()[2])
        }
        testDictionary[listOfFoodTypes[i]]["Food {}".format(e)] = food
        e += 1
print(testDictionary)

for item in testDictionary["Fruit"]:
        if testDictionary["Fruit"][item]["Type of food"] == "Fruit":
            FruitsList.append(item)
for item in testDictionary["Vegetables"]:
        if testDictionary["Vegetables"][item]["Type of food"] == "Vegetables":
            VegiesList.append(item)
for item in testDictionary["Milk"]:
        if testDictionary["Milk"][item]["Type of food"] == "Milk":
            MilkProductsList.append(item)
for item in testDictionary["Nuts"]:
        if testDictionary["Nuts"][item]["Type of food"] == "Nuts":
            NutsList.append(item)
for item in testDictionary["Jams"]:
        if testDictionary["Jams"][item]["Type of food"] == "Jams":
            JamsList.append(item)
for item in testDictionary["Juices"]:
        if testDictionary["Juices"][item]["Type of food"] == "Juices":
            JuicesList.append(item)
print(FruitsList)
print(VegiesList)
print(MilkProductsList)
print(NutsList)
print(JamsList)
print(JuicesList)
class TestUI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()
    def setup(self):
        self.CurrentCart = []
        self.CurrentFoodType = "Null"
        self.setGeometry(0, 0, 1500, 850)
        self.setWindowTitle('Test UI')
        #Buttons code goes here
        self.Fruits = QtWidgets.QPushButton("Fruits", self)
        self.Fruits.setMinimumSize(130,130)
        self.Fruits.move(30, 10)
        self.Fruits.clicked.connect(self.Fruits_Clicked)

        self.Vegetables = QtWidgets.QPushButton("Vegetables", self)
        self.Vegetables.setMinimumSize(130,130)
        self.Vegetables.move(190, 10)
        self.Vegetables.clicked.connect(self.Veges_Clicked)

        self.MilkProducts = QtWidgets.QPushButton("Milk Products", self)
        self.MilkProducts.setMinimumSize(130,130)
        self.MilkProducts.move(350, 10)
        self.MilkProducts.clicked.connect(self.Milk_Clicked)

        self.Nuts = QtWidgets.QPushButton("Nuts", self)
        self.Nuts.setMinimumSize(130,130)
        self.Nuts.move(510, 10)
        self.Nuts.clicked.connect(self.Nuts_Clicked)

        self.Jams = QtWidgets.QPushButton("Jams", self)
        self.Jams.setMinimumSize(130,130)
        self.Jams.move(670, 10)
        self.Jams.clicked.connect(self.Jams_Clicked)

        self.Juices = QtWidgets.QPushButton("Juices", self)
        self.Juices.setMinimumSize(130,130)
        self.Juices.move(830, 10)
        self.Juices.clicked.connect(self.Juices_Clicked)

        #Checkout Code
        self.Cart = QtWidgets.QTextBrowser(self)
        self.Cart.setMinimumSize(450,600)
        self.Cart.move(1000,10)

        #Total Text goes here, it needs to blend into the checkout
        self.Total = QtWidgets.QTextBrowser(self)
        self.Total.setMinimumSize(450,10)
        self.Total.setText("Total: $0")
        self.Total.setMaximumHeight(50)
        self.Total.move(1000,610)

        self.Checkout = QtWidgets.QPushButton("Checkout", self)
        self.Checkout.setMinimumSize(220,130)
        self.Checkout.move(1230,670)
        self.Checkout.clicked.connect(self.CheckOut_Clicked)

        self.Clear = QtWidgets.QPushButton("Clear Cart", self)
        self.Clear.setMinimumSize(220,130)
        self.Clear.move(1000,670)
        self.Clear.clicked.connect(self.Clear_Clicked)

        self.Food0 = QtWidgets.QPushButton("Food0", self)
        self.Food0.setMinimumSize(130,130)
        self.Food0.move(30,200)
        self.Food0.setObjectName("Food 0")
        self.Food0.hide()
        self.Food0.clicked.connect(self.Food0Clicked)
        self.Food1 = QtWidgets.QPushButton("Food1", self)
        self.Food1.setMinimumSize(130,130)
        self.Food1.move(190,200)
        self.Food1.setObjectName("Food 1")
        self.Food1.hide()
        self.Food1.clicked.connect(self.Food1Clicked)
        self.Food2 = QtWidgets.QPushButton("Food2", self)
        self.Food2.setMinimumSize(130,130)
        self.Food2.move(350,200)
        self.Food2.setObjectName("Food 2")
        self.Food2.hide()
        self.Food2.clicked.connect(self.Food2Clicked)
        self.Food3 = QtWidgets.QPushButton("Food3", self)
        self.Food3.setMinimumSize(130,130)
        self.Food3.move(510,200)
        self.Food3.setObjectName("Food 3")
        self.Food3.hide()
        self.Food3.clicked.connect(self.Food3Clicked)
        self.Food4 = QtWidgets.QPushButton("Food4", self)
        self.Food4.setMinimumSize(130,130)
        self.Food4.move(670,200)
        self.Food4.setObjectName("Food 4")
        self.Food4.hide()
        self.Food4.clicked.connect(self.Food4Clicked)
        self.Food5 = QtWidgets.QPushButton("Food5", self)
        self.Food5.setMinimumSize(130,130)
        self.Food5.move(830,200)
        self.Food5.setObjectName("Food 5")
        self.Food5.hide()
        self.Food5.clicked.connect(self.Food5Clicked)
        self.Food6 = QtWidgets.QPushButton("Food6", self)
        self.Food6.setMinimumSize(130,130)
        self.Food6.move(30,330)
        self.Food6.setObjectName("Food 6")
        self.Food6.hide()
        self.Food6.clicked.connect(self.Food6Clicked)
        self.Food7 = QtWidgets.QPushButton("Food7", self)
        self.Food7.setMinimumSize(130,130)
        self.Food7.move(190,330)
        self.Food7.setObjectName("Food 7")
        self.Food7.hide()
        self.Food7.clicked.connect(self.Food7Clicked)
        self.Food8 = QtWidgets.QPushButton("Food8", self)
        self.Food8.setMinimumSize(130,130)
        self.Food8.move(350,500)
        self.Food8.setObjectName("Food 8")
        self.Food8.hide()
        self.Food8.clicked.connect(self.Food8Clicked)
        self.Food9 = QtWidgets.QPushButton("Food9", self)
        self.Food9.setMinimumSize(130,130)
        self.Food9.move(510,500)
        self.Food9.setObjectName("Food 9")
        self.Food9.hide()
        self.Food9.clicked.connect(self.Food9Clicked)
        self.Food10 = QtWidgets.QPushButton("Food10", self)
        self.Food10.setMinimumSize(130,130)
        self.Food10.move(670,500)
        self.Food10.setObjectName("Food 10")
        self.Food10.hide()
        self.Food10.clicked.connect(self.Food10Clicked)
        self.Food11 = QtWidgets.QPushButton("Food11", self)
        self.Food11.setMinimumSize(130,130)
        self.Food11.move(830,500)
        self.Food11.setObjectName("Food 11")
        self.Food11.hide()
        self.Food11.clicked.connect(self.Food11Clicked)

        self.FoodsDictionary = {0: self.Food0, 1: self.Food1, 2: self.Food2, 3: self.Food3, 4: self.Food4, 5: self.Food5, 6: self.Food6, 7: self.Food7, 8: self.Food8, 9: self.Food9, 10: self.Food10, 11: self.Food11}

        self.currentOrders = []
        self.show()
    #Code for buttons warning terrible code ahead

    def Veges_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(VegiesList)):
            self.FoodsDictionary[i].setText(testDictionary["Vegetables"][VegiesList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Vegetables"][VegiesList[i]]["ObjectName"])
        self.CurrentFoodType = "Vegetables"

        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Milk_Clicked(self):

        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(MilkProductsList)):
            self.FoodsDictionary[i].setText(testDictionary["Milk"][MilkProductsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Milk"][MilkProductsList[i]]["ObjectName"])
        self.CurrentFoodType = "Milk"
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Nuts_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(NutsList)):
            self.FoodsDictionary[i].setText(testDictionary["Nuts"][NutsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Nuts"][NutsList[i]]["ObjectName"])
        self.CurrentFoodType = "Nuts"
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Jams_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(JamsList)):
            self.FoodsDictionary[i].setText(testDictionary["Jams"][JamsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Jams"][JamsList[i]]["ObjectName"])
        self.CurrentFoodType = "Jams"
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()

    def Juices_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(JuicesList)):
            self.FoodsDictionary[i].setText(testDictionary["Juices"][JuicesList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Juices"][JuicesList[i]]["ObjectName"])
        self.CurrentFoodType = "Juices"
        self.show()
    def Fruits_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(FruitsList)):
            self.FoodsDictionary[i].setText(testDictionary["Fruit"][FruitsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Fruit"][FruitsList[i]]["ObjectName"])
        self.CurrentFoodType = "Fruit"
        self.show()
    def Food0Clicked(self):
        print(self.CurrentCart)#trying to find why name is getting into self.currentCart
        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food0.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food0.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food0.objectName()]["Price"]}')
        print(self.CurrentCart)
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
        print(self.Cart, cartText)
    def Food1Clicked(self):
        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food1.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food1.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food1.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food2Clicked(self):
        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food2.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food2.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food2.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food3Clicked(self):
        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food3.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food3.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food3.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food4Clicked(self):
        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food4.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food4.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food4.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food5Clicked(self):
        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food5.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food5.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food5.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food6Clicked(self):

        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food6.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food6.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food6.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food7Clicked(self):

        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food7.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food7.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food7.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food8Clicked(self):

        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food8.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food8.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food8.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food9Clicked(self):

        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food9.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food9.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food9.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food10Clicked(self):

        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food10.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food10.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food10.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Food11Clicked(self):

        self.currentOrders.append(testDictionary[self.CurrentFoodType][self.Food11.objectName()]["RawPrice"])
        self.CurrentCart.append(f'{testDictionary[self.CurrentFoodType][self.Food11.objectName()]["Name"]}: {testDictionary[self.CurrentFoodType][self.Food11.objectName()]["Price"]}')
        total = 0
        cartText = []
        for item in Counter(self.CurrentCart):
            cartText.append(f"{item} * {Counter(self.CurrentCart)[item]}")
        self.Cart.setText("")
        for item in cartText:
            self.Cart.append(item)
        for item in self.currentOrders:
            total += item
            self.Total.setText(f"Total: ${cint(total)}")
    def Clear_Clicked(self):
        self.Cart.setText("")
        self.currentOrders = []
        self.CurrentCart = []
        self.Total.setText("Total: $0")
    def CheckOut_Clicked(self):
        total = 0
        for item in self.currentOrders:
            total += item
        print(total)
        print(self.CurrentCart)
        #code to checkout
        # fr = None
        # if len(self.CurrentCart) > 0:
        #     with open('Orders.json', 'r') as f:
        #         fr = json.load(f)
        #         print(fr)
        #         fr['orders'].append(self.CurrentCart)
        #
        #     with open('Orders.json', 'w') as fw: json.dump(fr, fw)

        TestUI.checkoutCart = transferData(self.CurrentCart)
        self.Checkout = CheckoutUI(self)
        self.Checkout.show()
        #self.CurrentCart.clear()
class CheckoutUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.setupCheckout()
    def setupCheckout(self):
        #self.CurrentCart = []
        #self.CurrentFoodType = "Null"
        self.setGeometry(0, 0, 400, 500)
        self.setWindowTitle('Checkout')
        self.currentCart = TestUI.checkoutCart
        self.Name = QtWidgets.QLineEdit(self, placeholderText="Name")
        self.Name.move(50,10)
        self.Name.resize(300,50)

        self.DeliveryOrPickup = QtWidgets.QComboBox(self)
        self.DeliveryOrPickup.move(50, 70)
        self.DeliveryOrPickup.setMinimumSize(300,50)
        self.DeliveryOrPickup.addItem("Pickup")
        self.DeliveryOrPickup.addItem("Delivery")


        self.cardInfo(50, 150)
        print(self.currentCart)

        self.show()
    def checkout(self):
        fr = None
        if len(self.currentCart) > 0:
            with open('Orders.json', 'r') as f:
                fr = json.load(f)
                print(fr)
                if self.Name.text() == "":
                    self.Name.setText("Unknown")
                self.currentCart.insert(0, self.DeliveryOrPickup.currentText())
                self.currentCart.insert(0, self.Name.text())
                # self.currentCart.append(self.Name.text())
                fr['orders'].append(self.currentCart)

            with open('Orders.json', 'w') as fw: json.dump(fr, fw)
            self.close()
    def cardInfo(self, posx, posy):
        self.CardNumber = QtWidgets.QLineEdit(self, placeholderText="Card Number")
        self.SecurityCode = QtWidgets.QLineEdit(self, placeholderText="Security Code")
        self.ExpireMonth = QtWidgets.QComboBox(self)
        self.ExpireYear = QtWidgets.QComboBox(self)
        self.Order = QtWidgets.QPushButton("Place Order", self)
        self.Order.clicked.connect(self.checkout)

        self.Order.move(posx, posy + 150)
        self.CardNumber.move(posx,posy + 50)
        self.SecurityCode.move(posx, posy + 100)
        self.ExpireMonth.move(posx,posy)
        self.ExpireYear.move(posx + 120,posy)
        for i in range (12):
            self.ExpireMonth.addItem(calendar.month_name[i + 1])
        yearRange = 1001
        startingYear = int(datetime.datetime.now().year)
        print(startingYear, startingYear + yearRange)
        for i in range(startingYear, startingYear + yearRange):
            self.ExpireYear.addItem(str(i))
            # print(i)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()

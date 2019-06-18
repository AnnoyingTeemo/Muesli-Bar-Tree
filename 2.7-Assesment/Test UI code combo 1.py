with open("Foods.txt", "r") as f: foods = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices
import sys, random
from PyQt5 import QtWidgets
#fruits, vegies, milk products, nuts, jams, juices

#Stuff for Setup
FoodTypesList = ['fruits', 'vegies', 'milk_products', 'nuts', 'jams', 'juices']
testDictionary = {
    "Fruit": {},
    "Vegetable": {},
    "Milk Product": {},
    "Nuts": {},
    "Jam": {},
    "Juice": {}
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

i = 0
for word in foods:
    food = {
        "Name": word.strip().split()[0].replace('_', ' '),
        "Type of food": word.strip().split()[1].replace('_', ' '),
        #"Price": '${}'.format(word.strip().split()[2]),
        "Price": f'${word.strip().split()[2]}',
        "Per Kg or Each": word.strip().split()[3].replace('_', ' ')
    }
    testDictionary[word.strip().split()[1].replace('_', ' ')]["Food {}".format(i)] = food
    i += 1
print(testDictionary)

# foods.close()

for item in testDictionary["Fruit"]:
        if testDictionary["Fruit"][item]["Type of food"] == "Fruit":
            FruitsList.append(item)
for item in testDictionary["Vegetable"]:
        if testDictionary["Vegetable"][item]["Type of food"] == "Vegetable":
            VegiesList.append(item)
for item in testDictionary["Milk Product"]:
        if testDictionary["Milk Product"][item]["Type of food"] == "Milk Product":
            MilkProductsList.append(item)
for item in testDictionary["Nuts"]:
        if testDictionary["Nuts"][item]["Type of food"] == "Nuts":
            NutsList.append(item)
for item in testDictionary["Jam"]:
        if testDictionary["Jam"][item]["Type of food"] == "Jam":
            JamsList.append(item)
for item in testDictionary["Juice"]:
        if testDictionary["Juice"][item]["Type of food"] == "Juice":
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

        # #Add better buttons here, this is just for testing so far
        # self.Food0 = QtWidgets.QPushButton(testDictionary["Food 0"]["Name"], self)
        # self.Food0.setMinimumSize(130,130)
        # self.Food0.move(100,500)
        # self.Food0.setObjectName("Food 0")
        # self.Food0.hide()
        # self.Food0.clicked.connect(self.Food0Clicked)
        #
        # self.Food1 = QtWidgets.QPushButton(testDictionary["Food 1"]["Name"], self)
        # self.Food1.setMinimumSize(130,130)
        # self.Food1.setObjectName("Food 1")
        # self.Food1.move(200,500)
        # self.Food1.hide()
        # self.Food1.clicked.connect(self.Food1Clicked)
        #
        # self.Food2 = QtWidgets.QPushButton(testDictionary["Food 2"]["Name"], self)
        # self.Food2.setMinimumSize(130,130)
        # self.Food2.setObjectName("Food 2")
        # self.Food2.move(300,500)
        # self.Food2.hide()
        # self.Food2.clicked.connect(self.Food2Clicked)
        #
        #
        # self.Food3 = QtWidgets.QPushButton(testDictionary["Food 3"]["Name"], self)
        # self.Food3.setMinimumSize(130,130)
        # self.Food3.move(400,500)
        # self.Food3.setObjectName("Food 3")
        # self.Food3.hide()
        # self.Food3.clicked.connect(self.Food3Clicked)
        #
        # self.Food4 = QtWidgets.QPushButton(testDictionary["Food 4"]["Name"], self)
        # self.Food4.setMinimumSize(130,130)
        # self.Food4.move(500,500)
        # self.Food4.setObjectName("Food 4")
        # self.Food4.hide()
        # self.Food4.clicked.connect(self.Food4Clicked)
        #
        # self.Food5 = QtWidgets.QPushButton(testDictionary["Food 5"]["Name"], self)
        # self.Food5.setMinimumSize(130,130)
        # self.Food5.setObjectName("Food 5")
        # self.Food5.move(600,500)
        # self.Food5.hide()
        # self.Food5.clicked.connect(self.Food5Clicked)
        #
        # self.Food6 = QtWidgets.QPushButton(testDictionary["Food 6"]["Name"], self)
        # self.Food6.setMinimumSize(130,130)
        # self.Food6.setObjectName("Food 6")
        # self.Food6.move(700,500)
        # self.Food6.hide()
        # self.Food6.clicked.connect(self.Food6Clicked)
        #
        # self.Food7 = QtWidgets.QPushButton(testDictionary["Food 7"]["Name"], self)
        # self.Food7.setMinimumSize(130,130)
        # self.Food7.setObjectName("Food 7")
        # self.Food7.move(800,500)
        # self.Food7.hide()
        # self.Food7.clicked.connect(self.Food7Clicked)



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
        #self.Food1.clicked.connect(self.Food1Clicked)

        self.Food2 = QtWidgets.QPushButton("Food2", self)
        self.Food2.setMinimumSize(130,130)
        self.Food2.move(350,200)
        self.Food2.setObjectName("Food 2")
        self.Food2.hide()
       #self.Food2.clicked.connect(self.Food2Clicked)

        self.Food3 = QtWidgets.QPushButton("Food3", self)
        self.Food3.setMinimumSize(130,130)
        self.Food3.move(510,200)
        self.Food3.setObjectName("Food 3")
        self.Food3.hide()
      #  self.Food3.clicked.connect(self.Food3Clicked)
        self.Food4 = QtWidgets.QPushButton("Food4", self)
        self.Food4.setMinimumSize(130,130)
        self.Food4.move(670,200)
        self.Food4.setObjectName("Food 4")
        self.Food4.hide()
     #   self.Food4.clicked.connect(self.Food4Clicked)
        self.Food5 = QtWidgets.QPushButton("Food5", self)
        self.Food5.setMinimumSize(130,130)
        self.Food5.move(830,200)
        self.Food5.setObjectName("Food 5")
        self.Food5.hide()
    #    self.Food5.clicked.connect(self.Food5Clicked)
        self.Food6 = QtWidgets.QPushButton("Food6", self)
        self.Food6.setMinimumSize(130,130)
        self.Food6.move(30,330)
        self.Food6.setObjectName("Food 6")
        self.Food6.hide()
   #     self.Food6.clicked.connect(self.Food6Clicked)
        self.Food7 = QtWidgets.QPushButton("Food7", self)
        self.Food7.setMinimumSize(130,130)
        self.Food7.move(190,330)
        self.Food7.setObjectName("Food 7")
        self.Food7.hide()
  #      self.Food7.clicked.connect(self.Food7Clicked)
        self.Food8 = QtWidgets.QPushButton("Food8", self)
        self.Food8.setMinimumSize(130,130)
        self.Food8.move(350,500)
        self.Food8.setObjectName("Food 8")
        self.Food8.hide()
 #       self.Food8.clicked.connect(self.Food8Clicked)
        self.Food9 = QtWidgets.QPushButton("Food9", self)
        self.Food9.setMinimumSize(130,130)
        self.Food9.move(510,500)
        self.Food9.setObjectName("Food 9")
        self.Food9.hide()
#        self.Food9.clicked.connect(self.Food9Clicked)
        self.Food10 = QtWidgets.QPushButton("Food10", self)
        self.Food10.setMinimumSize(130,130)
        self.Food10.move(670,500)
        self.Food10.setObjectName("Food 10")
        self.Food10.hide()
       # self.Food10.clicked.connect(self.Food10Clicked)
        self.Food11 = QtWidgets.QPushButton("Food11", self)
        self.Food11.setMinimumSize(130,130)
        self.Food11.move(830,500)
        self.Food11.setObjectName("Food 11")
        self.Food11.hide()
#        self.Food11.clicked.connect(self.Food11Clicked)

        self.FoodsDictionary = {0: self.Food0, 1: self.Food1, 2: self.Food2, 3: self.Food3, 4: self.Food4, 5: self.Food5, 6: self.Food6, 7: self.Food7, 8: self.Food8, 9: self.Food9, 10: self.Food10, 11: self.Food11}

        self.currentOrders = []
        self.show()
    #Code for buttons warning terrible code ahead


    def Veges_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(VegiesList)):
            self.FoodsDictionary[i].setText(testDictionary["Vegetable"][VegiesList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Vegetable"][VegiesList[i]]["Name"])


        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Milk_Clicked(self):

        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(MilkProductsList)):
            self.FoodsDictionary[i].setText(testDictionary["Milk Product"][MilkProductsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Milk Product"][MilkProductsList[i]]["Name"])

        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Nuts_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(NutsList)):
            self.FoodsDictionary[i].setText(testDictionary["Nuts"][NutsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Nuts"][NutsList[i]]["Name"])

        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Jams_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(JamsList)):
            self.FoodsDictionary[i].setText(testDictionary["Jam"][JamsList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Jam"][JamsList[i]]["Name"])

        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Juices_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(JuicesList)):
            self.FoodsDictionary[i].setText(testDictionary["Juice"][JuicesList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Juice"][JuicesList[i]]["Name"])

        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Fruits_Clicked(self):
        for i in range(len(self.FoodsDictionary)):
            self.FoodsDictionary[i].hide()
        for i in range(len(FruitsList)):
            self.FoodsDictionary[i].setText(testDictionary["Juice"][JuicesList[i]]["Name"])
            self.FoodsDictionary[i].show()
            self.FoodsDictionary[i].setObjectName(testDictionary["Juice"][JuicesList[i]]["Name"])

        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Food0Clicked(self):
        #self.Cart.append(f"{testDictionary['Food 0']['Name']}: {testDictionary['Food 0']['Price']}")
        #self.currentOrders.append()
        self.Cart.append(self.Food0.objectName())
        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food1Clicked(self):
        self.Cart.append(f"{testDictionary['Food 1']['Name']}: {testDictionary['Food 1']['Price']}")
        self.currentOrders.append("Food 1")

        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food2Clicked(self):
        self.Cart.append(f"{testDictionary['Food 2']['Name']}: {testDictionary['Food 2']['Price']}")
        self.currentOrders.append("Food 2")


        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food3Clicked(self):
        self.Cart.append(f"{testDictionary['Food 3']['Name']}: {testDictionary['Food 3']['Price']}")
        self.currentOrders.append("Food 3")

        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food4Clicked(self):
        self.Cart.append(f"{testDictionary['Food 4']['Name']}: {testDictionary['Food 4']['Price']}")
        self.currentOrders.append("Food 4")


        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food5Clicked(self):
        self.Cart.append(f"{testDictionary['Food 5']['Name']}: {testDictionary['Food 5']['Price']}")
        self.currentOrders.append("Food 5")


        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food6Clicked(self):
        self.Cart.append(f"{testDictionary['Food 6']['Name']}: {testDictionary['Food 6']['Price']}")
        self.currentOrders.append("Food 6")


        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Food7Clicked(self):
        self.Cart.append(f"{testDictionary['Food 7']['Name']}: {testDictionary['Food 7']['Price']}")
        self.currentOrders.append("Food 7")

        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
            self.Total.setText(f"Total: ${total}")
    def Clear_Clicked(self):
        self.Cart.setText("")
        self.currentOrders = []
        self.Total.setText("Total: $0")
    def CheckOut_Clicked(self):
        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
        print(total)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()


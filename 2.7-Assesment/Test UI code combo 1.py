with open("Foods.txt", "r") as f: foods = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices
import sys, random
from PyQt5 import QtWidgets
#fruits, vegies, milk products, nuts, jams, juices

#Stuff for Setup
FoodTypesList = ['fruits', 'vegies', 'milk_products', 'nuts', 'jams', 'juices']
testDictionary = {}
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
        "Per Kg or Each": word.strip().split()[3].replace('_', ' '),
        "RawPrice": float(word.strip().split()[2].replace('_', ' '))
    }
    testDictionary["Food {}".format(i)] = food
    i += 1


# foods.close()

for item in testDictionary:
        if testDictionary[item]["Type of food"] == "Fruit":
            FruitsList.append(item)
        elif testDictionary[item]["Type of food"] == "Vegetable":
            VegiesList.append(item)
        elif testDictionary[item]["Type of food"] == "Milk Product":
            MilkProductsList.append(item)
        elif testDictionary[item]["Type of food"] == "Nuts":
            NutsList.append(item)
        elif testDictionary[item]["Type of food"] == "Jam":
            JamsList.append(item)
        elif testDictionary[item]["Type of food"] == "Juice":
            JuicesList.append(item)
        else:
            raise Exception("Theres a type of food not spelt right!") #Stop the code if this happens




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
        self.Cart.append("Test")
        self.Cart.append("Test2")
        self.Cart.setMinimumSize(450,650)
        self.Cart.move(1000,10)

        self.Checkout = QtWidgets.QPushButton("Checkout", self)
        self.Checkout.setMinimumSize(220,130)
        self.Checkout.move(1230,670)
        self.Checkout.clicked.connect(self.CheckOut_Clicked)

        self.Clear = QtWidgets.QPushButton("Clear Cart", self)
        self.Clear.setMinimumSize(220,130)
        self.Clear.move(1000,670)
        self.Clear.clicked.connect(self.Clear_Clicked)

        #Add better buttons here, this is just for testing so far
        self.Food0 = QtWidgets.QPushButton(testDictionary["Food 0"]["Name"], self)
        self.Food0.setMinimumSize(130,130)
        self.Food0.move(100,500)
        self.Food0.setObjectName("Food 0")
        self.Food0.hide()
        self.Food0.clicked.connect(self.Food0Clicked)

        self.Food1 = QtWidgets.QPushButton(testDictionary["Food 1"]["Name"], self)
        self.Food1.setMinimumSize(130,130)
        self.Food1.setObjectName("Food 1")
        self.Food1.move(200,500)
        self.Food1.hide()
        self.Food1.clicked.connect(self.Food1Clicked)

        self.Food2 = QtWidgets.QPushButton(testDictionary["Food 2"]["Name"], self)
        self.Food2.setMinimumSize(130,130)
        self.Food2.setObjectName("Food 2")
        self.Food2.move(300,500)
        self.Food2.hide()
        self.Food2.clicked.connect(self.Food2Clicked)


        self.Food3 = QtWidgets.QPushButton(testDictionary["Food 3"]["Name"], self)
        self.Food3.setMinimumSize(130,130)
        self.Food3.move(400,500)
        self.Food3.setObjectName("Food 3")
        self.Food3.hide()
        self.Food3.clicked.connect(self.Food3Clicked)

        self.Food4 = QtWidgets.QPushButton(testDictionary["Food 4"]["Name"], self)
        self.Food4.setMinimumSize(130,130)
        self.Food4.move(500,500)
        self.Food4.setObjectName("Food 4")
        self.Food4.hide()
        self.Food4.clicked.connect(self.Food4Clicked)

        self.Food5 = QtWidgets.QPushButton(testDictionary["Food 5"]["Name"], self)
        self.Food5.setMinimumSize(130,130)
        self.Food5.setObjectName("Food 5")
        self.Food5.move(600,500)
        self.Food5.hide()
        self.Food5.clicked.connect(self.Food5Clicked)

        self.Food6 = QtWidgets.QPushButton(testDictionary["Food 6"]["Name"], self)
        self.Food6.setMinimumSize(130,130)
        self.Food6.setObjectName("Food 6")
        self.Food6.move(700,500)
        self.Food6.hide()
        self.Food6.clicked.connect(self.Food6Clicked)

        self.Food7 = QtWidgets.QPushButton(testDictionary["Food 7"]["Name"], self)
        self.Food7.setMinimumSize(130,130)
        self.Food7.setObjectName("Food 7")
        self.Food7.move(800,500)
        self.Food7.hide()
        self.Food7.clicked.connect(self.Food7Clicked)
        self.currentOrders = []
        self.show()
    #Code for buttons warning terrible code ahead


    def Veges_Clicked(self):
        #I need to find a better way to do this than 7 if statements
        #Temp solution i swear
        if self.Food0.objectName() in VegiesList:
            self.Food0.show()
        else: self.Food0.hide()
        if self.Food1.objectName() in VegiesList:
            self.Food1.show()
        else: self.Food1.hide()
        if self.Food2.objectName() in VegiesList:
            self.Food2.show()
        else: self.Food2.hide()
        if self.Food3.objectName() in VegiesList:
            self.Food3.show()
        else: self.Food3.hide()
        if self.Food4.objectName() in VegiesList:
            self.Food4.show()
        else: self.Food4.hide()
        if self.Food5.objectName() in VegiesList:
            self.Food5.show()
        else: self.Food5.hide()
        if self.Food6.objectName() in VegiesList:
            self.Food6.show()
        else: self.Food6.hide()
        if self.Food7.objectName() in VegiesList:
            self.Food7.show()
        else: self.Food7.hide()



        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Milk_Clicked(self):
        #I need to find a better way to do this than 7 if statements
        #Temp solution i swear
        if self.Food0.objectName() in MilkProductsList:
            self.Food0.show()
        else: self.Food0.hide()
        if self.Food1.objectName() in MilkProductsList:
            self.Food1.show()
        else: self.Food1.hide()
        if self.Food2.objectName() in MilkProductsList:
            self.Food2.show()
        else: self.Food2.hide()
        if self.Food3.objectName() in MilkProductsList:
            self.Food3.show()
        else: self.Food3.hide()
        if self.Food4.objectName() in MilkProductsList:
            self.Food4.show()
        else: self.Food4.hide()
        if self.Food5.objectName() in MilkProductsList:
            self.Food5.show()
        else: self.Food5.hide()
        if self.Food6.objectName() in MilkProductsList:
            self.Food6.show()
        else: self.Food6.hide()
        if self.Food7.objectName() in MilkProductsList:
            self.Food7.show()
        else: self.Food7.hide()





        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Nuts_Clicked(self):
        #I need to find a better way to do this than 7 if statements
        #Temp solution i swear
        if self.Food0.objectName() in NutsList:
            self.Food0.show()
        else: self.Food0.hide()
        if self.Food1.objectName() in NutsList:
            self.Food1.show()
        else: self.Food1.hide()
        if self.Food2.objectName() in NutsList:
            self.Food2.show()
        else: self.Food2.hide()
        if self.Food3.objectName() in NutsList:
            self.Food3.show()
        else: self.Food3.hide()
        if self.Food4.objectName() in NutsList:
            self.Food4.show()
        else: self.Food4.hide()
        if self.Food5.objectName() in NutsList:
            self.Food5.show()
        else: self.Food5.hide()
        if self.Food6.objectName() in NutsList:
            self.Food6.show()
        else: self.Food6.hide()
        if self.Food7.objectName() in NutsList:
            self.Food7.show()
        else: self.Food7.hide()




        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Jams_Clicked(self):
        #I need to find a better way to do this than 7 if statements
        #Temp solution i swear
        if self.Food0.objectName() in JamsList:
            self.Food0.show()
        else: self.Food0.hide()
        if self.Food1.objectName() in JamsList:
            self.Food1.show()
        else: self.Food1.hide()
        if self.Food2.objectName() in JamsList:
            self.Food2.show()
        else: self.Food2.hide()
        if self.Food3.objectName() in JamsList:
            self.Food3.show()
        else: self.Food3.hide()
        if self.Food4.objectName() in JamsList:
            self.Food4.show()
        else: self.Food4.hide()
        if self.Food5.objectName() in JamsList:
            self.Food5.show()
        else: self.Food5.hide()
        if self.Food6.objectName() in JamsList:
            self.Food6.show()
        else: self.Food6.hide()
        if self.Food7.objectName() in JamsList:
            self.Food7.show()
        else: self.Food7.hide()



        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Juices_Clicked(self):
        #I need to find a better way to do this than 7 if statements
        #Temp solution i swear
        if self.Food0.objectName() in JuicesList:
            self.Food0.show()
        else: self.Food0.hide()
        if self.Food1.objectName() in JuicesList:
            self.Food1.show()
        else: self.Food1.hide()
        if self.Food2.objectName() in JuicesList:
            self.Food2.show()
        else: self.Food2.hide()
        if self.Food3.objectName() in JuicesList:
            self.Food3.show()
        else: self.Food3.hide()
        if self.Food4.objectName() in JuicesList:
            self.Food4.show()
        else: self.Food4.hide()
        if self.Food5.objectName() in JuicesList:
            self.Food5.show()
        else: self.Food5.hide()
        if self.Food6.objectName() in JuicesList:
            self.Food6.show()
        else: self.Food6.hide()
        if self.Food7.objectName() in JuicesList:
            self.Food7.show()
        else: self.Food7.hide()




        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Fruits_Clicked(self):
        #I need to find a better way to do this than 7 if statements
        #Temp solution i swear
        if self.Food0.objectName() in FruitsList:
            self.Food0.show()
        else: self.Food0.hide()
        if self.Food1.objectName() in FruitsList:
            self.Food1.show()
        else: self.Food1.hide()
        if self.Food2.objectName() in FruitsList:
            self.Food2.show()
        else: self.Food2.hide()
        if self.Food3.objectName() in FruitsList:
            self.Food3.show()
        else: self.Food3.hide()
        if self.Food4.objectName() in FruitsList:
            self.Food4.show()
        else: self.Food4.hide()
        if self.Food5.objectName() in FruitsList:
            self.Food5.show()
        else: self.Food5.hide()
        if self.Food6.objectName() in FruitsList:
            self.Food6.show()
        else: self.Food6.hide()
        if self.Food7.objectName() in FruitsList:
            self.Food7.show()
        else: self.Food7.hide()




        #self.Cart.append("This is a test")
        #self.Food1.show()
        #self.Cart.append(random.randint(0, 10000)) This crashed it
        self.show()
    def Food0Clicked(self):
        self.Cart.append(f"{testDictionary['Food 0']['Name']}: {testDictionary['Food 0']['Price']}")
        self.currentOrders.append("Food 0")
    def Food1Clicked(self):
        self.Cart.append(f"{testDictionary['Food 1']['Name']}: {testDictionary['Food 1']['Price']}")
        self.currentOrders.append("Food 1")
    def Food2Clicked(self):
        self.Cart.append(f"{testDictionary['Food 2']['Name']}: {testDictionary['Food 2']['Price']}")
        self.currentOrders.append("Food 2")
    def Food3Clicked(self):
        self.Cart.append(f"{testDictionary['Food 3']['Name']}: {testDictionary['Food 3']['Price']}")
        self.currentOrders.append("Food 3")
    def Food4Clicked(self):
        self.Cart.append(f"{testDictionary['Food 4']['Name']}: {testDictionary['Food 4']['Price']}")
        self.currentOrders.append("Food 4")
    def Food5Clicked(self):
        self.Cart.append(f"{testDictionary['Food 5']['Name']}: {testDictionary['Food 5']['Price']}")
        self.currentOrders.append("Food 5")
    def Food6Clicked(self):
        self.Cart.append(f"{testDictionary['Food 6']['Name']}: {testDictionary['Food 6']['Price']}")
        self.currentOrders.append("Food 6")
    def Food7Clicked(self):
        self.Cart.append(f"{testDictionary['Food 7']['Name']}: {testDictionary['Food 7']['Price']}")
        self.currentOrders.append("Food 7")
    def Clear_Clicked(self):
        self.Cart.setText("")
        self.currentOrders = []
    def CheckOut_Clicked(self):
        total = 0
        for item in self.currentOrders:
            total += testDictionary[item]["RawPrice"]
        print(total)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = TestUI()
    app.exec_()


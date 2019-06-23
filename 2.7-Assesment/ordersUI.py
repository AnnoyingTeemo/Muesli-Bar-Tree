with open("Orders.json", "r") as f: Orders = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices
import sys, random
from collections import Counter
from PyQt5 import QtWidgets


currentOrders = {}
print(Orders)

for order in Orders:
    print(order)

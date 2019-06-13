foods = open("Foods.txt", "r")

testDictionary = {}
testList = []
amountOfWords = 0
for word in foods:
    amountOfWords += 1
for i in range(amountOfWords):
    testDictionary["Food Name {}".format(i)] = foods.readline().rstrip()

print(testDictionary)

foods.close()

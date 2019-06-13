foods = open("Foods.txt", "r")

testDictionary = {}
testList = []
amountOfWords = 0
i = 0
for word in foods:
    food = {
        "Name": word.strip().split()[0],
        "Price": '${}'.format(word.strip().split()[1])
    }
    testDictionary["Food {}".format(i)] = food
    i += 1

print(testDictionary)

foods.close()

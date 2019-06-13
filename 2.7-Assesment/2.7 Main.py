with open("Foods.txt", "r") as f: foods = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices

testDictionary = {}
testList = []
amountOfWords = 0
i = 0
for word in foods:
    food = {
        "Name": word.strip().split()[0].replace('_', ' '),
        "Type of food": word.strip().split()[1].replace('_', ' '),
        #"Price": '${}'.format(word.strip().split()[2]),
        "Price": f'${word.strip().split()[2]}',
    }
    testDictionary["Food {}".format(i)] = food
    i += 1

print(testDictionary)

# foods.close()
#

with open("Foods.txt", "r") as f: foods = f.readlines()
#fruits, vegies, milk products, nuts, jams, juices

testDictionary = {
    "Fruit": {},
    "Vegetable": {},
    "Milk Product": {},
    "Nuts": {},
    "Jam": {},
    "Juice": {}
}
testList = []
amountOfWords = 0
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
#

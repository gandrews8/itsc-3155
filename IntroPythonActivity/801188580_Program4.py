nameList = []
priceList = []
maxItems = int(input("Enter number of items: "))
x = 0
for x in range(0,maxItems):
    nameToAdd = ""
    priceToAdd = ""
    thing = input("Enter item name and price: ")
    thingList = list(thing)
    for y in thingList:
        if (y != ' ' and y.isnumeric() == False):
            nameToAdd = nameToAdd + y
        else:
            priceToAdd = priceToAdd + y
    nameList.append(nameToAdd)
    priceList.append(priceToAdd)
for x in range(0,maxItems):
    print(nameList[x] + priceList[x])

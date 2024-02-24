myList = [0, 1]

# Change '20' in range function below to change how much of the sequence is printed

for i in range(0, 20):
    myList.append(myList[(len(myList) - 1)] + myList[((len(myList) - 2))])
    print(myList[i])


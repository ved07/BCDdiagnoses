from MLP import multiLayeredPerceptron

network = multiLayeredPerceptron()

initialisedData = network.dataFrameInit('Dataset.csv')

initialisedTestData = network.dataFrameInit('testDataset.csv')

mlp = network.runNeuralNet(dataFrame=initialisedData)

for x in range(6) :
    pred = network.predict(initialisedTestData,initialisedData, x, mlp)
    while pred == None:
        mlp = network.runNeuralNet(dataFrame=initialisedData)
        pred = network.predict(initialisedTestData, initialisedData, x, mlp)
    print(pred)


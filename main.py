from MLP import multiLayeredPerceptron

network = multiLayeredPerceptron()

initialisedData = network.dataFrameInit('Dataset.csv')

initialisedTestData = network.dataFrameInit('testDataset.csv')

mlp = network.runNeuralNet(dataFrame=initialisedData)



print(network.initPredData(initialisedData, ['Coughs']))
print(network.initPredData(initialisedData, ['Coughs'])['Coughs'])
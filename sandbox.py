from mlp import multiLayeredPerceptron

network = multiLayeredPerceptron()
initialisedData = network.dataFrameInit('data.csv')
commonality = network.dataFrameInit('commonality.csv')
symp_arr = ['Coughs','fever','Loss of smell']
diag = network.initPredData(initialisedData, symp_arr)
pred = network.predLoop(predData=diag, dataframe=initialisedData, commonality=commonality)
print(pred)
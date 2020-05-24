import encoding
from sklearn.neural_network import MLPClassifier
import pandas as pd


class multiLayeredPerceptron():
    def __init__(self):
        encoder = encoding.encoder()
        self.encoder = encoder
    def dataFrameInit(self, dataFileName):
        dataFrame = pd.read_csv(dataFileName)
        dataFrame = dataFrame.fillna(0.)

        return dataFrame

    def extractValues(self, dataframe):
        dataframe = dataframe.drop('Disease', axis=1)
        values = dataframe.values
        return values

    def train(self, classifier, X_data, y):
        y = self.encoder.oneHotEncode(array=y)
        classifier.fit(X=X_data, y=y)

    def predict(self, dataFrame, position, classifier):
        value = self.extractValues(dataFrame)
        value = classifier.predict(value[position].reshape(1, -1))
        value = list(value[0])
        return self.encoder.decode(array=value, strings=list(dataFrame['Disease']))

    def runNeuralNet(self, dataFrame):
        classifier = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10,9,8, 7), max_iter=5000000)
        self.train(classifier, self.extractValues(dataFrame), dataFrame['Disease'])
        return classifier

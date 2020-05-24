import pandas as pd

import numpy as np

class encoder():

    def __init__(self):

        self = []

    def oneHotEncode(self, array):

        encodedArray = []

        numericArray = list(range(len(array)))

        for value in numericArray:

            ind = numericArray.index(value)

            endArray = np.zeros(shape=[len(array)])

            endArray[ind] = 1

            endArray = endArray.tolist()

            encodedArray.append(endArray)

        return encodedArray

    def decode(self, array,strings):

        for number in array:

            if number == 1:

                return strings[array.index(number)]



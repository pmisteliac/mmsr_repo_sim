import numpy
import os
from CsvHelper import read
from Validator import validateTopicModel


def randomTest(validationNames, iterations = 1000):
    accuracy = 0
    idNameValidationDict = dict()
    for index in range(len(validationNames)):
        idNameValidationDict[index] = validationNames[index]

    for _ in range(iterations):
        similarityMatrix = numpy.random.rand(len(validationNames), len(validationNames))
        accuracy += validateTopicModel(similarityMatrix, idNameValidationDict)

    print("Random accuracy:", accuracy / iterations)


# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    currentDir = os.path.dirname( __file__ )
    inputPathRaw = os.path.join(currentDir, '..', 'term_extractor/result/repos.csv')
    inputPath = os.path.abspath(inputPathRaw)

    validationNames, validationFeatures = read(inputPath)
    randomTest(validationNames)


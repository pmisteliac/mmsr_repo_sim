from Evaluation import evaluateModels, plot, selectTopicModel
from TopicModeler import modelTopics
from Similarity import calculateSimilarity
from CsvHelper import read, write, createDir
from Validator import validateTopicModel
import os
import time
import datetime


def experiment():
    currentDir = os.path.dirname( __file__ )
    inputPathCuratedRaw = os.path.join(currentDir, '..', 'term_extractor/result/curated_repos_nocom.csv')
    inputPathCurated = os.path.abspath(inputPathCuratedRaw)

    inputPathTrainingRaw = os.path.join(currentDir, '..', 'term_extractor/result/top_repos_nocom.csv')
    inputPathTraining = os.path.abspath(inputPathTrainingRaw)

    validationNames, validationFeatures, trainingNames, trainingFeatures = [], [], [], []
    validationNames, validationFeatures = read(inputPathCurated)
    trainingNames, trainingFeatures =  read(inputPathTraining)
    for i in range(17,22):
        now = datetime.datetime.now()
        dateTime = now.strftime("%d-%m-%Y-%H-%M")
        experimentDescription = str(i) + '_' + dateTime + "_FullCorpus-NoComments"
        pipeline(experimentDescription, trainingNames, validationNames, trainingFeatures, validationFeatures)


def pipeline(description, trainingNames, validationNames, trainingFeatureLists, valiationFeatureLists):
    print('\n-----------------------NEW EXPERIMENT-----------------------')
    print(description, '\n')

    startTime = time.time()

    currentDir = os.path.dirname( __file__ )
    experimentPathRaw = os.path.join(currentDir, '..', "results/" + description)
    experimentPath = os.path.abspath(experimentPathRaw)

    # generate a topic model from the raw input, with each document in the model representing an entire repository
    # (topicModels, dictionary, corpus, processedFeatures, topicCounts)
    documentFeatureLists = valiationFeatureLists + trainingFeatureLists
    repositoryNames = validationNames + trainingNames

    topicLimit = min(128, len(repositoryNames) - 1)
    topicModels, dictionary, corpus, repositoryFeatures, topicCounts, alphas, betas = modelTopics(documentFeatureLists, 2, topicLimit)

    # evaluate the generated models to find the best one
    silhouetteScores, coherenceScores = evaluateModels(topicModels, topicCounts, dictionary, corpus, repositoryFeatures)
    parameters = [str(topicCount) + "; " + alpha + "; " + beta for topicCount, alpha, beta in zip(topicCounts, alphas, betas)]
    # plot(parameters, silhouetteScores, "silhouetteScore", "# topics, alpha, beta")

    print('Silhouette Scores:', silhouetteScores)
    print('Coherence Scores:', coherenceScores)
    # select the best topic model based in the coherenceScores
    finalModel, modelIndex = selectTopicModel(topicModels, silhouetteScores, coherenceScores)

    # create a similarity matrix for all documents in the topic model
    similarityMatrix = calculateSimilarity(finalModel, corpus)

    idNameDict = dict()
    for index in range(len(documentFeatureLists)):
        idNameDict[index] = repositoryNames[index]
    accuracy = validateTopicModel(similarityMatrix, idNameDict, range(len(validationNames)))

    endTime = time.time()
    executionTime = endTime - startTime

    # results
    createDir(experimentPath)
    print('\n-----------------------RESULTS-----------------------')
    print('Model with index', modelIndex, 'has an accuracy of', accuracy, ' and took: ', executionTime, 'seconds.')
    print('Parameters:', parameters[modelIndex])
    print('Silhouette Score:', silhouetteScores[modelIndex])
    print('Coherence Score:', coherenceScores[modelIndex])
    print('\nSimilarity matrix:', similarityMatrix)
    print('-----------------------END RESULTS-----------------------\n')


    # save experiment data
    dumpExperimentResults = [('Model Index', modelIndex), ('Execution Time', executionTime), ('Model Accuracy', accuracy), ('Parameters', parameters), ('Silhouette Scores', silhouetteScores), ('Coherence Scores', coherenceScores), ('Similarity Matrix', similarityMatrix)]
    write(experimentPath + "/results.csv", dumpExperimentResults)
    write(experimentPath + "/processedFeatures.csv", repositoryFeatures)
    print('-----------------------FINISH-----------------------\n')


# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    experiment().runInParallel(numProcesses=4, numThreads=8)


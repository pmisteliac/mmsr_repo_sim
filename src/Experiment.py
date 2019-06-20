from Evaluation import evaluateModels, plot, selectTopicModel
from TopicModeler import modelTopics
from Similarity import calculateSimilarity
from CsvHelper import read, write, createDir
from Validator import validateTopicModel
import os
import time


def run(description, trainingNames, validationNames, trainingFeatureLists, valiationFeatureLists):
    startTime = time.time()

    experimentPath = "results/" + description

    # generate a topic model from the raw input, with each document in the model representing an entire repository
    # (topicModels, dictionary, corpus, processedFeatures, topicCounts)
    documentFeatureLists = valiationFeatureLists + trainingFeatureLists
    repositoryNames = validationNames + trainingNames
    topicModels, dictionary, corpus, repositoryFeatures, topicCounts, alphas, betas = modelTopics(documentFeatureLists, 16, 64)

    # evaluate the generated models to find the best one
    silhouetteScores, coherenceScores = evaluateModels(topicModels, topicCounts, dictionary, corpus, repositoryFeatures)
    parameters = [str(topicCount) + "; " + alpha + "; " + beta for topicCount, alpha, beta in zip(topicCounts, alphas, betas)]
    # plot(parameters, silhouetteScores, "silhouetteScore", "# topics, alpha, beta")

    print('Silhouette Scores:', silhouetteScores)
    print('Coherence Scores:', coherenceScores)
    # select the best topic model based in the coherenceScores
    finalModel, modelIndex = selectTopicModel(topicModels, silhouetteScores)

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
    print('-----------------------FINISH-----------------------\n')

    # save experiment data
    dumpExperimentResults = [('Model Index', modelIndex), ('Execution Time', executionTime), ('Final Model Accuracy', accuracy), ('Parameters', parameters), ('Silhouette Scores', silhouetteScores), ('Coherence Scores', coherenceScores), ('Final Similarity matrix', similarityMatrix)]
    write(experimentPath + "/results.csv", dumpExperimentResults)
    write(experimentPath + "/processedFeatures.csv", repositoryFeatures)


# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    currentDir = os.path.dirname( __file__ )
    inputPathCuratedRaw = os.path.join(currentDir, '..', 'term_extractor/result/curated_repos.csv')
    inputPathCurated = os.path.abspath(inputPathCuratedRaw)

    inputPathTrainingRaw = os.path.join(currentDir, '..', 'term_extractor/result/top_repos.csv')
    inputPathTraining = os.path.abspath(inputPathTrainingRaw)

    validationNames, validationFeatures, trainingNames, trainingFeatures = [], [], [], []
    validationNames, validationFeatures = read(inputPathCurated)
    trainingNames, trainingFeatures =  read(inputPathTraining)
    experimentDescription = "04_20-06-Full-Comments"
    run(experimentDescription, trainingNames, validationNames, trainingFeatures, validationFeatures).runInParallel(numProcesses=4, numThreads=8)


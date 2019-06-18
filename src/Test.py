from Evaluation import evaluateModels, plot, selectTopicModel
from TopicModeler import modelTopics
from Similarity import calculateSimilarity
from CsvHelper import read, write, createDir
from Validator import validateTopicModel
import os


def run(description, trainingNames, validationNames, trainingFeatureLists, valiationFeatureLists):
    experimentPath = "results/" + description

    # generate a topic model from the raw input, with each document in the model representing an entire repository
    # (topicModels, dictionary, corpus, processedFeatures, topicCounts)
    documentFeatureLists = valiationFeatureLists + trainingFeatureLists
    topicModels, dictionary, corpus, repositoryFeatures, topicCounts, alphas, betas = modelTopics(documentFeatureLists, 2, 16)

    # evaluate the generated models to find the best one
    silhouetteScores, coherenceScores, perplexityScores = evaluateModels(topicModels, topicCounts, dictionary, corpus, repositoryFeatures)
    parameters = [str(topicCount) + "; " + alpha + "; " + beta for topicCount, alpha, beta in zip(topicCounts, alphas, betas)]
    # plot(parameters, silhouetteScores, "silhouetteScore", "# topics, alpha, beta")

    # select the best topic model based in the coherenceScores
    finalModel = selectTopicModel(topicModels, silhouetteScores)

    # create a similarity matrix for all documents in the topic model
    similarityMatrix = calculateSimilarity(finalModel, corpus)

    idNameValidationDict = dict()
    for index in range(len(validationNames)):
        idNameValidationDict[index] = validationNames[index]
    accuracy = validateTopicModel(similarityMatrix, idNameValidationDict)

    # results
    createDir(experimentPath)
    print('-----------------------RESULTS-----------------------')
    print('Final Model Accuracy:\n', accuracy)
    print('Parameters:\n', parameters)
    print('Silhouette Scores:\n', silhouetteScores)
    print('Coherence Scores:\n', coherenceScores)
    print('Final Similarity matrix:\n', similarityMatrix)


    # save experiment data
    write(experimentPath + "/silhouetteScores.csv", silhouetteScores)
    write(experimentPath + "/similarityMatrix.csv", similarityMatrix)
    write(experimentPath + "/parameters.csv", parameters)
    write(experimentPath + "/coherenceScores.csv", coherenceScores)
    write(experimentPath + "/processedFeatures.csv", repositoryFeatures)
    write(experimentPath + "/coherenceScores.csv", coherenceScores)


# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    currentDir = os.path.dirname( __file__ )
    inputPathRaw = os.path.join(currentDir, '..', 'term_extractor/result/repos.csv')
    inputPath = os.path.abspath(inputPathRaw)

    validationNames, validationFeatures = read(inputPath)
    experimentDescription = "02_18-06"
    run(experimentDescription, [], validationNames, [], validationFeatures).runInParallel(numProcesses=4, numThreads=8)

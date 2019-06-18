from Evaluation import evaluateModels, plot, selectTopicModel
from TopicModeler import modelTopics
from Similarity import calculateSimilarity
from CsvHelper import read, write, createDir
import os

# Test Input:
testFeatureList01 = ['client_side', 'server', 'http', 'responseHandler', 'request.empty', 'request', 'open', 'close', 'shutdown', 'a', "isA", "isa"]
testFeatureList02 = ['ssl', 'http', 'client', 'timeout_error', 'connection', 'request', 'API', 'restful', 'none', "is"]

testFeatureList03 = ['server', 'ssl', 'https', 'requester', 'empty', 'request', 'send', 'receive', 'close', 'await', "respond", "bind"]
testFeatureList04 = ['route', 'http', 'communication', 'connection', 'timedout', 'pass', 'request', 'HttpRoute', 'startServer', "shutdownServer"]

testFeatureList05 = ['client_side', 'servlet', 'http', 'handler', 'request.empty', 'request', 'ongoing', 'close', 'end', 'a', "isA", "isa"]
testFeatureList06 = ['tls', 'https', 'clientside', 'timeout_error', 'connection', 'request', 'API', 'restful', 'none', "is"]

testFeatureLists01 = [testFeatureList01, testFeatureList02]
testFeatureLists02 = [testFeatureList03, testFeatureList04]
testFeatureLists03 = [testFeatureList05, testFeatureList06]


def run(description, names, documentFeatureLists):
    experimentPath = "results/" + description
    createDir(experimentPath)

    # generate a topic model from the raw input, with each document in the model representing an entire repository
    # (topicModels, dictionary, corpus, processedFeatures, topicCounts)
    topicModels, dictionary, corpus, repositoryFeatures, topicCounts, alphas, betas = modelTopics(documentFeatureLists, 2, 8)
    write(experimentPath + "/processedFeatures.csv", repositoryFeatures)

    # evaluate the generated models to find the best one
    silhouetteScores, coherenceScores, perplexityScores = evaluateModels(topicModels, topicCounts, dictionary, corpus, repositoryFeatures)
    parameters = [str(topicCount) + "; " + alpha + "; " + beta for topicCount, alpha, beta in zip(topicCounts, alphas, betas)]
    # plot(parameters, silhouetteScores, "silhouetteScore", "# topics, alpha, beta")

    # select the best topic model based in the coherenceScores
    finalModel = selectTopicModel(topicModels, silhouetteScores)

    # create a similarity matrix for all documents in the topic model
    similarityMatrix = calculateSimilarity(finalModel, corpus)

    print(similarityMatrix)
    write(experimentPath + "/similarityMatrix.csv", similarityMatrix)
    print(parameters)
    write(experimentPath + "/parameters.csv", parameters)
    print(silhouetteScores)
    write(experimentPath + "/silhouetteScores.csv", [str(score) for score in silhouetteScores])


# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    currentDir = os.path.dirname( __file__ )
    inputPathRaw = os.path.join(currentDir, '..', 'term_extractor/result/repos.csv')
    inputPath = os.path.abspath(inputPathRaw)

    names, repositoryFeatures = read(inputPath)
    experimentDescription = "01_18-06"
    run(experimentDescription, names, repositoryFeatures).runInParallel(numProcesses=4, numThreads=8)


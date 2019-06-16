from Evaluation import evaluateModels, plot, selectTopicModel
from TopicModeler import modelTopics
from Similarity import calculateSimilarity


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


def run(names, documentFeatureLists):
    # generate a topic model from the raw input, with each document in the model representing an entire repository
    # (topicModels, dictionary, corpus, processedFeatures, topicCounts)
    topicModels, dictionary, corpus, repositoryFeatures, topicCounts = modelTopics(documentFeatureLists, 4, 4)

    # evaluate the generated models to find the best one
    coherenceScores, perplexityScores = evaluateModels(topicModels, dictionary, corpus, repositoryFeatures)
    # plot(name, topicCounts, coherenceScores, perplexityScores)

    # select the best topic model based in the coherenceScores
    finalModel = selectTopicModel(topicModels, coherenceScores)

    # create a similarity matrix for all documents in the topic model
    similarityMatrix = calculateSimilarity(names, finalModel, corpus)
    print(similarityMatrix)


# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    names = ["test01", "test02", "test03"]
    repositoryFeatures = [testFeatureLists01, testFeatureLists02, testFeatureLists03]
    run(names, repositoryFeatures).runInParallel(numProcesses=4, numThreads=8)


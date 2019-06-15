from Evaluation import evaluateModels
from TopicModeler import modelTopics

# Test Input:
testFeatureList01 = ['client_side', 'server', 'http', 'responseHandler', 'request.empty', 'request', 'open', 'close', 'shutdown', 'a', "isA", "isa"]
testFeatureList02 = ['ssl', 'http', 'client', 'timeout_error', 'connection', 'request', 'API', 'restful', 'none', "is"]

testFeatureList03 = ['server', 'ssl', 'https', 'requester', 'empty', 'request', 'send', 'receive', 'close', 'await', "respond", "bind"]
testFeatureList04 = ['route', 'http', 'communication', 'connection', 'timedout', 'pass', 'request', 'HttpRoute', 'startServer', "shutdownServer"]

testFeatureLists01 = [testFeatureList01, testFeatureList02]
testFeatureLists02 = [testFeatureList03, testFeatureList04]


def run(featureLists):
    # topicModels, dictionary, corpus, processedFeatures, topicCounts
    modeled = [ modelTopics(features, 2, 256) for features in featureLists]

    for (topicModels, dictionary, corpus, processedFeatures, topicCounts) in modeled:
        evaluateModels(topicModels, dictionary, corpus, processedFeatures, topicCounts)

# execute in parallel, otherwise it takes to long
if __name__ == '__main__':
    run([testFeatureLists01, testFeatureLists02]).runInParallel(numProcesses=4, numThreads=8)


# Gensim
from gensim.models import CoherenceModel, ldamodel
# Custom
from CorpusBuilder import buildCorpus
from Preprocessor import preProcess
from Evaluation import evaluateModels
# Other
from typing import List, Any
import math


def modelTopics(featureLists: List[List[str]], topicMin = 2, topicLimit = 256) -> List[List[str]]:
    print('\nRaw input:', featureLists)

    processedFeatures = preProcess(featureLists)
    print('\nPre processed input:', processedFeatures)

    dictionary, corpus = buildCorpus(processedFeatures)
    print('\nCorpus (Dictionary, Bag of Words):', corpus)

    topicCounts = [1 << exponent for exponent in range(int(math.log(topicMin, 2)), int(math.log(topicLimit, 2)) + 1)]
    topicModels = generateTopicModels(dictionary, corpus, topicCounts)

    evaluateModels(topicModels, dictionary, corpus, processedFeatures, topicCounts)


def generateTopicModels( dictionary, bow, topicCounts):
    models = []
    for amountTopics in topicCounts:
        ldaModel = ldamodel.LdaModel(bow, amountTopics, dictionary, passes=20, alpha='auto', per_word_topics=True)
        models.append((amountTopics, ldaModel))
    return models


# Test Input:
testFeatureList01 = ['client_side', 'server', 'http', 'responseHandler', 'request.empty', 'request', 'open', 'close', 'shutdown', 'a', "isA", "isa"]
testFeatureList02 = ['ssl', 'http', 'client', 'timeout_error', 'connection', 'request', 'API', 'restful', 'none', "is"]
testFeatureLists = [testFeatureList01, testFeatureList02]


# execute in parallel, otherwise it taks to long
if __name__ == '__main__':
    modelTopics(testFeatureLists, 2, 256).runInParallel(numProcesses=4, numThreads=8)

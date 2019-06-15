# Gensim
import gensim
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, ldamodel
# Custom
from CorpusBuilder import buildCorpus
from Preprocessor import preProcess
from Evaluation import evaluateModel
# Other
from typing import List, Any
import math


def modelTopics(featureLists: List[List[str]]) -> List[List[str]]:
    print('\nRaw input:', featureLists)

    processedFeatures = preProcess(featureLists)
    print('\nPre processed input:', processedFeatures)

    dictionary, corpus = buildCorpus(processedFeatures)
    print('\nCorpus (Dictionary, Bag of Words):', corpus)

    topicModels = generateTopicModels(dictionary, corpus, 256)
    for (amountTopics, topicModel) in topicModels:
        evaluateModel(topicModel, dictionary, corpus, processedFeatures, amountTopics)


def generateTopicModels( dictionary, bow, limit, start = 2):
    topicCounts = [1<< x for x in range(int(math.log(start, 2)), int(math.log(limit, 2)) + 1)]
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
    modelTopics(testFeatureLists).runInParallel(numProcesses=4, numThreads=8)

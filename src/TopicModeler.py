# Gensim
from gensim.models import CoherenceModel, ldamodel, wrappers
# Custom
from CorpusBuilder import buildCorpus
from Preprocessor import preProcess
# Other
from typing import List, Any
import math
import os

def modelTopics(featureLists: List[List[str]], topicMin = 2, topicLimit = 256):
    print('\nRaw input:', featureLists)

    processedFeatures = preProcess(featureLists)
    print('\nPre processed input:', processedFeatures)

    dictionary, corpus = buildCorpus(processedFeatures)
    print('\nCorpus (Dictionary, Bag of Words):', corpus)

    topicCounts = [1 << exponent for exponent in range(int(math.log(topicMin, 2)), int(math.log(topicLimit, 2)) + 1)]

    # topicModels = generateTopicModelsMallet(dictionary, corpus, topicCounts)
    topicModels = generateTopicModels(dictionary, corpus, topicCounts)

    return topicModels, dictionary, corpus, processedFeatures, topicCounts


def generateTopicModels(dictionary, bow, topicCounts):
    models = []
    for amountTopics in topicCounts:
        ldaModel = ldamodel.LdaModel(bow, amountTopics, dictionary, passes=20, alpha='auto', per_word_topics=True)
        models.append((amountTopics, ldaModel))
    return models


# buggy on windows systems, because gensim cannot resolve windows path properly
def generateTopicModelsMallet(dictionary, bow, topicCounts):
    pathMalletEnvironment = os.path.abspath('C:/Users/Jan/mallet-2.0.8')
    os.environ['MALLET_HOME'] = pathMalletEnvironment
    pathMallet = os.path.abspath('C:/Users/Jan/mallet-2.0.8/bin/mallet')
    models = []
    for amountTopics in topicCounts:
        ldamallet = wrappers.LdaMallet(pathMallet, corpus=bow, num_topics=amountTopics, id2word=dictionary)
        models.append((amountTopics, ldamallet))
    return models
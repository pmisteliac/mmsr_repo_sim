# Gensim
from gensim.models import ldamodel, wrappers
# Custom
from CorpusBuilder import buildCorpus
from Preprocessor import preProcess
from Utils import flatten
from Importer import write
# Other
from typing import List
import math
import os


def modelTopics(featureLists: List[List[List[str]]], topicMin = 2, topicLimit = 256):
    # combine all terms from a single repository into one document/ term list in order to compare the repositories later easily
    combinedFeatureLists = [flatten(featureList) for featureList in featureLists]
    write("combinedFeatureLists.csv", combinedFeatureLists)

    processedFeatures = preProcess(combinedFeatureLists)
    write("processedFeatures.csv", processedFeatures)

    dictionary, corpus = buildCorpus(processedFeatures)

    topicCounts = [1 << exponent for exponent in range(int(math.log(topicMin, 2)), int(math.log(topicLimit, 2)) + 1)]
    topicModels, alphas, betas = generateTopicModels(dictionary, corpus, topicCounts)

    return topicModels, dictionary, corpus, processedFeatures, topicCounts, alphas, betas


def generateTopicModels(dictionary, bow, topicCounts):
    models = []
    alphas = ['auto' for _ in topicCounts]
    betas = alphas
    for amountTopics in topicCounts:
        ldaModel = ldamodel.LdaModel(bow, amountTopics, dictionary, passes=20, alpha='auto', eta='auto', per_word_topics=True)
        models.append(ldaModel)
    return models, alphas, betas


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


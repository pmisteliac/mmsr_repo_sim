import gensim
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, ldamodel
import matplotlib.pyplot as plt

def evaluateModel(topicModel, dict, bow, processedFeatures):
    print('\nPerplexity Score: ', computePerplexityScore(topicModel, bow))
    modelList, coherenceScores = computeCoherenceScores(dict, bow, processedFeatures, 255)
    print(modelList)
    print(coherenceScores)

def computePerplexityScore(topicModel, bow):
    perplexity = topicModel.log_perplexity(bow)
    return perplexity

def computeCoherenceScores(dictionary, bow, features, limit, start = 2):
    coherenceScores = []
    coherenceScores = []
    models = []
    topicCounts = []
    for amountTopics in topicCounts:
        ldaModel = ldamodel.LdaModel(bow, dictionary, amountTopics)
        models.append(ldaModel)

        coherenceModel = CoherenceModel(ldaModel, features, dictionary, 'c_v')
        coherenceScores.append(coherenceModel.get_coherence())

    return models, coherenceScores


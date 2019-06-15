import gensim
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel, ldamodel
import matplotlib.pyplot as plt


def evaluateModel(topicModel, dict, bow, features, amountTopics):
    print('\nTopic Model with ', amountTopics, " topics: ", topicModel.print_topics())
    perplexityScore = computePerplexityScore(topicModel, bow)
    print('Perplexity Score: ', perplexityScore)
    coherenceScore = computeCoherenceScores(topicModel, dict, features)
    print('Coherence Score: ', coherenceScore)
    return perplexityScore, coherenceScore


def computePerplexityScore(topicModel, bow):
    perplexity = topicModel.log_perplexity(bow)
    return perplexity


def computeCoherenceScores(topicModel, dictionary, features):
    coherenceModel = CoherenceModel(model=topicModel, texts=features, dictionary=dictionary, coherence='c_v')
    return coherenceModel.get_coherence()


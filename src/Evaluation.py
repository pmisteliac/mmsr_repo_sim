from gensim.models import CoherenceModel, ldamodel
import matplotlib.pyplot as plotter


# evaluate the topic model by calculating coherence and perplexity scores
def evaluateModels(topicModels, dictionary, corpus, features):
    coherenceScores = []
    perplexityScores = []
    for topicModel in topicModels:
        perplexityScore, coherenceScore = evaluateModel(topicModel, dictionary, corpus, features)
        coherenceScores.append(coherenceScore)
        perplexityScores.append(perplexityScore)

    return coherenceScores, perplexityScores


def evaluateModel(topicModel, dict, bow, features):
    perplexityScore = computePerplexityScore(topicModel, bow)
    coherenceScore = computeCoherenceScores(topicModel, dict, features)
    return perplexityScore, coherenceScore


def computePerplexityScore(topicModel, bow):
    perplexity = topicModel.log_perplexity(bow)
    return perplexity


def computeCoherenceScores(topicModel, dictionary, features):
    coherenceModel = CoherenceModel(model=topicModel, texts=features, dictionary=dictionary, coherence='c_v')
    return coherenceModel.get_coherence()


# select the best topic model from the given models for a specific corpus
def selectTopicModel(topicModels, coherenceScores):
    bestIndex = coherenceScores.index(min(coherenceScores))
    return topicModels[bestIndex]


def plot(name, topicCount, coherenceScores, perplexityScores):
    plotter.semilogx(topicCount, coherenceScores, basex=2)
    plotter.xlabel("# Topics")
    plotter.ylabel("Coherence Score")
    plotter.legend(name + " coherence scores", loc='best')
    plotter.show()

    plotter.semilogx(topicCount, perplexityScores, basex=2)
    plotter.xlabel("# Topics")
    plotter.ylabel("Perplexity Score")
    plotter.legend(name + " perplexity scores", loc='best')
    plotter.show()


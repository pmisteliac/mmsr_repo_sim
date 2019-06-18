from gensim.models import CoherenceModel, ldamodel
import matplotlib.pyplot as plotter
from sklearn.cluster import KMeans
from sklearn import metrics

from Similarity import calculateSimilarity


# evaluate the topic model by calculating coherence and perplexity scores
def evaluateModels(topicModels, topicCounts, dictionary, corpus, features):
    coherenceScores = []
    silhouetteScores = []
    perplexityScores = []
    for topicModel, topicCount in zip(topicModels, topicCounts):
        silhouetteScore, perplexityScore, coherenceScore = evaluateModel(topicModel, topicCount, dictionary, corpus, features)
        coherenceScores.append(coherenceScore)
        perplexityScores.append(perplexityScore)
        silhouetteScores.append(silhouetteScore)

    return silhouetteScores, coherenceScores, perplexityScores


def evaluateModel(topicModel,topicCount, dict, bow, features):
    perplexityScore = computePerplexityScore(topicModel, bow)
    coherenceScore = computeCoherenceScores(topicModel, dict, features)
    silhouetteScore = computeSilhouetteCoefficient(calculateSimilarity(topicModel, bow), topicCount)
    return silhouetteScore, perplexityScore, coherenceScore


# Coherence Score
def computePerplexityScore(topicModel, bow):
    perplexity = topicModel.log_perplexity(bow)
    return perplexity


# Perplexity Score
def computeCoherenceScores(topicModel, dictionary, features):
    coherenceModel = CoherenceModel(model=topicModel, texts=features, dictionary=dictionary, coherence='c_v')
    return coherenceModel.get_coherence()


# Silhouette Coefficient
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
def computeSilhouetteCoefficient(similarityMatrix, topicCount):
    labels = cluster(similarityMatrix, topicCount).labels_
    return metrics.silhouette_score(similarityMatrix, labels, metric="precomputed")


def cluster(similarityMatrix, topicCount):
    kmeans = KMeans(n_clusters = topicCount)
    return kmeans.fit(similarityMatrix)


# select the best topic model from the given models for a specific corpus
def selectTopicModel(topicModels, silhouetteScores):
    bestIndex = silhouetteScores.index(max(silhouetteScores))
    return topicModels[bestIndex]


def plot(parameters, scores, scoreDescrption, parameterDescription):
    plotter.yticks(parameters, scores)
    plotter.xlabel(parameterDescription)
    plotter.ylabel("Coherence Score")
    plotter.legend(scoreDescrption + " distribution by parameterization", loc='best')
    plotter.show()


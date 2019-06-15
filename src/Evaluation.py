from gensim.models import CoherenceModel, ldamodel
import matplotlib.pyplot as plotter


def evaluateModels(topicModels, dictionary, corpus, features, topicCounts):
    coherenceScores = []
    perplexityScores = []
    for (amountTopics, topicModel) in topicModels:
        perplexityScore, coherenceScore = evaluateModel(topicModel, dictionary, corpus, features, amountTopics)
        coherenceScores.append(coherenceScore)
        perplexityScores.append(perplexityScore)

    plot(topicCounts, coherenceScores, perplexityScores)


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


def plot(topicCounts, coherenceScores, perplexityScores):
    plotter.plot(topicCounts, coherenceScores)
    plotter.xlabel("# Topics")
    plotter.ylabel("Coherence Score")
    plotter.legend("coherence scores", loc='best')
    plotter.show()

    plotter.plot(topicCounts, perplexityScores)
    plotter.xlabel("# Topics")
    plotter.ylabel("Perplexity Score")
    plotter.legend("perplexity scores", loc='best')
    plotter.show()


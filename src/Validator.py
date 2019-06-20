from typing import List
from Similarity import intersection
from Utils import flatten


# Validate the generated similarity matrix against our validation matrix
# densely populated similarity matrix generated by the topic model, indicating the similarity of each document to the others
# dictionary of all names of the repository in the topic model, mapping the id of the repository document in the similarity matrix to the name of the repository
# Returns a validation score from 0 - 1, higher is better
# the validation score, represents the percentage of correct similarity rankings for each repository of the validation corpus
def validateTopicModel(similarityMatrix, idNameDictionary, validationIndices) -> float:
    accuracySum = 0

    for validationIndex in validationIndices:
        repositoryName = idNameDictionary[validationIndex]

        # get the n most similar repositories to the current one, with n beeing the number of expected similar repositories plus 1
        n = len(getValidatedSimilarRepository(repositoryName))
        topTenSimilarRepositoryIndices = getNmostSimilarRepositories(similarityMatrix, validationIndex, n)
        topTenSimilarRepositories = [idNameDictionary[index] for index in topTenSimilarRepositoryIndices]

        # calculate the ranking accuracy
        accuracy = calculateAccuracy(repositoryName ,topTenSimilarRepositories)
        print(repositoryName, "is found to be similar to", topTenSimilarRepositories, "with an accuracy of", accuracy)
        accuracySum += accuracy

    return accuracySum/ len(idNameDictionary)


# Get the n (default 10) most similar repository indices to the given repository index
def getNmostSimilarRepositories(similarityMatrix, repositoryIndex, n = 10) -> List[int]:
    similarRepositories = similarityMatrix[repositoryIndex]
    return similarRepositories.argsort()[-n:-1]


# calculate how many of the expected repositors where in the top n similar repositories and give the result as a percentage
def calculateAccuracy(repositoryName, similarRepositories) -> float:
    expectedRepositores = getValidatedSimilarRepository(repositoryName)
    validatedIntersection = intersection(similarRepositories, expectedRepositores)
    expectedIntersection = len(expectedRepositores) - 1
    accuracy = len(validatedIntersection)/ expectedIntersection

    return accuracy


# get the manually validated similar repositories, expected to be ranked highly in our similarity ranking for a specific repository
def getValidatedSimilarRepository(repositoryName):
    httpList = ['httputil', 'http-client', 'async-http-client', 'http-request', 'okhttp', 'netty-http-client', 'google-http-java-client']
    tictacToeList = ['ticTacToe', 'TicTacToe-MVVM', 'ticTacToe2', 'Tic-Tac-Toe', 'ticTacToe3', 'tic-tac-toe-android-app']
    calendarList = ['EasyCalendar', 'android-calendar-card', 'Material-Calendar-View', 'calendar', 'Etar-Calendar', 'CosmoCalendar', 'CalendarListview']
    oauthList = ['signpost', 'scribejava', 'spring-security-oauth', 'apis', 'oauth2-shiro', 'oauth2-server']
    dataBaseDriver = ['sqlite-jdbc', 'neo4j-java-driver', 'arangodb-java-driver', 'snowflake-jdbc', 'mssql-jdbc']

    return flatten([subList for subList in [httpList, tictacToeList, calendarList, oauthList, dataBaseDriver] if repositoryName in subList])


from typing import List, Any

#Jaccard
# calculate the similarity of two lists with Jaccard-Coefficient
# the return values ranges from 0 to 1, higher values are more similar
def calculateJaccardSimilarity(topicSetLeft: List[Any], topicSetRight: List[Any]) -> float:
    combinedElements: int = len(union(topicSetLeft, topicSetRight))
    commonElements: int = len(intersection(topicSetLeft, topicSetRight))
    return (commonElements / combinedElements)


# implements union for two lists of variable sizes
def union(setLeft: List[Any], setRight: List[Any]) -> List[Any]:
    return list(set(setLeft) | set(setRight))


# implements intersection for two lists of variable sizes
def intersection(setLeft: List[Any], setRight: List[Any]) -> List[Any]:
    return list(set(setLeft) & set(setRight))


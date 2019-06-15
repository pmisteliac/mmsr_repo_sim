from typing import List, Any

# a little helper to flatten lists, not flattening strings
def flatten(unevenList: List[Any]) -> List[Any]:
    flattenedList = []
    for subList in unevenList:
        if isinstance(subList, list) and not isinstance(subList, (str, bytes)):
            for element in subList:
                flattenedList.append(element)
        else:
            flattenedList.append(subList)
    return flattenedList

# make all strings in a list to lower
def toLower(termList: List[str]) -> List[str]:
    return list(map(lambda term: term.lower(), termList))
# https://leetcode.com/problems/find-words-containing-character/
def findWordsContaining(words: list, x: str) -> list:
    result = []
    for index, element in enumerate(words):
        if x in element:
            result.append(index)
    return result

# Test cases
print(findWordsContaining(["abc","deq","mee","aqq","dkd","ccc"], "a")) # [0,3]
print(findWordsContaining(["a","b","c"], "z")) # []
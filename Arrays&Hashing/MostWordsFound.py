# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
def mostWordsFound(sentences: list[str]) -> int:
    return max([len(i.split(" ")) for i in sentences])

# Test Cases
print(mostWordsFound(["hello world","hello world hello world","hello world hello world hello world"])) # 6
print(mostWordsFound(["hello","world","hello world"])) # 2
print(mostWordsFound(["hello","world","hello world hello world"])) # 4
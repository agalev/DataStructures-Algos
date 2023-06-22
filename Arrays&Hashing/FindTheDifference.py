# https://leetcode.com/problems/find-the-difference/description/
def findTheDifference(s: str, t: str) -> str:
    sortedS = sorted(s)
    sortedT = sorted(t)

    for i in range(len(sortedS)):
        if sortedS[i] != sortedT[i]:
            return sortedT[i]
    return sortedT[-1]

print(findTheDifference("abcd", "abcde")) # "e"
print(findTheDifference("", "y")) # "y"
print(findTheDifference("a", "aa")) # "a"
print(findTheDifference("ae", "aea")) # "a"

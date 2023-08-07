# https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/
def countConsistentStrings(allowed: str, words: list[str]) -> int:
    result = 0
    for i in words:
        for j in range(len(i)):
            if i[j] not in allowed:
                break
            if j == len(i)-1:
                result+=1
    return result

# Test Cases
print(countConsistentStrings('ab', ["ad","bd","aaab","baa","badab"])) # return 2
print(countConsistentStrings('abc', ["a","b","c","ab","ac","bc","abc"])) # return 7
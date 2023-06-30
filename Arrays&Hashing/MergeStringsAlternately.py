# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
def mergeAlternately(word1: str, word2: str) -> str:
    array1 = list(word1)
    array2 = list(word2)
    result = []

    if len(array1) > len(array2):
        for i in range(len(array2)):
            result.append(array1[i])
            result.append(array2[i])
        [result.append(i) for i in array1[len(array2):]]
    else:
        for i in range(len(array1)):
            result.append(array1[i])
            result.append(array2[i])
        [result.append(i) for i in array2[len(array1):]]
    
    return ''.join(result)

print(mergeAlternately("abc", "pqr")) # "apbqcr"
print(mergeAlternately("ab", "pqrs")) # "apbqrs"
print(mergeAlternately("abcd", "pq")) # "apbqcd"
print(mergeAlternately("ab", "pq")) # "apbq"
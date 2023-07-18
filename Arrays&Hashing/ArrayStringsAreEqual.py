# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
def arrayStringsAreEqual(word1, word2):
    str_1 = ''
    str_2 = ''

    for i in word1:
        str_1 += i
    for i in word2:
        str_2 += i
    if str_1 == str_2:
        return True
    else:
        return False

# Test Cases
print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"])) # True
print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"])) # False
print(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])) # True
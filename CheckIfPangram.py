# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
def checkIfPangram(sentence: str) -> bool:
    pangramic = []
    for i in sentence:
        if i not in pangramic:
            pangramic.append(i)
    return True if len(pangramic) == 26 else False

# Test Cases
print(checkIfPangram('thequickbrownfoxjumpsoverthelazydog')) # return True
print(checkIfPangram('leetcode')) # return False
print(checkIfPangram('abcdefghijklmnopqrstuvwxyz')) # return True
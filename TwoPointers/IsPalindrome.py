# https://leetcode.com/problems/palindrome-number/description/
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    array = list(str(x))
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex < rightIndex:
        if array[leftIndex] != array[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True

print(isPalindrome(121)) # True
print(isPalindrome(-121)) # False
print(isPalindrome(10)) # False
print(isPalindrome(-101)) # False
print(isPalindrome(0)) # True
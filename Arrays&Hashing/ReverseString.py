# https://leetcode.com/problems/reverse-string/description/
def reverseString(s: list) -> list:
    left = 0
    right = len(s)-1

    while left < right:
        templeft = s[left]
        tempright = s[right]
        s[left] = tempright
        s[right] = templeft
        left+=1
        right-=1
    return s

print(reverseString(["h","e","l","l","o"])) # ["o","l","l","e","h"]
print(reverseString(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]
print(reverseString(["a"])) # ["a"]
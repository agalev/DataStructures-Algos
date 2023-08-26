# https://leetcode.com/problems/length-of-last-word/description/
def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(" ")[-1])

print(lengthOfLastWord("Hello World")) # 5
print(lengthOfLastWord("a ")) # 1
print(lengthOfLastWord(" ")) # 0
print(lengthOfLastWord("a")) # 1
print(lengthOfLastWord("")) # 0
print(lengthOfLastWord("a b")) # 1
print(lengthOfLastWord("a b c")) # 1
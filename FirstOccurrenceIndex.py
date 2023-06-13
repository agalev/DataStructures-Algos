# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

print(strStr("hello", "ll")) # 2
print(strStr("aaaaa", "bba")) # -1
print(strStr("", "")) # 0
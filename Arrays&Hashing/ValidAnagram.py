# https://leetcode.com/problems/valid-anagram/
def isAnagram(s: str, t: str) -> bool:
    # sortS = list(s)
    # sortT = list(t)
    # sortS.sort()
    # sortT.sort()
    # print (sortS == sortT)
    # return sortS == sortT
    return sorted(list(s)) == sorted(list(t))

print(isAnagram("anagram", "nagaram")) # True
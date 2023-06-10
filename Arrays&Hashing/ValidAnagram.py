# https://leetcode.com/problems/valid-anagram/
def isAnagram(s: str, t: str) -> bool:
    # return sorted(list(s)) == sorted(list(t))
    sortS = list(s)
    sortT = list(t)
    sortS.sort()
    sortT.sort()
    print (sortS == sortT)
    return sortS == sortT

isAnagram("anagram", "nagaram") # True
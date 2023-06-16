# https://leetcode.com/problems/isomorphic-strings/description/
def isIsomorphic(s: str, t: str) -> bool:
    sMap = {}
    tMap = {}

    for i in range(len(s)):
        if s[i] not in sMap and t[i] not in tMap:
            sMap[s[i]] = t[i]
            tMap[t[i]] = s[i]
        elif s[i] in sMap and sMap[s[i]] == t[i]:
            continue
        else:
            return False
    return True

print(isIsomorphic("egg", "add")) # True
print(isIsomorphic("foo", "bar")) # False
print(isIsomorphic("paper", "title")) # True
print(isIsomorphic("ab", "aa")) # False
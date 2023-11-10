# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/
def isAcronym(words: list[str], s: str) -> bool:
    result = ''
    for i in words:
        result += i[0]
    if result == s:
        return True
    else:
        return False

print(isAcronym(["Self","Driving","Car"], "SDC")) # True
print(isAcronym(["Self","Driving","Car"], "SDCC")) # False
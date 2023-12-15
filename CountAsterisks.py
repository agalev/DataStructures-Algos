# https://leetcode.com/problems/count-asterisks/
def countAsterisks(s: str) -> int:
    result = 0
    inside_bars = False
    for i in s:
        if inside_bars == False and i == '*':
            result += 1
        elif inside_bars == False and i == '|':
            inside_bars = True
        elif inside_bars == True and i == '|':
            inside_bars = False
    return result

# Test cases
print(countAsterisks("|**|*|*")) # 1
print(countAsterisks("****")) # 4
print(countAsterisks("|**|")) # 0
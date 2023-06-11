# https://leetcode.com/problems/roman-to-integer/description/
def romanToInt(s: str) -> int:
    Romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(s)):
        if (i != len(s)-1 and Romans[s[i]] < Romans[s[i+1]]):
            result -= Romans[s[i]]
        else:
            result += Romans[s[i]]
    return result

print(romanToInt("III")) # 3
print(romanToInt("IV")) # 4
print(romanToInt("IX")) # 9
print(romanToInt("LVIII")) # 58
print(romanToInt("MCMXCIV")) # 1994
# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
def balancedStringSplit(s: str) -> int:
    result = 0
    L_count, R_count = 0, 0
    for i in list(s):
        if i == 'L':
            L_count += 1
        else:
            R_count += 1
        if L_count == R_count:
            result += 1
            L_count, R_count = 0, 0
    return result

# Test Cases
print(balancedStringSplit('RLRRLLRLRL')) # return 4
print(balancedStringSplit('RLLLLRRRLR')) # return 3
print(balancedStringSplit('LLLLRRRR')) # return 1
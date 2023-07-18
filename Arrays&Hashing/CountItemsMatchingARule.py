# https://leetcode.com/problems/count-items-matching-a-rule/description/
def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    key_index = int
    result = 0

    if ruleKey == "type":
        key_index = 0
    elif ruleKey == "color":
        key_index = 1
    elif ruleKey == "name":
        key_index = 2


    for i in range(len(items)):
        if items[i][key_index] == ruleValue:
            result += 1

    return result

# Test Cases
print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")) # 1
print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")) # 2
print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "name", "iphone")) # 1
# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    map = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    stack = []
    for c in range(len(s)):
        if s[c] in list(map.values()):
            stack.append(s[c])
        elif len(stack) > 0 and map[s[c]] == stack[-1]:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
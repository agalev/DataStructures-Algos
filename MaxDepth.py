# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/
def maxDepth(s: str) -> int:
    stack = []
    result = 0
    for i in s:
        if i == '(':
            stack.append(i)
            if len(stack) > result:
                result = len(stack)
        elif i == ')':
            stack.pop()
    return result
                
# Test Cases
print(maxDepth('(1+(2*3)+((8)/4))+1')) # return 3
print(maxDepth('(1)+((2))+(((3)))')) # return 3
print(maxDepth('1+(2*3)/(2-1)')) # return 1
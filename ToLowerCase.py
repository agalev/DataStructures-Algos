# https://leetcode.com/problems/to-lower-case/submissions/
def toLowerCase(s: str) -> str:
    return ''.join([i.lower() for i in s])

# Test Cases
print(toLowerCase('Hello')) # return 'hello'
print(toLowerCase('here')) # return 'here'
print(toLowerCase('LOVELY')) # return 'lovely'
print(toLowerCase('al&phaBET')) # return 'al&phabet'
print(toLowerCase('')) # return ''
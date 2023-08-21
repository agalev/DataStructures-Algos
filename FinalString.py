# https://leetcode.com/problems/faulty-keyboard/submissions/
def finalString(s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i] == 'i':
                result.reverse()
            else:
                result.append(s[i])
        return ''.join(result)

# Test Cases
print(finalString('abc')) # return 'abc'
print(finalString('string')) # return 'rtsng'
print(finalString('')) # return ''
print(finalString('i')) # return 'i'
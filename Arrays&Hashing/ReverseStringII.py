# https://leetcode.com/problems/reverse-string-ii/description/
def reverseStr(s: str, k: int) -> str:
    array = list(s)
    result = []
    iterator = 0
    skip = False

    if k >= len(array):
        return ''.join(reversed(array))
    
    for i in range(0,len(array),k):
        iterator += k
        if skip == False:
            result.append("".join(reversed(array[i:iterator])))
            skip = True
        else:
            result.append("".join(array[i:iterator]))
            skip = False

    return ''.join(result)

print(reverseStr("abcdefg",2)) # "bacdfeg"
print(reverseStr("abcd",2)) # "bacd"
print(reverseStr("abcdefg",8)) # "gfedcba"
print(reverseStr("abcdefg",1)) # "abcdefg"
# https://leetcode.com/problems/longest-common-prefix/description/
def longestCommonPrefix(strs: list) -> str:
    result = ''
    # if len(strs) == 1:
    #     return strs[0]
    # for i in range(len(strs[0])):
    #     for j in range(1, len(strs)):
    #         if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
    #             return result
    #     result += strs[0][i]
    # return result
    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            return result
        result += strs[0][i]
    return result

print(longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(longestCommonPrefix(["dog","racecar","car"])) # ""
